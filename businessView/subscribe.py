import logging
from common.common_fun import Common,time,TimeoutException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class Subscribe(Common):
    trends = (By.ID, 'com.clickcoo.yishuobaobao:id/lv_trends')  #动态按钮
    home_subscribe = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_home_subscribe')  # 订阅
    subscriptionName = (By.ID, 'com.clickcoo.yishuobaobao:id/subscriptionName')  # 我的订阅专辑名
    playaudio = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_playaudio')  # 声音播放按钮
    voice_name = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_voice_name')  # 声音名
    playerrevolve = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_playerrevolve')  # 播放器
    audiorecommend = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_audiorecommend')  # 播放声音名

    subscriptionJoin = (By.ID, "com.clickcoo.yishuobaobao:id/btnsubscriptionJoinRecommended")  # 大家都在听-订阅
    nameRecommended = (By.ID, "com.clickcoo.yishuobaobao:id/subscriptionNameRecommended")  # 大家都在听-专辑名

    find_more = (By.XPATH, "//android.widget.TextView[contains(@text,'寻找更多')]")  # 寻找更多
    album_item = (By.ID, "com.clickcoo.yishuobaobao:id/iv_album_item")  # 热门专辑


    def subscribe(self):
        logging.info('===订阅大家都在听====')
        self.driver.find_element(*self.trends).click()
        self.driver.find_element(*self.home_subscribe).click()
        time.sleep(0.5)
        self.swipeUps(*self.subscriptionJoin)

    def check_subscribe(self):
        text1=self.waits(1,self.nameRecommended)[0].text
        logging.info('专辑：%s' %text1)
        self.driver.find_elements(*self.subscriptionJoin)[0].click()
        time.sleep(3)
        try:
            text2 = self.waits(5,self.nameRecommended)[0].text
        except TimeoutException:
            logging.error('subscribe fail!')
            self.getScreenShot('subscribe fail!')
            return False
        else:
            logging.info('专辑：%s' % text2)
            if text2 == text1:
                logging.error('subscribe fail!')
                self.getScreenShot('subscribe fail!')
                return False
            else:
                logging.info('subscribe success!')
                return True


    def subscribe_play(self):
        logging.info('===播放我的订阅中专辑声音====')
        self.driver.find_element(*self.trends).click()
        self.wait(1,self.home_subscribe).click()
        self.driver.find_elements(*self.subscriptionName)[0].click()



    def check_subscribe_play(self):
        logging.info('===检查播放专辑声音====')
        text1=self.waits(1,self.voice_name)[0].text
        logging.info('点播: %s' %text1)
        self.driver.find_elements(*self.playaudio)[0].click()
        self.wait(1,self.playerrevolve).click()
        text2 = self.driver.find_element(*self.audiorecommend).text
        logging.info('播放: %s' %text2)
        a=self.string_similar(text1,text2)
        # print(a)
        if a >= 0.85:
            logging.info('subscribe_play success!')
            return True
        else:
            logging.error('subscribe_play fail!')
            self.getScreenShot('subscribe_play fail!')
            return False

    def subscribes_play(self):
        logging.info('===播放大家都在听中专辑声音====')
        self.driver.find_element(*self.trends).click()
        self.check_radio()
        self.driver.find_element(*self.home_subscribe).click()
        time.sleep(2)
        self.swipeUp_s(*self.find_more)
        try:
            self.waits(2,self.album_item)[0].click()
        except TimeoutException:
            logging.error('大家都在听专辑数据加载失败！')
            self.getScreenShot('subscribes专辑数据加载失败！')
            return False
        else:
            logging.info('大家都在听专辑数据加载成功！')













if __name__ == '__main__':
    driver = appium_desired()
    s = Subscribe(driver)

    # s.subscribes_play()
    # s.check_subscribe_play()

    s.subscribe()
    s.check_subscribe()

    # s.subscribe_play()
    # s.check_subscribe_play()

