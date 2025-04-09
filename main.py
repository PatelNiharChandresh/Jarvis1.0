from chat_bot import ChatBot
from speaking import TextToSpeech
from listening import SpeechRecognizer

def main():
    chatBot = ChatBot()
    speechRecognizer = SpeechRecognizer()
    textToSpeech = TextToSpeech()
    speechRecognizer.adjust_for_ambient_noise()
    while True:
        user_message = speechRecognizer.listen()
        if user_message.lower() == "exit":
            textToSpeech.speak("Exiting the chat.")
            break
        if user_message is not None:
            assistant_response = chatBot.talk_to_bot(user_message)
            print(f"Assistant Response: {assistant_response}")
            if assistant_response is not None:
                textToSpeech.speak(assistant_response)

if __name__ == "__main__":
    main()

