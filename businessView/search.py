import logging
from common.common_fun import Common,TimeoutException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class Search(Common):
    bn_search = (By.ID, 'com.clickcoo.yishuobaobao:id/ibn_serach')  #搜索按钮
    et_serachkey = (By.ID, 'com.clickcoo.yishuobaobao:id/et_serachkey')  #搜索输入框
    btn_searchstart = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_searchstart')  #搜索
    heartstation_play = (By.ID, 'com.clickcoo.yishuobaobao:id/cb_heartstation_play')  #播放
    btn_searchusers = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_searchusers')  #用户
    userlayout = (By.ID, 'com.clickcoo.yishuobaobao:id/layout_userlayout')  #用户列表
    btn_searchalbum = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_searchalbum')  #专辑
    albumlayout = (By.ID, 'com.clickcoo.yishuobaobao:id/layout_albumlayout')  #专辑列表

    def search_action(self,keyword):
        logging.info('===搜索====')
        self.driver.find_element(*self.bn_search).click()
        self.wait(2,self.et_serachkey).send_keys(keyword)
        self.wait(1,self.btn_searchstart).click()

    def check_voice(self):
         logging.info('====check search_voice======')
         try:
             self.waits(8,self.heartstation_play)[0].click()
         except TimeoutException:
             logging.error('搜索声音失败！')
             self.getScreenShot('搜索声音失败！')
             return False
         else:
             logging.info('搜索声音成功')
             return True


    def check_user(self):
        self.wait(1,self.btn_searchusers).click()
        logging.info('====check search_user======')
        try:
            self.waits(3,self.userlayout)[0]
        except  TimeoutException:
            logging.error('搜索用户失败！')
            self.getScreenShot('搜索用户失败！')
            return False
        else:
            logging.info('搜索用户成功')
            return True


    def check_album(self):
        self.driver.find_element(*self.btn_searchalbum).click()
        logging.info('====check search_album======')
        try:
            self.waits(3,self.albumlayout)[0]
        except  TimeoutException:
            logging.error('搜索专辑失败！')
            self.getScreenShot('搜索专辑失败！')
            return False
        else:
            logging.info('搜索专辑成功')
            return True



if __name__ == '__main__':
    driver=appium_desired()
    s=Search(driver)
    s.search_action('a')
    s.check_voice()
    s.check_user()
    s.check_album()





