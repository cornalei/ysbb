import unittest,time,os
from common.desired_caps_l import appium_desired
import logging

class StartEnd(unittest.TestCase):
    def getScreenShot(self):
        timestrmap=time.strftime("%Y%m%d-%H.%M.%S")
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s.png' %timestrmap
        self.driver.get_screenshot_as_file(image_file)
        print('screenshot:',timestrmap,'.png')

    def setUp(self):
        logging.info('=====setUp====')
        self.driver=appium_desired()

    def tearDown(self):
        logging.info('====tearDown====')
        self.driver.close_app()