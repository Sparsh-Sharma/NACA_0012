import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
from numpy import *
import matplotlib.pylab as pylab


def L_p(x):
	return 10*np.log10(x**2/4.e-10)

blocksize=4096
j=0

filename = 'Tu_038_GA_dt=001 - Copy.csv'
df = pd.read_csv(filename, usecols=[3])
df2 = pd.read_csv(filename, usecols=[0])
print (df)

(werte,freq)=plt.psd(df, NFFT=blocksize, Fs=51200, detrend=mlab.detrend_none,window=mlab.window_hanning, noverlap=0.75*blocksize, pad_to=None,sides='default', scale_by_freq='True')
#xx=30


pegel=L_p(werte*0.950065396**2)
#freq=freq[xx:]
#plt.plot()

#pegel=L_p(df)
#plt.plot()
	
#Sr=freq*durchmesser/U
#solldrucklist=[1000,1200,1500,1700]
alphalist=[0.25,0.5,0.75,1.0]
stylelist=['--','-.',':','-']

plt.figure(1,figsize=(8.4/2.54,4.0/2.54))
plt.semilogx(freq,pegel,linestyle=stylelist[j],linewidth=0.6,alpha=alphalist[j])
j+=1
plt.show()



Y    = np.fft.fft(df)
freq = np.fft.fftfreq(len(df2), 0.001)