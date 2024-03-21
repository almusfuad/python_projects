import nltk
from nltk.chat.util import Chat, reflections

# patterns and responses for the chat
pairs= [
      (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
      (r'how are you?', ['I am fine, thank you!', 'I\'m doing well, how about you?']),
      (r'what is your name?', ['I am a simple chatbot.', 'You can call me KothaBot']),
      (r'(.*)(bad|not (well|good))', ['I\'m sorry to hear that.', 'Oh no! what happened?']),
      (r'(.*) (good|fine|well)', ['That\'s good to hear you!', 'Awesome!', 'Glad to hear that.']),
      (r'bye|quit|exit', ['Goodbye!', 'See you later!', 'Take care.']),
]

# create chat
chat = Chat(pairs, reflections)

def chat_with_bot(input_function = input):
      print("Welcome to KothaBot. Let's chat! Type 'exit' to exit.")
      while True:
            user_input = input('You: ')
            response = chat.respond(user_input)
            
            # check for available response
            if response:
                  print('Bot:', response)
            else:
                  print('Bot: Sorry, I can\'t respond correctly. I am under development.')
                  
                  
            if user_input.lower() in ['bye', 'quit', 'exit']:
                  break
            
if __name__ == '__main__':
      nltk.download('punkt')
      chat_with_bot()
