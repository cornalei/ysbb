import logging
from common.common_fun import Common
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class Message(Common):
    iv_square = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_square')  # 消息
    relative_to_me = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_relative_to_me')  # 与我相关
    notice_right = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_mine_notice_right')  # 与我相关-删除
    notice_back = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_mine_notice_back')  # 与我相关-返回

    notification = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_notification')  # 通知
    group_notification = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_group_notification')  # 群组通知
    common_right = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_common_right')  # 通知-删除
    common_back = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_common_back')  # 通知-返回

    def delete_message(self):
        self.find_element(self.iv_square).click()
        logging.info('===清空与我相关===')
        self.find_element(self.relative_to_me).click()
        self.find_element(self.notice_right).click()
        self.find_element(self.notice_back).click()

        logging.info('===清空通知===')
        self.find_element(self.notification).click()
        self.find_element(self.common_right).click()
        self.find_element(self.common_back).click()

        logging.info('===清空群组通知===')
        self.find_element(self.group_notification).click()
        self.find_element(self.common_right).click()
        return True


if __name__ == '__main__':
    driver=appium_desired()
    m=Message(driver)
    m.delete_message()