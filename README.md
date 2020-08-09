# Speech Recognizer
made with the help of https://realpython.com/python-speech-recognition/

### To setup microphone access on linux:
`sudo apt-get install python-pyaudio python3-pyaudio`

### To test if everything is working:
`python -m speech_recognition`

### To find microphone to use:
```
import speech_recognition as sr
sr.Microphone.list_microphone_names()
```
##### To set microphone:
`mic = sr.Microphone(device_index=3)`
