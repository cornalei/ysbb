import logging
from common.common_fun import Common,NoSuchElementException,time
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
class RadioStation(Common):
    trends = (By.ID, 'com.clickcoo.yishuobaobao:id/lv_trends')  #动态按钮
    paly_state = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_paly_state')  #电台—播放按钮
    voice_play = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_voice_play')  #电台—播放按钮
    voice_title = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_voice_title')  #电台—声音名称
    playerrevolve = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_playerrevolve')  #播放器
    audiorecommend = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_audiorecommend')  # 播放声音名

    def radio_play(self):
        logging.info('===动态-电台====')
        self.driver.find_element(*self.trends).click()
        self.check_radio()
        self.swipeUp()
        time.sleep(1)
        try:
            self.driver.find_elements(*self.paly_state)[0].click()
            return True
        except IndexError:
            try:
                self.driver.find_elements(*self.voice_play)[0].click()
                return True
            except IndexError:
                logging.error('radio_play fail!')
                self.getScreenShot('radio_play fail!')
                return False


    def check_radio_play(self):
        logging.info('====check_radio_play======')
        text1 = self.waits(1,self.voice_title)[0].text
        logging.info('点播: %s' % text1)
        self.driver.find_element(*self.playerrevolve).click()
        try:
            text2 = self.driver.find_element(*self.audiorecommend).text
        except NoSuchElementException:
            logging.error('radio_play fail!')
            self.getScreenShot('radio_play fail!')
            return False
        else:
            logging.info('播放: %s' % text2)
            return True
            # a = self.string_similar(text1, text2)
            # if a >= 0.85:
            #     logging.info('radio_play success!')
            #     return True
            # else:
            #     logging.error('radio_play fail!')
            #     self.getScreenShot('radio_play fail!')
            #     return False




if __name__ == '__main__':
    driver=appium_desired()
    r=RadioStation(driver)
    if r.radio_play() is False:
        logging.error('radio_play fail!')
    else:
        r.check_radio_play()