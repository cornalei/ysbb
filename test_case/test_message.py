#消息
from common.myunit import StartEnd
from businessView.message import Message
import unittest
import logging

class TestMessage(StartEnd):
    # @unittest.skip('test_delete_message')
    def test_delete_message(self):
        logging.info('======test_delete_message=====')
        m = Message(self.driver)
        try:
            self.assertTrue(m.delete_message())
        except BaseException as error:
            self.add_img()
            raise error



if __name__ == '__main__':
    unittest.main()