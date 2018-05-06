try:
    import speech_recognition as sr
    import json
    import os
    from pprint import pprint

    import texttospeech as tts
    import stereotomono as stm
    import visualizewav as viz
    import mictowav as mic
    r = sr.Recognizer()

    file = sr.AudioFile('file.wav')
    with file as source:
        audio = r.record(source)
        r.adjust_for_ambient_noise(source)
        try:
            pprint(r.recognize_google(audio, show_all=True))  # pretty-print the recognition result
            result = r.recognize_google(audio)
            print("You said " + result)
            viz.visualize_sound("./file.wav")
            words = result.lower()
            if words=="stop":
                break
            tts.speak(result)
            stm.stereo_to_mono("./output.wav", "./output.wav")
            viz.visualize_sound("./output.wav")
            # os.system("rm output.wav")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


    print ('done')
    viz.pause()
except KeyboardInterrupt:
    print('okay see you later')