#个人服务
from common.myunit import StartEnd
from businessView.services import Services
import unittest
import logging

class TestServicese(StartEnd):

    # @unittest.skip('test_free')
    def test_free(self):
        logging.info('======test免流量收听=====')
        s = Services(self.driver)
        self.assertTrue(s.free())

    # @unittest.skip('test_advice')
    def test_advice(self):
        logging.info('======test意见反馈=====')
        s = Services(self.driver)
        self.assertTrue(s.advice())



if __name__ == '__main__':
    unittest.main()