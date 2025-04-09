import speech_recognition as sr
import time

class SpeechRecognizer:

    #This constructior will initialize the recognizer and set the energy threshold and pause threshold
    def __init__(self):
        self.recognizer = sr.Recognizer() 
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.dynamic_energy_adjustment_damping = 0.15
        self.recognizer.dynamic_energy_ratio = 1.5
        self.recognizer.pause_threshold = 1.2 
        self.recognizer.energy_threshold = 300 

    #Function to adjust for ambient noise
    def adjust_for_ambient_noise(self):
        with sr.Microphone() as source:    
            print("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=5)
            print("Ambient noise adjusted.")
            time.sleep(0.5)

    #Continuously listen for speech and print the recognized text
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")           
            try:
                audio = self.recognizer.listen(source, timeout=10,phrase_time_limit=20)
                try:
                    print("Recognizing...")
                    text = self.recognizer.recognize_google(audio, language="en-US",show_all=False)
                    print(f"Recognized: {text}")
                    return text
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
            time.sleep(0.1)

if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    recognizer.adjust_for_ambient_noise()
    recognizer.listen()

# Note: The above code will continuously listen for speech and print the recognized text.

    