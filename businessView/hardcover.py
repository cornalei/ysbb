import logging,time
from common.common_fun import Common,TimeoutException,TimeoutException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class Hardcover(Common):
    textviewHardcover = (By.ID, 'com.clickcoo.yishuobaobao:id/textviewHardcover')  # 精装
    buyalbum = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_hardcover_buyalbum')  # 我的已购专辑
    share_album = (By.ID, 'com.clickcoo.yishuobaobao:id/layout_share_album')  # 我的已购专辑
    wishlist = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_hardcover_wishlist')  # 我的心愿单
    wishlist_title = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_wishlist_title')  # 我的心愿单

    todayRecommendmore = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_hardcover_todayRecommendmore')  # 今日特推-更多
    todayrecomend_desc = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_todayrecomend_desc')  # 今日特推-专辑名称
    mybuyalbum = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_mybuyalbum')  # 专辑列表
    mybuyalbum_title = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_mybuyalbum_title')  # 专辑列表-专辑名称
    tv_album_name = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_album_name')  # 详情-专辑名称

    heavyfine_desc = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_heavyfine_desc')  # 重磅精品-专辑名称
    heavyfinemore = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_hardcover_heavyfinemore')  # 重磅精品-更多
    textview_audio = (By.ID, 'com.clickcoo.yishuobaobao:id/textview_audio')  # 声音
    album_voice = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_album_voice')  # 声音列表

    newarrivalmore = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_hardcover_newarrivalmore')  # 最新上架-更多

    add_wish = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_add_wish')  # +加入心愿单
    wish = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_wish')  # 心愿单
    buy = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_buy')  # 立即购买


#今日特推
    def todayrecomend(self):
        logging.info('===今日特推===')
        self.find_element(self.textviewHardcover).click()
        text1=self.find_elements(self.todayrecomend_desc)[0].text
        self.find_element(self.todayRecommendmore).click()
        try:
            self.waits(1,self.mybuyalbum_title)[0].click()
        except TimeoutException:
            logging.error('精装数据加载失败！')
            self.getScreenShot('精装数据加载失败！')
            return False
        else:
            text2 = self.find_element(self.tv_album_name).text
            if text1==text2:
                logging.info('今日特推专辑正确')
                return True
            else:
                logging.error('今日特推专辑有误！')
                self.getScreenShot('今日特推专辑有误！')
                return False
#重磅精品
    def heavyfine(self):
        self.find_element(self.textviewHardcover).click()
        time.sleep(0.5)
        logging.info('===重磅精品+声音===')
        self.swipeUp()
        time.sleep(0.5)
        self.find_elements(self.heavyfine_desc)[0].click()
        self.find_element(self.textview_audio).click()
        try:
            self.find_elements(self.album_voice)[0].click()
        except TimeoutException:
            logging.error('精装声音数据加载失败！')
            self.getScreenShot('精装声音数据加载失败！')
            return False
        else:
            logging.info('重磅精品正确')
            return True

    def newalbum(self):
        self.find_element(self.textviewHardcover).click()
        time.sleep(0.5)
        self.swipeUp()
        logging.info('===最新上架+加入心愿单===')
        self.wait(1,self.newarrivalmore).click()
        try:
            self.find_elements(self.mybuyalbum_title)[0].click()
        except TimeoutException:
            logging.error('详情页加载失败！')
            self.getScreenShot('详情页加载失败！')
            return False
        else:
            self.find_element(self.add_wish).click()
            text1=self.find_element(self.tv_album_name).text
            self.find_element(self.wish).click()
            self.swipeUp_ss(self.wishlist_title)
            text2=self.find_element(self.tv_album_name).text
            if text1 == text2:
                logging.info('加入心愿单成功')
                return True
            else:
                logging.error('加入心愿单失败！')
                self.getScreenShot('add wish fail！')
                return False

    def buyalbums(self):
        self.find_element(self.textviewHardcover).click()
        logging.info('===我的已购专辑===')
        self.find_element(self.buyalbum).click()
        self.find_elements(self.mybuyalbum)[0].click()
        try:
            self.find_element(self.share_album)
        except TimeoutException:
            logging.error('已购专辑加载失败！')
            self.getScreenShot('已购专辑加载失败！')
            return False
        else:
            logging.info('已购专辑加载成功')
            return True



if __name__ == '__main__':
    driver=appium_desired()
    h=Hardcover(driver)
    # h.todayrecomend()
    # h.heavyfine()
    h.newalbum()
    # h.buyalbums()