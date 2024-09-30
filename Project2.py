import re
import random

# Define a list of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you ?', ['I am fine, thank you!', 'I am doing well. How about you?']),
    (r'(.*) your name ?', ['My name is ChatBot!', 'You can call me ChatBot.']),
    (r'(.*) (created|made) you ?', ['I was created by a Python enthusiast.']),
    (r'(.*) (help|support)', ['How can I assist you?', 'What do you need help with?']),
    (r'exit|bye', ['Goodbye!', 'See you soon!']),
]

# Function to match user input with a response
def chatbot_response(user_input):
    for pattern, responses in pairs:
        match = re.match(pattern, user_input.lower())
        if match:
            return random.choice(responses)
    return "Sorry, I don't understand that."

# Main loop to interact with the chatbot
def chat():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input('You: ')
        if user_input.lower() in ['exit', 'bye']:
            print("ChatBot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat()
pip install chatterbot chatterbot_corpus
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new ChatBot instance
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the English corpus
trainer.train('chatterbot.corpus.english')

# Function to chat with the bot
def chat_with_bot():
    print("Chat with me! Type 'bye' to exit.")
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat_with_bot()
