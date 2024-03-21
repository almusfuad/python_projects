import nltk
from nltk.chat.util import Chat, reflections

# patterns and responses for the chat
pairs= [
      (r'hi|hello|hey', ['Hello', 'Hi there!', 'Hey!']),
      (r'how are you?', ['I am fine, thank you!', 'I\'m doing well, how about you?']),
      (r'i\'m (.*)', ['Nice to hear you that']),
      (r'(.*) your name?', ['I am KothaBot. Develop by Fuad.']),
      (r'(.*)(bad|not (well|good))', ['I\'m sorry to hear that.']),
      (r'(.*) (good|fine|well)', ['That\'s great!','Good to hear you!']),
      (r'quit', ['Bye!', 'Goodbye!', 'Take care.', 'Bye!']),
]

# create chat
chat = Chat(pairs, reflections)

def chat_with_bot():
      if not nltk.data.find("corpora/ycoe.zip"):
            nltk.download('all')
      print("Welcome to KothaBot. Let's chat! Type 'quit' to exit.")
      while True:
            user_input = input('You: ')
            response = chat.respond(user_input)
            
            # check for available response
            if response:
                  print('Bot:', response)
            else:
                  print('Bot: Sorry, I can\'t respond correctly. I am under development.')
                  
                  
            if user_input.lower() == 'quit':
                  break
            
if __name__ == '__main__':
      chat_with_bot()
