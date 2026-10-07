# from gtts import gTTS
# import playsound

# def speak(text):
#     tts=gTTS(text=text, lang="ru")
#     filename = "voice.mp3"
#     tts.save(filename)

#     playsound.playsound(filename)

# speak("Hello John, your voice assistant is working.")

import speech_recognition as sr
import sounddevice as sd
from gtts import gTTS
import playsound


SAMPLE_RATE = 16000
CHANNELS = 1
DURATION = 5

def listen():
    print("Listening...")

    recording = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16"
    )
    sd.wait()
    print("Finished Listening.")
    audio_bytes = recording.tobytes()
    audio = sr.AudioData(
        audio_bytes, SAMPLE_RATE, 2
    )
    return audio

def speak(text):
    print("Assistant:", text)
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def respond(text):
    text = text.lower()
    if "hello" in text or "hi" in text:
        return "Hello! how are you?"
    elif "what's your name" in text:
        return "I'm your assistant"
    elif "can you hear me" in text:
        return "Yes, i can hear you clearly"
    elif "goodbye" in text:
        return "Goodbye, Have a great day."
    else:
        return "I'm not sure how to respond to that yet"

recognizer = sr.Recognizer()
audio = listen()

# with sr.Microphone() as source:
#     print("Listening...")
#     audio = recognizer.listen(source)
try:
    text= recognizer.recognize_google(audio)
    print("You said:", text)
    response = respond(text)
    speak(response)
except sr.UnknownValueError:
    print("Sorry, I could not understand you.")
except sr.RequestError as e:
    print("Could not connect to the speech recognition service:", e)