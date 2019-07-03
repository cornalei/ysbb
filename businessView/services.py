import logging
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class Services(Common):
    lv_mine = (By.ID, 'com.clickcoo.yishuobaobao:id/lv_mine')  # 我的
    collect = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_collect')  # 收藏夹
    collect_item = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_collect_item')  # 默认收藏夹
    offline = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_offline')  # 离线收听
    draft = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_draft')  # 草稿箱
    free_flow = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_free_flow')  # 免流量收听
    activationation = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_activationation')  # 免流量收听

    suggestion = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_suggestion')  # 意见反馈
    problemcontent = (By.ID, 'com.clickcoo.yishuobaobao:id/et_problemcontent')  # 说点什么吧!
    contact = (By.ID, 'com.clickcoo.yishuobaobao:id/et_contact')  # 请填写手机、QQ、邮箱
    problemsubmit = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_problemsubmit')  # 发送


    def free(self):
        self.driver.find_element(*self.lv_mine).click()
        self.driver.find_element(*self.free_flow).click()
        try:
            self.driver.find_element(*self.activationation).click()
        except NoSuchElementException:
            logging.error('免流量加载失败！')
            self.getScreenShot('免流量加载失败!')
            return False
        else:
            logging.info('免流量加载成功！')
            return True

    def advice(self):
        self.driver.find_element(*self.lv_mine).click()
        self.driver.find_element(*self.suggestion).click()
        self.driver.find_element(*self.problemcontent).send_keys('lei-意见反馈测试，tks!')
        self.driver.find_element(*self.contact).send_keys('123456')
        self.driver.find_element(*self.problemsubmit).click()
        try:
            self.driver.find_element(*self.lv_mine).click()
        except NoSuchElementException:
            logging.error('意见提交失败！')
            self.getScreenShot('意见提交失败!')
            return False
        else:
            logging.info('意见提交成功！')
            return True







if __name__ == '__main__':
    driver=appium_desired()
    s=Services(driver)
