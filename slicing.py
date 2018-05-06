from pydub import AudioSegment

def slice(infile, timestamps):
	audio = AudioSegment.from_wav(infile)
	i = 0
	for time in timestamps:
		piece = audio[time[1] * 1000 : time[2] * 1000]
		piece.export("chunk" + str(i) + ".wav", format="wav")
		i = i + 1
		print("you said \"" + time[0] + "\" between " + str(time[1]) + " and " + str(time[2]))
	return i