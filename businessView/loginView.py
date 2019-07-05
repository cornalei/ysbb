import logging
from common.common_fun import Common,TimeoutException
from common.desired_caps_l import appium_desired
from selenium.webdriver.common.by import By

class LoginView(Common):
    tv_login = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_login')  #引导页-登录
    username_type = (By.ID, 'com.clickcoo.yishuobaobao:id/et_username')  # 手机号
    password_type=(By.ID,'com.clickcoo.yishuobaobao:id/et_userpwd')#密码
    loginBtn=(By.ID,'com.clickcoo.yishuobaobao:id/rl_loginsubmit')#提交登录
    baobao = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_baobao')  # 一说宝宝引导

    def login_action(self,username,password):
        self.swipeLeft2()
        logging.info('===引导页登录====')
        self.driver.find_element(*self.tv_login).click()

        logging.info('============login_action==============')
        logging.info('username is:%s' %username)
        self.wait(1,self.username_type).send_keys(username)

        logging.info('password is:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished！')

    def check_loginStatus(self):
        logging.info('====check_loginStatus======')
        try:
            self.wait(8,self.baobao).click()
        except  TimeoutException:
            logging.error('登录失败！')
            self.getScreenShot('登录失败！')
            return False
        else:
            logging.info('登录成功')
            return True

if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    l.login_action('13928413356','123456')
    l.check_loginStatus()