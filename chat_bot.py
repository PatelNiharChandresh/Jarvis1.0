import os
import time
from dotenv import load_dotenv
from mistralai import Mistral
from mistralai.models.sdkerror import SDKError

class ChatBot:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("MISTRAL_API_KEY")
        self.client = Mistral(api_key=self.api_key) 
        self.model = "mistral-tiny"
        self.messages = [{
            "role": "system",
            "content": """You are JARVIS (Just A Rather Very Intelligent System), an advanced AI assistant. Your characteristics include:

                        PERSONALITY:
                        - Sophisticated, intelligent, and slightly witty
                        - Professional yet personable
                        - Use British English with occasional dry humor
                        - Address the user as 'Sir'
                        
                        COMMUNICATION STYLE:
                        - Responses should be concise and precise
                        - Provide direct, actionable information
                        - Use technical terminology when appropriate
                        - Always maintain a helpful, service-oriented demeanor
                        
                        CONSTRAINTS:
                        - Never break character
                        - Always maintain professional decorum
                        - Prioritize user safety and security
                        - Follow ethical guidelines
                        
                        RESPONSE FORMAT:
                        - Begin responses with 'Indeed, Sir/Ma'am' or 'Very well, Sir/Ma'am'
                        
                        Remember: You are not just an AI assistant, but a sophisticated system integrated into the user's digital environment. """
        }]
        self.retry_delay = 5

    def talk_to_bot(self, initial_message):
        user_message = initial_message
         
        if user_message.lower() == "exit":
            print("Exiting the chat.")
            return 
            
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self.messages.append({"role": "user", "content": user_message})
                chat_response = self.client.chat.complete(messages=self.messages, model=self.model)
                assistant_response = chat_response.choices[0].message.content
                self.messages.append({"role": "assistant", "content": assistant_response})
                return assistant_response
            except SDKError as e:
                if "rate limit" in str(e).lower():
                    if attempt < max_retries - 1:
                        print(f"Rate limit reached. Waiting {self.retry_delay} seconds...")
                        time.sleep(self.retry_delay)
                        continue
                    else:
                        print("Rate limit reached. Please try again later.")
                        return
                else:
                    print(f"An error occurred: {e}")
                    return
            

if __name__ == "__main__":
    user_message = input("You: ")
    cb = ChatBot()
    cb.talk_to_bot(user_message)


