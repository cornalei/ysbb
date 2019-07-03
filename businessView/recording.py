import logging
from common.common_fun import Common,time,WebDriverWait,TimeoutException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
import random

class Recording(Common):
    lv_mine = (By.ID, 'com.clickcoo.yishuobaobao:id/lv_mine')  # 我的
    recording_btn = (By.XPATH, '//android.widget.TextView[@text="录制声音"]')  # 录制声音
    record = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_record')  # 录制
    rerecord = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_rerecord')  # 重录
    confirm = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_confirm')  # 确定
    save = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_save')  # 保存
    publish = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_publish')  # 发布

    dialog = (By.ID, 'com.clickcoo.yishuobaobao:id/ivb_dialog_desc')  # 描述按钮
    audio_desc = (By.ID, 'com.clickcoo.yishuobaobao:id/et_audio_desc')  # 请添加声音的描述
    audiodesc = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_audiodesc_confirm')  # 确定

    native_pictrue = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_native_pictrue_1')  # 添加封面
    selectbtn = (By.ID, 'com.clickcoo.yishuobaobao:id/ibtn_selectbtn')  # 图片选择
    phtoalbumsubmit = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_phtoalbumsubmit')  # 完成

    audio_title = (By.ID, 'com.clickcoo.yishuobaobao:id/et_audio_title')  # 录音标题
    send_audio = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_send_audio')  # 发布

    paly_state = (By.ID, 'com.clickcoo.yishuobaobao:id/iv_paly_state')  # 声音播放

    nativeaudiochoose = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_nativeaudiochoose')  # 上传本地声音
    audioname = (By.ID, 'com.clickcoo.yishuobaobao:id/tv_audioname')  # 本地声音列表
    nativeaudiopublish = (By.ID, 'com.clickcoo.yishuobaobao:id/btn_nativeaudiopublish')  # 发布

    def __init__(self,driver,describe,title):
        self.driver=driver
        self.describe=describe
        self.title=title

    def recording(self):
        self.driver.find_element(*self.lv_mine).click()
        self.driver.find_element(*self.recording_btn).click()
        self.driver.find_element(*self.record).click()
        time.sleep(3)
        self.driver.find_element(*self.record).click()
        self.driver.find_element(*self.rerecord).click()
        self.driver.find_element(*self.confirm).click()
        time.sleep(15)
        self.driver.find_element(*self.record).click()
        self.driver.find_element(*self.save).click()
        self.driver.find_element(*self.publish).click()
        self.driver.find_element(*self.dialog).click()
        self.driver.find_element(*self.audio_desc).send_keys(self.describe)
        self.driver.find_element(*self.audiodesc).click()
        self.driver.find_element(*self.native_pictrue).click()
        self.driver.find_elements(*self.selectbtn)[1].click()
        self.driver.find_element(*self.phtoalbumsubmit).click()
        self.driver.find_element(*self.audio_title).send_keys(self.title)
        self.driver.find_element(*self.send_audio).click()

    def check_recording(self):
        try:
            WebDriverWait(self.driver,15).until(lambda x:x.find_element_by_xpath('//*[@resource-id="com.clickcoo.yishuobaobao:id/tv_voice_title" and @text="%s" ]' %self.title))
        except TimeoutException:
            logging.error('录音发布失败！')
            self.getScreenShot('Recording release failed!')
            return False
        else:
            self.driver.find_elements(*self.paly_state)[0].click()
            logging.info('录音发布成功！')
            return True

    def upload_voice(self):
        self.driver.find_element(*self.lv_mine).click()
        self.driver.find_element(*self.recording_btn).click()
        self.driver.find_element(*self.nativeaudiochoose).click()
        self.driver.find_elements(*self.audioname)[0].click()
        self.driver.find_element(*self.nativeaudiopublish).click()
        self.driver.find_element(*self.dialog).click()
        self.driver.find_element(*self.audio_desc).send_keys(self.describe)
        self.driver.find_element(*self.audiodesc).click()
        self.driver.find_element(*self.native_pictrue).click()
        self.driver.find_elements(*self.selectbtn)[1].click()
        self.driver.find_element(*self.phtoalbumsubmit).click()
        self.driver.find_element(*self.audio_title).send_keys(self.title)
        self.driver.find_element(*self.send_audio).click()

    def check_upload_voice(self):
        try:
            WebDriverWait(self.driver,20).until(lambda x:x.find_element_by_xpath('//*[@resource-id="com.clickcoo.yishuobaobao:id/tv_voice_title" and @text="%s" ]' %self.title))
        except TimeoutException:
            logging.error('录音发布失败！')
            self.getScreenShot('Recording release failed!')
            return False
        else:
            self.driver.find_elements(*self.paly_state)[0].click()
            logging.info('录音发布成功！')
            return True

if __name__ == '__main__':
    driver=appium_desired()


    title = '小仙女' + str(random.randint(0, 1000))
    describe = '这是小仙女的声音：' + str(random.randint(0, 10000))

    r = Recording(driver, describe, title)
    r.upload_voice()
    r.check_upload_voice()

