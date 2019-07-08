import logging
from common.common_fun import Common,TimeoutException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class Friend(Common):
    iv_square = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_square')  # 消息
    private_letter = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_send_private_letter')  # 好友按钮
    user_name = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_user_name')  # 好友名字
    search = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_search')  # 搜索


    new_friend = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_new_friend')  # 新的朋友
    btn_add = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_agree_friend_right')  # 添加朋友

    friend_search = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_friend_search')  # 搜索一说用户(昵称/手机号)
    serachkey = (By.ID, 'com.clickcoo.yishuobaobao:id/et_serachkey')  # 搜索框
    searchstart = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_searchstart')  # 搜索按钮
    userlayout = (By.ID, 'com.clickcoo.yishuobaobao:id/layout_userlayout')  # 搜索到的用户

    find_phone = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_find_phone')  # 添加通讯录好友
    thirdplatformname = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_thirdplatformname')  # 通讯录好友

    find_sina = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_find_sina')  # 邀请新浪微博好友
    circlememberlayout = (By.ID, 'com.clickcoo.yishuobaobao:id/layout_circlememberlayout')  # 新浪微博好友
    addthirduserback = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_addthirduserback')  # 返回

    find_wx = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_find_wx')  # 邀请微信好友
    mm = (By.ID, 'com.tencent.mm:id/b14')  # 创建新聊天
    # wuser = (By.ID, 'com.tencent.mm:id/de9')  # 微信用户
    # wki = (By.ID, 'com.tencent.mm:id/ki')  # 确定(1)
    # wb = (By.ID, 'com.tencent.mm:id/b00')  # 分享
    # wazz = (By.ID, 'com.tencent.mm:id/azz')  # 返回一说宝宝
    back = (By.ID, 'com.tencent.mm:id/kx')  # 返回

    find_qq = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_find_qq')  # 邀请QQ好友
    ivTitleName = (By.ID, 'com.tencent.mobileqq:id/ivTitleName')  # 发送给


    def friends(self):
        self.find_element(self.iv_square).click()
        logging.info('===搜索已添加好友===')
        self.find_element(self.private_letter).click()
        try:
            name1=self.find_elements(self.user_name)[0].text
        except TimeoutException:
            logging.info('该用户没有好友')
            return False
        else:
            self.find_element(self.search).send_keys(name1)
            name2 = self.find_elements(self.user_name)[0].text
            if name1==name2:
                logging.info('搜索好友成功')
                return True
            else:
                logging.error('搜索好友失败！')
                self.getScreenShot('搜索好友失败！')
                return False

    def thirdfriend(self):
        self.find_element(self.iv_square).click()
        logging.info('===新的朋友-第三方===')
        self.find_element(self.new_friend).click()
        self.find_element(self.btn_add).click()
        self.find_element(self.find_sina).click()
        try:
            self.waits(5,self.circlememberlayout)[0]
        except TimeoutException:
            logging.error('新浪微博好友页面加载失败！')
            self.getScreenShot('新浪微博好友页面加载失败！')
            return False
        else:
            logging.info('新浪微博好友获取成功')
            self.find_element(self.addthirduserback).click()

            self.find_element(self.find_wx).click()
            try:
                self.wait(2,self.mm)
            except TimeoutException:
                logging.error('微信跳转失败！')
                return False
            else:
                logging.info('微信跳转成功')
                self.find_element(self.back).click()

            self.find_element(self.find_qq).click()
            try:
                self.find_element(self.ivTitleName)
            except TimeoutException:
                logging.error('QQ跳转失败！')
                return False
            else:
                logging.info('QQ跳转成功')
                return True

    def newfriend(self,username):
        self.find_element(self.iv_square).click()
        logging.info('===新的朋友===')
        self.find_element(self.new_friend).click()
        self.find_element(self.btn_add).click()
        self.find_element(self.find_phone).click()
        try:
            title = self.find_element(self.thirdplatformname).text
        except TimeoutException:
            logging.error('通讯录好友页面加载失败！')
            self.getScreenShot('通讯录好友页面加载失败！')
            return False
        else:
            if title == '通讯录好友':
                logging.info('跳转通讯录好友界面')
                self.find_element(self.addthirduserback).click()
            else:
                logging.error('通讯录好友页面加载失败！')
                self.getScreenShot('通讯录好友页面加载失败！')
                return False

        self.find_element(self.friend_search).click()
        self.find_element(self.serachkey).send_keys(username)
        self.find_element(self.searchstart).click()

        try:
            self.waits(5,self.userlayout)[0]
        except TimeoutException:
            logging.error('没有该用户！')
            self.getScreenShot('没有该用户！')
            return False
        else:
            logging.info('搜索用户成功')
            return True














if __name__ == '__main__':
    driver=appium_desired()
    f=Friend(driver)
    # f.friends()
    f.newfriend('虫虫')
    # f.thirdfriend()