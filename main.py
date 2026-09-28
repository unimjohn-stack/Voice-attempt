# from gtts import gTTS
# import playsound

# def speak(text):
#     tts=gTTS(text=text, lang="ru")
#     filename = "voice.mp3"
#     tts.save(filename)

#     playsound.playsound(filename)

# speak("Hello John, your voice assistant is working.")

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
try:
    text= recognizer.recognize_google(audio)
    print("You said:", text)
except:
    print("Sorry, I could not understand you.")
except:
    print("Could not connect to the speech recognition service:", e)