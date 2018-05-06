import os
from watson_developer_cloud import TextToSpeechV1

tts = TextToSpeechV1(
    username='c6111125-b9ad-4ecf-83b2-5258b04e5d99',
    password='ShsWI0ilPixm')

def speak (result):
	with open('./output.wav', 'wb') as audio_file:
		audio_file.write(tts.synthesize(result, accept='audio/wav', voice="en-US_AllisonVoice").content)
	print("Allison says")
	os.system("mpv output.wav")