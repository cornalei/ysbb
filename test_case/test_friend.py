#加好友
from common.myunit import StartEnd
from businessView.friend import Friend
import unittest
import logging

class TestFriend(StartEnd):
    # @unittest.skip('test_friends')
    def test_friends(self):
        logging.info('======test_friends=====')
        f = Friend(self.driver)
        try:
            self.assertTrue(f.friends())
        except BaseException as error:
            self.add_img()
            raise error

    # @unittest.skip('test_friends')
    def test_newfriend(self):
        logging.info('======test_newfriend=====')
        f = Friend(self.driver)
        try:
            self.assertTrue(f.newfriend('虫虫'))
        except BaseException as error:
            self.add_img()
            raise error

    # @unittest.skip('test_thirdfriend')
    def test_thirdfriend(self):
        logging.info('======test_thirdfriend=====')
        f = Friend(self.driver)
        try:
            self.assertTrue(f.thirdfriend())
        except BaseException as error:
            self.add_img()
            raise error


if __name__ == '__main__':
    unittest.main()