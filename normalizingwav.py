import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plot
import matplotlib as mpl
from pydub import AudioSegment


def normalizeInput(infile, tarfile): 
	inputFreq, inputaudio = wavfile.read(infile)
	targetFreq, targetaudio = wavfile.read(tarfile) 

	'''
	plot.subplot(211)
	plot.title('Spectrogram of input audio')
	plot.plot(inputaudio)
	plot.xlabel('Audio')
	plot.ylabel('Amplitude')
	with mpl.rc_context(rc={'interactive': False}):
	    plot.show()
	'''
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


	'''
	print("a_mean")
	print(a_mean)
	print("t_mean")
	print(t_mean)


	plot.subplot(211)
	plot.title('Spectrogram of target')
	plot.plot(target)
	plot.xlabel('Audio Input')
	plot.ylabel('Amplitude')
	with mpl.rc_context(rc={'interactive': False}):
	    plot.show()
	'''

	factor = t_mean / a_mean
	resultAudio = [x * factor for x in audio]
	resultAudio.export(infile, format="wav")

	'''
	plot.subplot(211)
	plot.title('Spectrogram of normalized audio')
	plot.plot(result)
	plot.xlabel('Audio Input')
	plot.ylabel('Amplitude')
	with mpl.rc_context(rc={'interactive': False}):
	    plot.show()
	'''

