import speech_recognition as sr
import time

class SpeechRecognizer:

    #This constructior will initialize the recognizer and set the energy threshold and pause threshold
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300  
        self.recognizer.pause_threshold = 0.8  

    #Function to adjust for ambient noise
    def adjust_for_ambient_noise(self):
        with sr.Microphone() as source:    
            print("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Ambient noise adjusted.")

    #Continuously listen for speech and print the recognized text
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            while True:
                try:
                    audio = self.recognizer.listen(source, timeout=5,phrase_time_limit=10)
                    try:
                        print("Recognizing...")
                        text = self.recognizer.recognize_google(audio)
                        print(f"Recognized: {text}")
                    except sr.UnknownValueError:
                        print("Sorry, I did not understand that.")
                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")
                    
                except sr.WaitTimeoutError:
                    print("No speech detected within timeout")
                except Exception as e:
                        print(f"An error occurred: {e}")
                except KeyboardInterrupt:
                    print("\nStopping the speech recognition...")
                    break
                time.sleep(0.1)

if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    recognizer.adjust_for_ambient_noise()
    recognizer.listen()

# Note: The above code will continuously listen for speech and print the recognized text.

    