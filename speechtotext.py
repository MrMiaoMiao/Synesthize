import json
from watson_developer_cloud import SpeechToTextV1

IBM_USERNAME = "1d951551-e18e-4f5e-8a25-a930339dea06"
IBM_PASSWORD = "vMSk7MAEfTSQ"

speech_to_text = SpeechToTextV1(
    username=IBM_USERNAME, 
    password=IBM_PASSWORD,
    url='https://stream.watsonplatform.net/speech-to-text/api')

def text_times(infile):
    with open(infile,'rb') as audio_file:
        result = speech_to_text.recognize(
                    audio=audio_file,content_type='audio/wav',
                    timestamps=True)
        timestamps = result['results'][0]['alternatives'][0]['timestamps']
        transcript = result['results'][0]['alternatives'][0]['transcript']
        confidence = result['results'][0]['alternatives'][0]['confidence']

        print(json.dumps(timestamps, indent=4))
        print("You said \"" + transcript + "\" with " + str(confidence * 100) + "% confidence")
        return timestamps, transcript, confidence
