import matplotlib.pyplot as plot
from scipy.io import wavfile
import numpy as np

def visualize_sound(infile,tarfile, word):
	inputFrequency, inputaudio = wavfile.read(infile)
	targetFreq, targetaudio = wavfile.read(tarfile) 

	fig=plot.figure()
	ax=fig.add_subplot(111, label="1")
	ax2=fig.add_subplot(111, label="2", frame_on=False)

	ax.plot(inputaudio, label="original audio", color="green", alpha=0.5)
	ax.set_xlabel("Original Sample (s)", color="C0")
	ax.set_ylabel("Original Amplitude", color="C0")
	ax.tick_params(axis='x', colors="C0")
	ax.tick_params(axis='y', colors="C0")
	
	ax2.plot(targetaudio, label="sample audio", color="blue", alpha=0.5)
	ax2.xaxis.tick_top()
	ax2.yaxis.tick_right()
	ax2.set_xlabel('Target Sample (s)', color="C1") 
	ax2.set_ylabel('Target Amplitude', color="C1")       
	ax2.xaxis.set_label_position('top') 
	ax2.yaxis.set_label_position('right') 
	ax2.tick_params(axis='x', colors="C1")
	ax2.tick_params(axis='y', colors="C1")

	plot.show()

def pause():
	plot.show()