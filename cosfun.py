import numpy as np
import matplotlib.pyplot as plot
def sine(p,q,r):
	time=np.arange(0,10,0.1);
	amplitude=np.cos((q*time)+r)
	y=amplitude*p
time=np.arange(0,10,0.1);
a1=input("enter first amplitude")
a2=input("enter second amplitude")
b1=input("enter frequency")
b2=input("enter frequency")
c1=input("enter phase")
c2=input("enter phase")
x1=sine(a1,b1,c1)
x2=sine(a2,b1,c1)
c=x1+x2
plot.plot(time,c)
plot.show( )
y1=sine(a1,b1,c1)
y2=sine(a1,b2,c1)
d=y1+y2
plot.plot(time,d)
plot.show( )
z1=sine(a1,b1,c1)
z2=sine(a1,b1,c2)
e=z1+z2
plot.plot(time,e)
plot.show( )
