from dtw import dtw
import matplotlib.pyplot as plot
from scipy.io import wavfile
import numpy as np

def visualize_sound(infile,tarfile, word):
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
	plot.title(word)
	plot.xlabel('Sample')
	plot.ylabel('Amplitude')
	plot.plot(resultAudio, label="sample audio", color="blue", alpha=0.5)
	plot.plot(targetaudio, label="target audio", color="yellow", alpha=0.5)
	plot.show()

def pause():
	plot.show()