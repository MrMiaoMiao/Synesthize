from dtw import dtw
from oct2py import octave

import matplotlib.pyplot as plot
from scipy.io import wavfile
import numpy as np

'''
inputwav = audioread('file.wav')
correctwav = audioread('real.wav')

frequencies = np.arange(5,105,5)


samplingFrequency = 400


s1 = np.empty([0]) # For samples
s2 = np.empty([0]) # For signal


start = 1
stop = samplingFrequency + 1


for frequency in frequencies:
	sub1 = np.arange(start, stop, 1)
	# Signal - Sine wave with varying frequency + Noise
	sub2 = np.sin(2*np.pi*sub1*frequency*1/samplingFrequency)+np.random.randn(len(sub1))

	s1 = np.append(s1, sub1)
    s2 = np.append(s2, sub2)
 
	start = stop+1
	stop = start+samplingFrequency


# Plot the signal
plot.subplot(211)
plot.plot(s1,s2)
plot.xlabel('Sample')
plot.ylabel('Amplitude')


# Plot the spectrogram
plot.subplot(212)
powerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(s2, Fs=samplingFrequency)
plot.xlabel('Time')
plot.ylabel('Frequency')

plot.show()   

'''

'''
[wave1,Fs1] = audioread('audio1.wav');
      [wave2, Fs2] = audioread('audio2.wav');
      dtw(wave1,wave2);
'''




#more stuff

#import the pyplot and wavfile modules 
from pydub import AudioSegment
#import audioop
from struct import pack
from math import sin, pi
import wave
import random

RATE=44100


wv = wave.open('test_mono.wav', 'w')
wv.setparams((1, 2, RATE, 0, 'NONE', 'not compressed'))
maxVol=2**15-1 #maximum amplitude
wvData=""
for i in range(0, RATE*3):
	wvData+=pack('h', int(maxVol*sin(i*500/RATE))) #500Hz
wv.writeframes(wvData)


# Read the wav file (mono)
samplingFrequency, signalData = wv
 

# Plot the signal read from wav file
plot.subplot(211)
plot.title('Spectrogram of input wav file')

plot.plot(signalData)
plot.xlabel('Sample')
plot.ylabel('Amplitude')

plot.subplot(212)
plot.specgram(signalData,Fs=samplingFrequency)
plot.xlabel('Time')
plot.ylabel('Frequency')


plot.show()