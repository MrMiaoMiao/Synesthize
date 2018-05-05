import speech_recognition as sr
import json
import os
from watson_developer_cloud import TextToSpeechV1

tts = TextToSpeechV1(
    username='c6111125-b9ad-4ecf-83b2-5258b04e5d99',
    password='ShsWI0ilPixm')
print(json.dumps(tts.list_voices(), indent=2))

r = sr.Recognizer()

mic = sr.Microphone()

with mic as source:             
    print("listening...")
    while True:

        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=0.5)
        # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            result = r.recognize_google(audio)
            print("You said " + result)
            words = result.lower()
            if words=="stop":
                break
            with open('./output.wav', 'wb') as audio_file:
                audio_file.write(
                    tts.synthesize(result, accept='audio/wav', voice="en-US_AllisonVoice").content)
            print("Allison says")
            os.system("mpv output.wav")
            os.system("rm output.wav")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except LookupError:
            print("Please, speak more clearly")     

'''
file = sr.AudioFile('file.wav')
with file as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.record(source)
'''
print("done")



'''
['HDA NVidia: HDMI 0 (hw:0,3)', 
'HDA NVidia: HDMI 1 (hw:0,7)', 
'HDA NVidia: HDMI 2 (hw:0,8)', 
'HDA NVidia: HDMI 3 (hw:0,9)', 
'HD Pro Webcam C920: USB Audio (hw:1,0)', 
'HD-Audio Generic: ALC1220 Analog (hw:2,0)', 
'HD-Audio Generic: ALC1220 Digital (hw:2,1)', 
'HD-Audio Generic: ALC1220 Alt Analog (hw:2,2)', 
'HD-Audio Generic: ALC1220 Analog (hw:2,4)', 
'hdmi', 'pulse', 'default']
'''
