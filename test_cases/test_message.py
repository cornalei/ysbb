#消息
from commons.multi_devices import devices_start_sync
from businessViews.message import multi_message
import unittest
import logging

class TestMessage(unittest.TestCase):
    # @unittest.skip('test_multi_message')
    def test_multi_message(self):
        logging.info('======test_multi_message=====')
        devices_start_sync(multi_message)


if __name__ == '__main__':
    unittest.main()