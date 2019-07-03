import logging
from common.common_fun import Common,TimeoutException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
import random

class Icon(Common):
    lv_mine = (By.ID, 'com.clickcoo.yishuobaobao:id/lv_mine')  # 我的
    user_head = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_user_head')  # 头像
    userphoto = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_userphoto')  # 头像
    takephoto = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_takephoto')  # 拍照
    pictures = (By.ID, 'com.huawei.camera:id/shutter_button')  # 拍照按钮
    multi_confirm = (By.ID, 'com.huawei.camera:id/done_button')  # 确认选择照片
    save_tv = (By.ID, 'com.android.gallery3d:id/head_select_right')  # 确定照片
    usernickname = (By.ID, 'com.clickcoo.yishuobaobao:id/et_usernickname')  # 名称
    consumersign = (By.ID, 'com.clickcoo.yishuobaobao:id/et_consumersign')  # 描述
    updatesubmit = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_updatesubmit')  # 完成

    def personal(self,name,describe):
        self.driver.find_element(*self.lv_mine).click()
        self.driver.find_element(*self.user_head).click()
        self.driver.find_element(*self.userphoto).click()
        self.driver.find_element(*self.takephoto).click()
        self.wait(3,self.pictures).click()
        # WebDriverWait(self.driver,3).until(lambda x:x.find_element_by_id('com.huawei.camera:id/done_button'))
        # WebDriverWait(self.driver,3).until(EC.presence_of_element_located(self.multi_confirm))
        self.wait(8,self.multi_confirm)
        self.driver.find_element(*self.multi_confirm).click()
        self.driver.find_element(*self.save_tv).click()
        self.driver.find_element(*self.usernickname).send_keys(name)
        self.driver.find_element(*self.consumersign).send_keys(describe)
        self.driver.find_element(*self.updatesubmit).click()
        try:
            self.wait(5,self.lv_mine)
        except TimeoutException:
            logging.error('修改个人信息失败！')
            self.getScreenShot('Failed to modify personal information!')
            return False
        else:
            logging.info('修改个人信息成功')
            return True




if __name__ == '__main__':
    driver = appium_desired()
    i = Icon(driver)

    name = '小仙女' + str(random.randint(0, 1000))
    describe = '小仙女的个性签名：' + str(random.randint(0, 1000))

    i.personal(name,describe)



