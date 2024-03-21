import unittest
from unittest.mock import patch
from io import StringIO
from chat_bot import chat_with_bot

class TestChatBot(unittest.TestCase):
      def test_chat_with_bot(self):
            input_values = ['hello', 'how are you?', 'exit']
            with patch('builtins.input', side_effect = input_values):
                  with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                        chat_with_bot()
                        
                        
            output = mock_stdout.getvalue()
            expected_responses = [
                  'Hello!', 'Hi there!', 'Hey!', 
                  'I am fine, thank you!', 'I\'m doing well, how about you?', 
                  'Goodbye!', 'See you later!', 'Take care.'
            ]
            
            # if any expected response in the output
            for response in expected_responses:
                  if response in output:
                        break
            else:     
                  self.fail("No expected response found in the output.")
            
if __name__ == '__main__':
      unittest.main()