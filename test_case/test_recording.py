#录音
from common.myunit import StartEnd
from businessView.recording import Recording
import unittest
import logging
import random

class TestRecording(StartEnd):
    # @unittest.skip('test_recording')
    def test_recording(self):
        logging.info('======test_recording=====')
        title = '小仙女' + str(random.randint(0, 1000))
        describe = '这是小仙女的声音：' + str(random.randint(0, 10000))

        r = Recording(self.driver, describe, title)
        r.recording()
        self.assertTrue(r.check_recording())

    # @unittest.skip('test_upload_voice')
    def test_upload_voice(self):
        logging.info('======test_upload_voice=====')
        title = '小仙女' + str(random.randint(0, 1000))
        describe = '这是小仙女的声音：' + str(random.randint(0, 10000))
        r = Recording(self.driver, describe, title)
        r.upload_voice()
        self.assertTrue(r.check_upload_voice())



if __name__ == '__main__':
    unittest.main()