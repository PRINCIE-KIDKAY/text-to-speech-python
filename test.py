import pyttsx3
import whisper
from fastapi import FastAPI
from whisper import load_model
import subprocess
import requests

app = FastAPI()
  # or "small", "medium", etc.

def gtts_voices(text):
    from gtts import gTTS

    tts = gTTS(text=text, lang='en', tld='co.zaco.za')
    tts.save('hello.mp3')

def speech_to_text():
    model = load_model("base")
    # load audio and pad/trim it to fit 30 seconds
    result = model.transcribe("test.mp3")
    print(result["text"])
    return result["text"]

    # text_to_speech(result["text"])

def text_to_speech(text):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 140)
    #
    engine.say(text)
    # engine.save_to_file(text, 'test.mp3')

    engine.runAndWait()
    engine.stop()


if __name__ == "__main__":
    text = """
    Hi khumbelo. Get up to R800 back on your monthly fuel spend with Discovery Insure. Reply Yes or No to opt out. Std rates limits Ts&Cs apply. Iconaf Auth FSP
    """
    gtts_voices(text)
    # res = speech_to_text()
    # text_to_speech(res)

# speech_to_text()