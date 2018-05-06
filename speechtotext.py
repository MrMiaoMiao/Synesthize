import speech_recognition as sr
import json
import os

import texttospeech as tts
import stereotomono as stm
import visualizewav as viz
import mictowav as mic

r = sr.Recognizer()

mic.record()
file = sr.AudioFile('file.wav')
with file as source:
    audio = r.record(source)
    r.adjust_for_ambient_noise(source, duration=0.5)
    try:
        result = r.recognize_google(audio)
        print("You said " + result)
        # words = result.lower()
        # if words=="stop":
        #     break
        tts.speak(result)
        stm.stereo_to_mono("./output.wav", "./outfile.wav")
        viz.visualize_sound("./outfile.wav")
        os.system("rm output.wav outfile.wav")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


print ('done')