#播放器
from common.myunit import StartEnd
from businessView.player import Player
import unittest,logging

class TestPlayer(StartEnd):

    # @unittest.skip('test_forwarding_story')
    def test_forwarding(self):
        p = Player(self.driver)
        try:
            self.assertTrue(p.forwarding())
        except BaseException as error:
            self.add_img()
            raise error

    # @unittest.skip('test_play_collection')
    def test_play_collection(self):
        p = Player(self.driver)
        try:
            self.assertTrue(p.check_collection())
        except BaseException as error:
            self.add_img()
            raise error

    # @unittest.skip('test_play_comments')
    def test_play_comments(self):
        p = Player(self.driver)
        try:
            p.comments()
            self.assertTrue(p.check_comments())
        except BaseException as error:
            self.add_img()
            raise error

    # @unittest.skip('test_play_check')
    def test_play_check(self):
        logging.info('===举报、分享')
        p = Player(self.driver)
        try:
            self.assertTrue(p.play_check())
        except BaseException as error:
            self.add_img()
            raise error






if __name__ == '__main__':
    unittest.main()