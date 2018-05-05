import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()

with mic as source:             
    print("listening...")
    while True:

        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            result = r.recognize_google(audio)
            print("You said " + result)
            words = result.lower()
            if words=="stop":
                break
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
