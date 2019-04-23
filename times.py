import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('voice.wav')
#fs,data=wav.read('voice.wav')
fs2,data2=wav.read('low_voice.wav')
print(fs,fs2)
t1=np.arange(0,len(data)/fs,1.0/fs)
t2=np.arange(0,len(data2)/fs2,1.0/fs2)
#print(data)
a1=plt.subplot(2,1,1)
a1=plt(t1,data[0:len(t1)])
a2=plt.subplot(2,1,2,sharex=a1)
a2=plt.(t2,data2[0:len(t2)])
#plt.plt(data)
plt.show( )
#wav.write('low_voice.wav',fs,data)
