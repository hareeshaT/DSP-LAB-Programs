import numpy as np
import matplotlib.pyplot as plot
import cmath as cm
def butterworth(dp,ds,wp,ws):
	h=[ ]
	a=0.5*np.log(((1/(dp)**2)-1)/((1/(ds)**2)-1))
	b=np.log(wp/ws)
	x=a/b
	N=np.ceil(x)
	wc=wp/(((1/(dp)**2)-1))**(1/(2*N))
	w=1500
	print (N)
	for j in range(w):
		t=float(1/np.sqrt((1+(2*np.pi*j/wc)**(2*N))))
		h.append(t)
	return h
dp=0.8
ds=0.2
wp=2000*np.pi
ws=5000*np.pi
h=[ ]
h=butterworth(dp,ds,wp,ws)
plot.plot(h,'b')
plot.show( )
