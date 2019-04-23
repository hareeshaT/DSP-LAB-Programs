import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
fs,data=wav.read('voice.wav')
print(fs)
print(data)
plt.plt(data)
plt.show( )
wav.write('low_voice.wav',fs,data)
