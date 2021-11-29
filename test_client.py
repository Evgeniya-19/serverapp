import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_presence, process_ans


class TestClass(unittest.TestCase):
    dict_1 = {

    }

    def test_create_presence_isnotnone(self):
        self.assertIsNotNone(create_presence('Name')[USER][ACCOUNT_NAME], True)

    def test_create_presence(self):
        self.assertEqual(create_presence('Name')[USER][ACCOUNT_NAME], 'Name')





if __name__ == '__main__':
    unittest.main()