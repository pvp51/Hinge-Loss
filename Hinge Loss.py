import sys
import math
import random

eta = 0.01
stop_condition=0.001

datafile=sys.argv[1]
f1 = open(datafile,'r')

data = []
l = f1.readline()

while(l!=''):
	a = l.split()
	l = []
	for j in range(0,len(a),1):
		l.append(float(a[j]))
	l.append(1)
	data.append(l)
	l=f1.readline()

rows = len(data)
cols = len(data[0])
f1.close()


labelfile = sys.argv[2]
f2 = open(labelfile,'r')

trainlabels = {}
n = [0,0]
l2 = f2.readline()

while (l2!=''):
	a = l2.split()
	l2 = []
	trainlabels[int(a[1])] = int(a[0])
	if (int (a[0]) == 0):
		trainlabels[int(a[1])]=-1
		
	l2=f2.readline()
f2.close()

w = {}
for j in range(0,cols,1):
	w[j] = random.uniform(-.01, .01)


def dot_product(aa,bb):
	dp = 0
	for j in range(0,cols,1):
		dp += float(aa[j]*bb[j])
	return dp

previous = 0
df1 = 0
current = 100
while (abs(previous - current)<0.000000001):
	dellf = [0]*cols
	for i in range(0,rows,1):
		if (trainlabels.get(i) is not None):
			df1 = dot_product(w,data[i])
			for j in range(0,cols,1):
				gradient = trainlabels.get(i)*df1
				if gradient<1:
					dellf[j] += trainlabels.get(i)*data[i][j]
				else:
					dellf[j] += 0

	for j in range(0,cols,1):
		w[j]=w[j]+eta*dellf[j]

	previous = current
	current = 0
	for i in range(0,rows,1):
		if (trainlabels.get(i) is not None):
			current+=max(0, (1-trainlabels.get(i)*dot_product(w,data[i])))

normw = 0
for j in range(0, cols-1, 1):
    normw += w[j]**2

print('W',w);

normw = (normw)**0.5
print("||W||=",normw)
d_origin = abs(float(w[cols-1])/normw)
print ("distance to origin= %.6f" % (d_origin))

dp = 0
for i in range(0,rows,1):
	if (trainlabels.get(i) is None):
		dp=dot_product(w,data[i])
		#print(dp)
		if dp>0:
			print ("%d %d" % (1, i))
		else:
			print ("%d %d" % (-1, i))
