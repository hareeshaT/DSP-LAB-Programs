import matplotlib.pyplot as plt
import numpy as np
f1=50
f2=70
Fs=5000
A=10
sample=10000
x=np.arange(sample)
y=A*np.sin((2*np.pi*f1*x/Fs)+90)
plt.subplot(511)
plt.plot(x,y)
y1=A*np.sin((2*np.pi*f2*x/Fs)+90)
plt.subplot(512)
plt.plot(x,y1)
y2=A*np.sin((2*np.pi*f1*x/Fs)+180)
plt.subplot(513)
plt.plot(x,y2)
y3=A*np.sin((2*np.pi*f2*x/Fs)+180)
plt.subplot(514)
plt.plot(x,y3)
z=y+y1+y2+y3
plt.subplot(515)
plt.plot(z)
plt.show()



