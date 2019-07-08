import logging
from common.common_fun import Common,TimeoutException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
import random
class Group(Common):
    trends = (By.ID, 'com.clickcoo.yishuobaobao:id/lv_trends')  #动态按钮
    home_group = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_home_group')  #群组
    isjoin = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_isjoin')  #申请加入
    collect_name = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_collect_name')  #输入验证信息
    btn_confirm = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_confirm')  #确认申请加入
    validate = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_validate')  #验证中

    create = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_fragment_currency_create')  #创建群组
    create_picture = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_group_create')  #上传封面
#魅族7.1.1
    # choose_picture = (By.XPATH, "//android.widget.Button[contains(@text,'从手机相册选择')]")  # 相册选择封面
    # pictures = (By.ID, 'com.meizu.media.gallery:id/thumbnail')  #相册
    # multi_confirm = (By.ID, 'com.meizu.media.gallery:id/action_get_multi_confirm')  #确认选择照片
    # save_tv = (By.ID, 'com.meizu.media.gallery:id/action_crop_save_tv')  #确定照片

#华为荣耀9
    choose_picture = (By.XPATH, "//android.widget.Button[contains(@text,'拍照')]")  # 拍照
    pictures = (By.ID, 'com.huawei.camera:id/shutter_button')  #拍照按钮
    multi_confirm = (By.ID, 'com.huawei.camera:id/done_button')  #确认选择照片
    save_tv = (By.ID, 'com.android.gallery3d:id/head_select_right')  #确定照片

    create_desc = (By.ID, 'com.clickcoo.yishuobaobao:id/edt_group_create_desc')  #群描述
    create_name = (By.ID, 'com.clickcoo.yishuobaobao:id/edt_group_create_name')  #命名群组
    select = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_select')  #隐私群组
    rl_next = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_next')  #下一步
    aod_item = (By.ID, 'com.clickcoo.yishuobaobao:id/cb_group_aod_item')  #选择好友
    friend_right = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_group_friend_right')  #完成
    friend_back = (By.ID, "com.clickcoo.yishuobaobao:id/btn_group_friend_back")  # 返回

    comment = (By.ID, "com.clickcoo.yishuobaobao:id/tv_comment")  # 参与讨论
    comment_text = (By.ID, "com.clickcoo.yishuobaobao:id/ed_commenttext")  # 请输入文字信息
    sendcomment = (By.ID, "com.clickcoo.yishuobaobao:id/iv_sendcomment")  # 请输入文字信息
    btn_face = (By.ID, "com.clickcoo.yishuobaobao:id/btn_face")  # 表情按钮
    iv_face = (By.ID, "com.clickcoo.yishuobaobao:id/item_iv_face")  # 经典表情

    group_name = (By.XPATH, "//*[@resource-id='com.clickcoo.yishuobaobao:id/tv_group_item_name'][contains(@text,'test')]")  # 群组名字
    oneself_text = (By.XPATH, "//*[@resource-id='com.clickcoo.yishuobaobao:id/tv_letter_oneself_text'][contains(@text,'test send message')]")  # 发送到群里的消息

    def join_group(self,collect_name):
        logging.info('===申请加入群组====')
        self.find_element(self.trends).click()
        self.check_radio()
        self.find_element(self.home_group).click()
        self.waits(3,self.isjoin)[1].click()
        self.wait(1,self.collect_name).send_keys(collect_name)
        self.find_element(self.btn_confirm).click()

    def check_join_group(self):
        logging.info('====check_join_group======')
        try:
            self.wait(1,self.validate).click()
        except  TimeoutException:
            logging.error('加入群组失败！')
            self.getScreenShot('加入群组失败！')
            return False
        else:
            logging.info('加入群组成功')
            return True

    def create_group(self,name,desc):
        logging.info('===创建群组====')
        self.find_element(self.trends).click()
        self.find_element(self.home_group).click()

        self.find_element(self.create).click()
        self.find_element(self.create_picture).click()
        self.wait(2,self.choose_picture).click()
        self.wait(2,self.pictures).click()
        self.wait(5,self.multi_confirm)
        self.find_element(self.multi_confirm).click()
        self.find_element(self.save_tv).click()

        self.wait(2,self.create_name).send_keys(name)
        self.find_element(self.create_desc).send_keys(desc)
        self.find_element(self.select).click()
        self.find_element(self.rl_next).click()

        try:
            self.waits(2,self.aod_item)[0].click()
            self.waits(2,self.aod_item)[1].click()
        except TimeoutException:
            self.find_element(self.friend_back).click()
            return False
        else:
            self.find_element(self.friend_right).click()
            return True

    def check_create_group(self):
        logging.info('====check_create_group======')
        try:
            self.wait(5,self.group_name).click()
        except  TimeoutException:
            logging.error('创建群组失败！')
            self.getScreenShot('创建群组失败！')
            return False
        else:
            logging.info('创建群组成功')
            return True

    def send_message(self,commenttext):
        logging.info('===发送群组消息====')

        # self.find_element(self.trends).click()
        # self.find_element(self.home_group).click()
        # self.find_element(self.group_name).click()

        self.wait(1,self.comment).click()
        self.wait(1,self.comment_text).send_keys(commenttext)
        self.find_element(self.btn_face).click()
        self.find_elements(self.iv_face)[2].click()
        self.find_element(self.sendcomment).click()

    def check_send_message(self):
        logging.info('====check_send_message======')
        try:
            self.wait(5,self.oneself_text).click()
        except  TimeoutException:
            logging.error('发送消息失败！')
            self.getScreenShot('发送消息失败！')
            return False
        else:
            logging.info('发送消息成功')
            return True




if __name__ == '__main__':
    driver = appium_desired()
    g = Group(driver)

    reason = 'test join group' + str(random.randint(10, 9000))
    name = 'test' + str(random.randint(10, 9000))
    desc = '这是一个测试描述' + str(random.randint(10, 9000))
    text = 'test send message' + str(random.randint(10, 9000))

    # g.join_group(reason)
    # g.check_join_group()

    g.create_group(name,desc)
    g.check_create_group()

    # g.send_message(text)
    # g.check_send_message()
