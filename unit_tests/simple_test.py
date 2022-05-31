import sys
import os
import unittest
import json
from common.data_values import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, DEFAULT_ENCODING
from common.data_function import get_message, send_message

sys.path.insert(0, os.path.join(os.getcwd(), '..'))


class TestSocket:

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):

        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode(DEFAULT_ENCODING)
        self.received_message = message_to_send

    def recv(self, max_len):

        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(DEFAULT_ENCODING)

class TestUtils(unittest.TestCase):

    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 111111.111111,
        USER: {
            ACCOUNT_NAME: 'test_test'
        }
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_err = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_send_message_true(self):

        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    def test_send_message_with_error(self):

        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertRaises(TypeError, send_message, test_socket, "wrong_dictionary")

    def test_get_message_ok(self):

        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        self.assertEqual(get_message(test_sock_ok), self.test_dict_recv_ok)

    def test_get_message_error(self):
        test_sock_err = TestSocket(self.test_dict_recv_err)
        self.assertEqual(get_message(test_sock_err), self.test_dict_recv_err)


if __name__ == '__main__':
    unittest.main()
