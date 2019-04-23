import numpy as np
import matplotlib.pyplot as plot
def sine(p,q,r):
	time=np.arange(0,10,0.1);
	amplitude=np.cos((q*time)+r)
	y=amplitude*p
	return y
	time=np.arange(0,10,0.1);
	A=input("enter the amplitude")
	f1=input("enter the first frequency")
	f2=input("enter the second frequency")
	p1=input("enter the first phase")
	p2=input("enter the second phase")
	h1=sine(A,f1,p1)
	h2=sine(A,f1,p2)
	h3=sine(A,f2,p1)
	h4=sine(A,f2,p2)
c=h1+h2+h3+h4
plot.plot(time,c)
plot.show( )	
