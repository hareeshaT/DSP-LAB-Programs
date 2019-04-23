import numpy as np
import cmath as cm
from matplotlib import pyplot as plt
x=input ("enter the sequence")
m=len(x)
l=input('enter the number')
while(l-1>m):
	x(m)=0
	m+=1
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