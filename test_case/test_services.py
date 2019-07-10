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
        try:
            self.assertTrue(s.free())
        except BaseException as error:
            self.add_img()
            raise error

    # @unittest.skip('test_advice')
    def test_advice(self):
        logging.info('======test意见反馈=====')
        s = Services(self.driver)
        try:
            self.assertTrue(s.advice())
        except BaseException as error:
            self.add_img()
            raise error



if __name__ == '__main__':
    unittest.main()