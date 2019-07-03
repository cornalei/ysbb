#精装
from common.myunit import StartEnd
from businessView.hardcover import Hardcover
import unittest
import logging

class TestHardcover(StartEnd):
    # @unittest.skip('test_todayrecomend')
    def test_todayrecomend(self):
        logging.info('======test_todayrecomend=====')
        h = Hardcover(self.driver)
        self.assertTrue(h.todayrecomend())

    # @unittest.skip('test_heavyfine')
    def test_heavyfine(self):
        logging.info('======test_heavyfine=====')
        h = Hardcover(self.driver)
        self.assertTrue(h.heavyfine())

    # @unittest.skip('test_newalbum')
    def test_newalbum(self):
        logging.info('======test_newalbum=====')
        h = Hardcover(self.driver)
        self.assertTrue(h.newalbum())

    # @unittest.skip('test_buyalbums')
    def test_buyalbums(self):
        logging.info('======test_buyalbums=====')
        h = Hardcover(self.driver)
        self.assertTrue(h.buyalbums())

if __name__ == '__main__':
    unittest.main()