import logging,time
from common.common_fun import Common,TimeoutException,NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class Player(Common):
    playerrevolve = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_playerrevolve')  # 播放器
    forwardaction = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_forwardaction')  # 转发按钮
    forwardtext = (By.ID, 'com.clickcoo.yishuobaobao:id/et_forwardtext')  # 评论输入框
    audioforwardsubmit = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_audioforwardsubmit')  # 发布

    btn_collectaction = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_collectaction')  # 收藏按钮
    collect_item = (By.ID, 'com.clickcoo.yishuobaobao:id/rl_collect_item')  # 收藏夹
    btn_back = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_back')  # 收藏夹-返回
    iv_return = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_return')  # 收起播放器
    audiorecommend = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_audiorecommend')  # 声音名称

    btn_downloadaction = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_downloadaction')  # 下载按钮
    btn_shareaction = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_shareaction')  # 分享按钮
    share_wechat = (By.XPATH, "//android.widget.TextView[contains(@text,'微信朋友圈')]")  # 微信朋友圈
    published = (By.ID, 'com.tencent.mm:id/ki')  # 发表

    audiomoreaction = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_audiomoreaction')  # 举报按钮
    reportselect = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_reportselect')  # 原因选择
    editTextMessage = (By.ID, 'com.clickcoo.yishuobaobao:id/editTextMessage')  # 原因描述
    btn_dialogconfirm = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_dialogconfirm')  # 确定举报
    btn_reportcommit = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_reportcommit')  # 提交按钮

    comment = (By.ID, 'com.clickcoo.yishuobaobao:id/comment_number')  # 评论按钮
    commenttext = (By.ID, 'com.clickcoo.yishuobaobao:id/ed_commenttext')  # 评论输入框
    btn_face = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_face')  # 表情
    item_iv_face = (By.ID, 'com.clickcoo.yishuobaobao:id/item_iv_face')  # 表情列表
    sendcomment = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_sendcomment')  # 发送按钮
    commentcontent = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_commentcontent')  # 评论内容

    lv_mine = (By.ID, 'com.clickcoo.yishuobaobao:id/lv_mine')  # 我的
    collect = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_collect')  # 收藏夹

    def forwarding(self):
        logging.info('===转发声音===')
        self.driver.find_element(*self.playerrevolve).click()
        self.wait(1,self.forwardaction).click()
        self.wait(1,self.forwardtext).send_keys('优秀！')
        self.driver.find_element(*self.audioforwardsubmit).click()
        logging.info('转发成功')
        return True

    def play_collection(self):
        self.driver.find_element(*self.playerrevolve).click()
        voice_name=self.wait(1,self.audiorecommend).text
        time.sleep(1.5)
        self.driver.find_element(*self.btn_collectaction).click()
        self.waits(1,self.collect_item)[0].click()
        return voice_name

    def check_collection(self):
        name = self.play_collection()
        element = (By.XPATH, "//android.widget.TextView[contains(@text,'%s')]" % name)
        try:
            self.driver.find_element(*self.btn_back).click()
        except NoSuchElementException:
            self.driver.find_element(*self.iv_return).click()
        else:
            self.driver.find_element(*self.iv_return).click()

        self.driver.find_element(*self.lv_mine).click()
        self.driver.find_element(*self.collect).click()
        self.driver.find_elements(*self.collect_item)[0].click()
        time.sleep(2)
        try:
            self.swipeUp_s(*element)
        except NoSuchElementException:
            logging.error('收藏声音失败！')
            self.getScreenShot('收藏声音失败！')
            return False
        else:
            logging.info('收藏声音成功')
            return True

    def play_check(self):
        self.driver.find_element(*self.playerrevolve).click()
        self.wait(2,self.audiomoreaction).click()
        self.driver.find_elements(*self.reportselect)[-1].click()
        self.driver.find_element(*self.editTextMessage).send_keys('lei-举报测试，tks！')
        self.driver.find_element(*self.btn_reportcommit).click()
        self.driver.find_element(*self.btn_dialogconfirm).click()
        logging.info('举报成功')

        logging.info('===点击下载===')
        self.driver.find_element(*self.btn_downloadaction).click()
        self.wait(5,self.btn_shareaction).click()
        self.wait(1,self.share_wechat).click()
        try:
            self.wait(1,self.published).click()
        except  TimeoutException:
            logging.error('分享声音失败！')
            self.getScreenShot('分享声音失败！')
            return False
        else:
            logging.info('分享声音到朋友圈成功')
            return True

    def comments(self):
        self.driver.find_element(*self.playerrevolve).click()
        self.wait(2,self.comment).click()
        self.wait(1,self.commenttext).send_keys('赞！')
        self.driver.find_element(*self.btn_face).click()
        self.driver.find_elements(*self.item_iv_face)[0].click()
        self.driver.find_element(*self.sendcomment).click()

    def check_comments(self):
        try:
            text = self.waits(2,self.commentcontent)[0].text
        except TimeoutException:
            logging.error('评论失败！')
            self.getScreenShot('评论失败！')
            return False
        else:
            logging.info('评论内容: %s' % text)
            a = '赞！'
            if a in text:
                logging.info('评论成功！')
                return True
            else:
                logging.error('评论失败！')
                self.getScreenShot('评论失败！')
                return False





if __name__ == '__main__':
    driver=appium_desired()
    p=Player(driver)


    # p.play_check()
    # p.comments()
    # p.check_comments()

    # p.forwarding()

    p.check_collection()

