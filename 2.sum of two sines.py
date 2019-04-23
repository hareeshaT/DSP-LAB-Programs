import matplotlib.pyplot as plot
import numpy as np
Fs=5000
f=5
sample=20000
x=np.arange(sample)
y=np.sin(2*np.pi*f*x/Fs)
plot.subplot(3,1,1)
plot.plot(x,y)
Fs1=8000
f1=6
y1=np.sin(2*np.pi*f1*x/Fs1)
plot.subplot(3,1,2)
plot.plot(x,y1)
z=y+y1
plot.subplot(3,1,3)
plot.plot(z)
plot.show()
 

