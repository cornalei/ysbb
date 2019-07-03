#播放器
from common.myunit import StartEnd
from businessView.player import Player
import unittest,logging,random

class TestPlayer(StartEnd):

    # @unittest.skip('test_forwarding_story')
    def test_forwarding(self):
        p = Player(self.driver)
        self.assertTrue(p.forwarding())

    # @unittest.skip('test_play_collection')
    def test_play_collection(self):
        p = Player(self.driver)
        self.assertTrue(p.check_collection())

    # @unittest.skip('test_play_comments')
    def test_play_comments(self):
        p = Player(self.driver)
        p.comments()
        self.assertTrue(p.check_comments())

    # @unittest.skip('test_play_check')
    def test_play_check(self):
        logging.info('===举报、下载、分享')
        p = Player(self.driver)
        self.assertTrue(p.play_check())





if __name__ == '__main__':
    unittest.main()