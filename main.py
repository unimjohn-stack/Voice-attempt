from gtts import gTTS
import playsound

def speak(text):
    tts=gTTS(text=text, lang="ru")
    filename = "voice.mp3"
    tts.save(filename)

    playsound.playsound(filename)

speak("Hello John, your voice assistant is working.")