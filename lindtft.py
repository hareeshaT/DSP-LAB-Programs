from matplotlib import pyplot as plt
import numpy as np
import cmath as cm
x1=input('Enter the first sequence:')
x2=input('Enter the second sequence:')
v1=[]
v2=[]
v1=np.append(v1,x1)
v2=np.append(v2,x2)
v=v1+v2
def dft(x):  
	l=len(x)
	j=cm.sqrt(-1)
	y=[ ]
	for k in range(0,l):
	    sum=0
	    for n in range(0,l):
	     sum=sum+(x[n]*(np.exp((-j)*(2*np.pi/l)*n*k)))
	    y=np.append(y,sum)
	return y
res1=dft(v)
print(res1)
y1=dft(x1)
y2=dft(x2)
res2=y1+y2
print(res2)
plt.subplot(211)
plt.stem(np.abs(res1))
plt.subplot(212)
plt.stem(np.abs(res2))
plt.show()

