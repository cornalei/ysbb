import logging
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class Set(Common):
    lv_mine = (By.ID, 'com.clickcoo.yishuobaobao:id/lv_mine')  # 我的
    iv_setting = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_setting')  # 设置
    account = (By.ID, 'com.clickcoo.yishuobaobao:id/layout_account')  # 账号与安全
    accountpass = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_accountsafe_accountpass')  # 修改密码
    sendcode = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_change_sendcode')  # 获取验证码
    phone = (By.ID, 'com.clickcoo.yishuobaobao:id/et_verifycode_phone')  # 请输入验证码
    position = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_verifycode_position')  # 下一步
    setpassword = (By.ID, 'com.clickcoo.yishuobaobao:id/edt_setpassword')  # 请输入密码

    aboutyishuo = (By.ID, 'com.clickcoo.yishuobaobao:id/layout_aboutyishuo')  # 关于一说宝宝
    TextView01 = (By.ID, 'com.clickcoo.yishuobaobao:id/TextView01')  # 官方微博
    aboutback = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_aboutback')  # 返回
    # versioncode = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_versioncode')  # 版本号

    def sets(self):
        self.driver.find_element(*self.lv_mine).click()
        self.driver.find_element(*self.iv_setting).click()
        self.driver.find_element(*self.aboutyishuo).click()
        logging.info('===检查关于一说宝宝===')
        try:
            self.driver.find_element(*self.TextView01).click()
        except NoSuchElementException:
            logging.error('没有官方微博信息！')
            self.getScreenShot('没有官方微博信息！')
            return False
        else:
            logging.info('官方信息正常')
            self.driver.find_element(*self.aboutback).click()

        logging.info('===检查错误验证码能否使用===')
        try:
            self.driver.find_element(*self.account).click()
        except NoSuchElementException:
            logging.error('长连接断开！')
            self.getScreenShot('长连接断开！')
        else:
            self.driver.find_element(*self.accountpass).click()
            self.driver.find_element(*self.sendcode).click()
            self.wait(3,self.phone)
            self.driver.find_element(*self.phone).send_keys('111111')
            self.driver.find_element(*self.position).click()
            try:
                self.driver.find_element(*self.setpassword)
            except NoSuchElementException:
                logging.info('验证码正常')
                return True
            else:
                logging.error('验证码异常！')
                return False


if __name__ == '__main__':
    driver=appium_desired()
    s=Set(driver)
    s.sets()
