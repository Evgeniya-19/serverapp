import socket
import sys
import json
import unittest
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, RESPONDEFAULT_IP_ADDRESSSE
from common.utils import get_message, send_message


class TestClass(unittest.TestCase):

    def test_process_client_message_isnotnone(self):
        self.assertIsNotNone(process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Name'}}), True)

    def test_process_client_message_assertIsNone(self):
        self.assertIsNone(process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Name'}}), False)

    def test_process_client_message_assertTrue(self):
        self.assertTrue({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Name'}}, True)




if __name__ == '__main__':
    unittest.main()