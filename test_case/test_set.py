#验证码和关于一说宝宝
from common.myunit import StartEnd
from businessView.set import Set
import unittest
import logging

class TestSet(StartEnd):
    # @unittest.skip('test_sets')
    def test_sets(self):
        logging.info('======test_sets=====')
        s = Set(self.driver)
        self.assertTrue(s.sets())



if __name__ == '__main__':
    unittest.main()