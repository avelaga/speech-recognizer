from twython import Twython
import speech_recognition as sr
from keys import apiKey, apiSecret, accessToken, accessTokenSecret

r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

#https://twitter.com/testpibot
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

tweetStr = "abhi is a butt"

#r.pause_threshold = 0.5

while True:
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.record(source, duration=10)
	try:
		tweetStr = r.recognize_google(audio)
		print(tweetStr)
		if len(tweetStr) > 1:
			api.update_status(status=tweetStr)
	except:
		print("**** failed *****")
