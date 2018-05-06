from pydub import AudioSegment

def stereo_to_mono(infile, outfile):
	mysound = AudioSegment.from_wav(infile)
	mysound = mysound.set_channels(1)
	trimmed = mysound[:-500]
	trimmed.export(outfile, format="wav")