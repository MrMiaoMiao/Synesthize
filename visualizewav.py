from dtw import dtw
import matplotlib.pyplot as plot
from scipy.io import wavfile

def visualize_sound(infile):
	samplingFrequency, signalData = wavfile.read(infile)

	plot.subplot(211)
	plot.title('Spectrogram of a wav file')
	plot.plot(signalData)
	plot.xlabel('Sample')
	plot.ylabel('Amplitude')

	# plot.subplot(212)
	# plot.specgram(signalData,Fs=samplingFrequency)
	# plot.xlabel('Time')
	# plot.ylabel('Frequency')

	plot.show()