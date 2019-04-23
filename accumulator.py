import numpy as np
import matplotlib.pyplot as plt
n=input("enter the no of samples")
a=[ ]
for i in range(0,n):
y=input("enter the samples")
a.append(y)
print(a)
plt.subplot(2,1,1)
plt.stem(a)
h=0
avrg=[ ]
for i in range(0,n):
h += a[i]
avrg.append(h)
print(avrg)
plt.subplot(2,1,2)
plt.stem(avrg)
plt.show( )
