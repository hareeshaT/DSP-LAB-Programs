import matplotlib.pyplot as plot
import numpy as np
x=input("enter x samples")
lx=len(x)
y=[ ]
for i in range (0,lx):
	y=np.append(y,x[lx-i-1])
print y