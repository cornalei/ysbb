import logging
from common.common_fun import Common,NoSuchElementException,time,TimeoutException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class Recommended(Common):
    hotuserhead = (By.ID, 'com.clickcoo.yishuobaobao:id/ciriv_hotuserhead')  # 儿童故事
    mybuyalbum = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_mybuyalbum')  # 故事列表
    playaudio = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_playaudio')  # 声音播放按钮

    find_more = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_find_more')  # 更多
    album_item = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_album_item')  # 专辑列表

    anchor_follow = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_anchor_follow')  #关注
    anchor_pic = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_anchor_pic')  #主播头像
    album = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_album')  #主页专辑

    loadpic = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_loadpic')  #banner图

    # def banner(self):
    #     self.driver.find_element(*self.loadpic).click()
    #     return True

    def story(self):
        logging.info('===播放儿童故事===')
        self.driver.find_elements(*self.hotuserhead)[1].click()
        try:
            self.waits(2,self.mybuyalbum)[1].click()
        except TimeoutException:
            logging.error('儿童故事数据加载失败！')
            self.getScreenShot('儿童故事数据加载失败！')
            return False
        else:
            self.driver.find_elements(*self.playaudio)[0].click()
            return True

    def check(self):
        logging.info('===推荐界面检查===')
        self.swipeUp()
        time.sleep(0.5)
        self.swipeUp()
        self.waits(2,self.find_more)[0].click()
        try:
            self.waits(1,self.album_item)[0].click()
        except TimeoutException:
            logging.error('专辑数据加载失败！')
            self.getScreenShot('专辑数据加载失败！')
            return False
        else:
            self.driver.find_elements(*self.playaudio)[0].click()
            return True

    def focus(self):
        logging.info('===关注主播===')
        self.waits(1,self.anchor_follow)[0].click()
        self.swipeLeft()
        self.driver.find_elements(*self.anchor_follow)[0].click()
        self.driver.find_elements(*self.anchor_pic)[0].click()
        try:
            self.driver.find_element(*self.album).click()
        except NoSuchElementException:
            logging.error('主页数据加载失败！')
            self.getScreenShot('主页数据加载失败！')
            return False
        else:
            return True

if __name__ == '__main__':
    driver=appium_desired()
    r=Recommended(driver)

    # r.banner()
    # r.story()
    # r.focus()
    r.check()