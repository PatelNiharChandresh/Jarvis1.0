import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 175)
        self.engine.setProperty('volume', 1.0)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    tts = TextToSpeech()
    speakThis = "Hello, I am your text-to-speech assistant."
    # Test default voice
    tts.speak(speakThis)