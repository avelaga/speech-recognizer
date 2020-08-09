import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

while True:
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	try:
		print(r.recognize_google(audio))
	except:
		print("**** failed *****")
