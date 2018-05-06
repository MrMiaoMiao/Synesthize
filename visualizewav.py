from dtw import dtw
import matplotlib.pyplot as plot
from scipy.io import wavfile

figure_count = 1

def visualize_sound(infile):
	global figure_count
	samplingFrequency, signalData = wavfile.read(infile)

	plot.figure(figure_count)
	figure_count = figure_count + 1
	plot.subplot(211)
	plot.title('Spectrogram of a wav file')
	plot.plot(signalData)
	plot.xlabel('Sample')
	plot.ylabel('Amplitude')

	plot.subplot(212)
	plot.specgram(signalData,Fs=samplingFrequency)
	plot.xlabel('Time')
	plot.ylabel('Frequency')

	plot.show(block=False)

def pause():
	plot.show()