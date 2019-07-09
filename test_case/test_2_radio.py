from common.myunit import StartEnd
from businessView.radioStation import RadioStation
import unittest
import logging

class TestRadio(StartEnd):
    # @unittest.skip('test_radio')
    def test_radio(self):
        logging.info('======test_radio=====')
        r = RadioStation(self.driver)

        try:
            if self.assertTrue(r.radio_play()) is AssertionError:
                logging.error('radio_play fail!')
            else:
                self.assertTrue(r.check_radio_play())
        except BaseException as error:
            self.getScreenShot()
            raise error

if __name__ == '__main__':
    unittest.main()