from pydub import AudioSegment

def stereo_to_mono(infile, outfile):
	mysound = AudioSegment.from_wav(infile)
	mysound = mysound.set_channels(1)
	mysound.export(outfile, format="wav")