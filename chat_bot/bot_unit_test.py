import unittest
from unittest.mock import patch
from io import StringIO
from chat_bot import chat_with_bot

class TestChatBot(unittest.TestCase):
      
      # use the console input and output for test
      @patch('builtins.input', side_effect = ['hello', 'quit'])
      @patch('sys.stdout', new_callable=StringIO)
      
      def test_chat_with_bot(self, mock_stdout, mock_input):
            expected_output = (
                  "Welcome to KothaBot. Let's chat! Type 'quit' to exit.\n"
                  "You: hello\n"
                  "Bot: Hello\n"
                  "You: quit\n"
                  "Bot: Bye!\n"
            )
            
            chat_with_bot()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            
if __name__ == '__main__':
      unittest.main()