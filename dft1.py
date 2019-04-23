import numpy as np
import cmath as cm
from matplotlib import pyplot as plt
x=input ("enter the sequence")
m=len(x)
l=input('enter the number')
o=l-m
for i in range(o):
	np.append(0)
j=cm.sqrt(-1)
y=[ ]
for k in range(0,l-1):
    sum=0
    for n in range(0,l):
     sum=sum+(x[n]*(np.exp((-j)*(2*np.pi/l)*n*k)))
    y=np.append(y,sum)
print (y)
plt.stem(np.abs(y))
plt.show()