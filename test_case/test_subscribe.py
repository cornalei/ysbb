from common.myunit import StartEnd
from businessView.subscribe import Subscribe
import unittest
import logging

class TestSubscribe(StartEnd):
    #播放大家都在听中专辑声音
    # @unittest.skip('test_subscribes_play')
    def test_1subscribes_play(self):
        logging.info('======test_subscribes_play=====')
        s = Subscribe(self.driver)
        try:
            s.subscribes_play()
            self.assertTrue(s.check_subscribe_play())
        except BaseException as error:
            self.getScreenShot()
            raise error

    #订阅大家都在听
    # @unittest.skip('test_subscribe')
    def test_2subscribe(self):
        logging.info('======test_subscribe=====')
        s = Subscribe(self.driver)
        try:
            s.subscribe()
            self.assertTrue(s.check_subscribe())
        except BaseException as error:
            self.getScreenShot()
            raise error

    # 播放我的订阅中专辑声音
    # @unittest.skip('test_subscribes_play')
    def test_3subscribe_play(self):
        logging.info('======test_subscribe_play=====')
        s = Subscribe(self.driver)
        try:
            s.subscribe_play()
            self.assertTrue(s.check_subscribe_play())
        except BaseException as error:
            self.getScreenShot()
            raise error










if __name__ == '__main__':
    unittest.main()