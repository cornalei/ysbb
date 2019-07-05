from baseView.baseView import BaseView
from selenium.webdriver.support.ui import WebDriverWait
from common.desired_caps_l import appium_desired
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import logging
from selenium.webdriver.common.by import By
import time,os
import csv
import difflib

class Common(BaseView):
    tiaoguo = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_startgoto')#跳过按钮
    baobao = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_baobao')#一说宝宝引导
    coupon = (By.ID, 'com.clickcoo.yishuobaobao:id/roundimageview')#优惠券
    iv_close = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_close')#关闭优惠券
    tip_commit = (By.ID, 'android:id/button1')  # 登出提醒-确定
    friend_trends = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_friend_trends')  # 电台引导

    # def check_Tiaoguo(self):
    #     logging.info('==跳过按钮==')
    #     try:
    #         tiaoguo = self.driver.find_element(*self.tiaoguo)
    #     except NoSuchElementException:
    #         logging.info('==没有跳过按钮==')
    #     else:
    #         tiaoguo.click()
    #         time.sleep(2)

    def check_Baobao(self):
        logging.info('==一说宝宝引导==')
        try:
            baobao = self.driver.find_element(*self.baobao)
        except NoSuchElementException:
            logging.info('==没有一说宝宝引导==')
        else:
            baobao.click()
            time.sleep(2)

    def check_radio(self):
        logging.info('===电台引导===')
        try:
            radio = self.driver.find_element(*self.friend_trends)
        except NoSuchElementException:
            logging.info('==没有电台引导==')
        else:
            radio.click()
            time.sleep(0.5)

    #相似度
    def string_similar(self,s1,s2):
        return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def swipeRight(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.1)
        x2 = int(l[0] * 0.9)
        self.swipe(x1, y1, x2, y1, 1000)

    def swipeDown(self):
        logging.info('swipeDown')
        l = self.get_size()
        x1 = int(l[0] * 0.2)
        y1 = int(l[1] * 0.2)
        y2 = int(l[1] * 0.9)
        self.swipe(x1, y1, x1, y2, 1000)

    def swipeUp(self):
        logging.info('swipeUp')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.9)
        y2 = int(l[1] * 0.1)
        self.swipe(x1, y1, x1, y2, 1000)
        time.sleep(1)

    def swipeUp_l(self):
        logging.info('swipeUp')
        l = self.get_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.9)
        y2 = int(l[1] * 0.5)
        self.swipe(x1, y1, x1, y2, 1000)
        time.sleep(0.5)

    def swipeUp_s(self,*element):
        i = 0
        while i < 10:
            try:
                self.driver.find_element(*element).click()
                break
            except:
                self.swipeUp_l()
                i = i + 1
                if i<10:
                    continue
                else:
                    raise NoSuchElementException


    def swipeUp_ss(self,*element):
        i = 0
        while i < 10:
            try:
                self.driver.find_elements(*element)[0].click()
                break
            except:
                self.swipeUp_l()
                i = i + 1
                if i < 10:
                    continue
                else:
                    raise IndexError

    def swipeUps(self,*element):
        i = 0
        while i < 10:
            try:
                a=self.driver.find_elements(*element)[0]
                break
            except:
                self.swipeUp()
                i = i + 1
                if i < 10:
                    continue
                else:
                    raise IndexError

    def swipeLeft2(self):
        for i in range(2):
            self.swipeLeft()
            time.sleep(1)
        time.sleep(4)

    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,module):
        # time=self.getTime()
        timestrmap=time.strftime('%Y%m%d-%H.%M.%S')
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s%s.png' %(module,timestrmap)
        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)
        print('screenshot:',module,timestrmap,'.png')

    def check_coupon(self):
        logging.info('====检查优惠券====')
        try:
            element=self.driver.find_element(*self.coupon)
        except NoSuchElementException:
            logging.info('===没有优惠券===')
        else:
            element.click()
            self.driver.find_element(*self.iv_close).click()
            time.sleep(2)

    # def check_account_alert(self):
    #     #检测是否有账号被挤下的登出提醒
    #     logging.info('=====check_account_alert====')
    #     try:
    #         element=self.driver.find_element(*self.tip_commit)
    #     except NoSuchElementException:
    #         pass
    #     else:
    #         logging.info('close tip_commit')
    #         element.click()

    def get_csv_data(self,csv_file,line):
        logging.info('=====get_csv_data======')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row


if __name__ == '__main__':
    driver=appium_desired()
    com=Common(driver)
    # com.swipeLeft2()
    # com.getScreenShot('startApp')
    # com.check_Tiaoguo()
    # com.check_Baobao()

    # list = ["这", "是", "一个", "测试", "数据"]
    # # for i in range(len(list)):
    #     # print(i, list[i])
    #
    # list1 = ["这", "是", "一个", "测试", "数据"]
    # for index, item in enumerate(list1):
    #     print(index, item)
    csv_file = '../data/account.csv'
    data = com.get_csv_data(csv_file,1)
    print(data)




