import numpy as np
import matplotlib.pyplot as plt
n=input("enter the no of samples for first signal ")
X=[ ]
for i in range(0,n):
	A1=input("enter the samples")
	X.append(A1)
print(X)
plt.subplot(3,1,1)
plt.stem(X)
k=input("enter the no of samples for second signal")
h=[ ]
for j in range(0,k):
	A2=input("enter the samples")
	h.append(A2)
print(h)
plt.subplot(3,1,2)
plt.stem(h)
y=[ ]
p=n+k-1
f=np.arange(0,p,1)
while(n<p):
	X.append(0)
	n=n+1
for i in range(0,p):
	sum=0
	for j in range(0,k):
		z=h[j]*X[i-j]
		sum=sum+z
	y.append(sum)
print(y)
plt.subplot(3,1,3)
plt.stem(y)
plt.show( )
