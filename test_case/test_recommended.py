#发现-推荐
from common.myunit import StartEnd
from businessView.recommended import Recommended
import unittest,logging,random

class TestRecommended(StartEnd):

    # @unittest.skip('test_banner')
    # def test_banner(self):
    #     logging.info('======发现-推荐banner=====')
    #     r = Recommended(self.driver)
    #     self.assertTrue(r.banner())

    # @unittest.skip('test_story')
    def test_1story(self):
        r = Recommended(self.driver)
        self.assertTrue(r.story())

    # @unittest.skip('test_check')
    def test_check(self):
        r = Recommended(self.driver)
        self.assertTrue(r.check())

    # @unittest.skip('test_focus')
    def test_focus(self):
        r = Recommended(self.driver)
        self.assertTrue(r.focus())



if __name__ == '__main__':
    unittest.main()