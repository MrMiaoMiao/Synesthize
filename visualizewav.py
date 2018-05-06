from dtw import dtw
import matplotlib.pyplot as plot
from scipy.io import wavfile
import numpy as np

def visualize_sound(infile,tarfile):
	inputFrequency, inputaudio = wavfile.read(infile)
	targetFreq, targetaudio = wavfile.read(tarfile) 

	audio = np.array(inputaudio)
	target = np.array(targetaudio)

	a = 0
	a_sum = 0
	for x in audio:
		if (x.all() > 0):
			a_sum += x
			a+=1
	a_mean = a_sum/a

	t = 0
	t_sum = 0
	for x in target:
		if (x.all()> 0):
			t_sum += x
			t+=1
	t_mean = t_sum/t


	factor = t_mean / a_mean
	resultAudio = [x * factor for x in audio]


	plot.figure(1)
	plot.subplot(211)
	plot.title('Spectrogram of a wav file')
	plot.plot(resultAudio)
	plot.xlabel('Sample')
	plot.ylabel('Amplitude')

	plot.subplot(212)
	plot.specgram(resultAudio,Fs=inputFrequency)
	plot.xlabel('Time')
	plot.ylabel('Frequency')

	plot.figure(2)
	plot.subplot(211)
	plot.title('Spectrogram of a wav file')
	plot.plot(targetaudio)
	plot.xlabel('Sample')
	plot.ylabel('Amplitude')

	plot.subplot(212)
	plot.specgram(targetaudio,Fs=targetFreq)
	plot.xlabel('Time')
	plot.ylabel('Frequency')

	plot.show()

def pause():
	plot.show()