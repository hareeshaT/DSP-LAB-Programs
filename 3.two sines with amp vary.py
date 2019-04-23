import matplotlib.pyplot as plot
import numpy as np
f1=5
Fs=100
A=5
A1=15
sample=1000
x=np.arange(sample)
y=A*np.sin((2*np.pi*f1*x/Fs)+90)
plot.subplot(3,1,1)
plot.plot(x,y)
y1=A1*np.sin((2*np.pi*f1*x/Fs)+90)
plot.subplot(3,1,2)
plot.plot(x,y1)  
z=y+y1
plot.subplot(3,1,3)
plot.plot(z)
plot.show()


