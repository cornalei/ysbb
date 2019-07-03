import logging
from common.common_fun import Common,TimeoutException
from common.desired_caps_l import appium_desired
from selenium.webdriver.common.by import By

class WechatLogin(Common):
    tiaoguo = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_startgoto')  # 跳过按钮
    btn_wechatlogin = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_wechatlogin')  # 微信登录

    button_myself=(By.ID,'com.clickcoo.yishuobaobao:id/lv_mine')#我的
    button_visitor=(By.ID,'com.clickcoo.yishuobaobao:id/tv_visitor')#登录
    username=(By.ID,'com.clickcoo.yishuobaobao:id/tv_user_name')#昵称

    setButton=(By.ID,'com.clickcoo.yishuobaobao:id/iv_setting')#设置
    logoutBtn=(By.ID,'com.clickcoo.yishuobaobao:id/layout_logoutlogin')#退出登录


    def login_action(self):
        self.swipeLeft2()
        self.wait(1,self.tiaoguo).click()
        self.check_Baobao()
        self.check_coupon()
        self.wait(1,self.button_myself).click()
        self.driver.find_element(*self.button_visitor).click()

        logging.info('============login_action==============')
        self.wait(1,self.btn_wechatlogin).click()
        logging.info('login finished!')

    def check_loginStatus(self):
        logging.info('====check_loginStatus======')
        try:
            self.wait(8,self.button_myself).click()
            # self.driver.find_element(*self.username)
        except  TimeoutException:
            logging.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            self.logout_action()
            return True

    def logout_action(self):
        logging.info('=====logout_action======')
        self.driver.find_element(*self.setButton).click()
        self.driver.find_element(*self.logoutBtn).click()


if __name__ == '__main__':
    driver = appium_desired()
    w = WechatLogin(driver)
    w.login_action()
    w.check_loginStatus()
