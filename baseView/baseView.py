from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,time

class BaseView(object):
    def __init__(self,driver):
        self.driver=driver

    def getTime(self):
        self.now=time.strftime("%Y%m%d-%H.%M.%S")
        return self.now

    def getScreenShot(self,module):
        timestrmap=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s%s.png' %(module,timestrmap)
        # logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)
        print('screenshot:',module,timestrmap,'.png')

    def find_element(self,loc):
        try:
            WebDriverWait(self.driver,1).until(EC.presence_of_element_located(loc))
        except Exception:
            self.getScreenShot('error')
        finally:
            return WebDriverWait(self.driver,1).until(EC.presence_of_element_located(loc))

    def find_elements(self,loc):
        try:
            WebDriverWait(self.driver,1).until(EC.presence_of_all_elements_located(loc))
        except Exception:
            self.getScreenShot('error')
        finally:
            return WebDriverWait(self.driver,1).until(EC.presence_of_all_elements_located(loc))

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self,start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def wait(self,num,element):
        try:
            WebDriverWait(self.driver,num).until(EC.presence_of_element_located(element))
        except Exception:
            self.getScreenShot('error')
        finally:
            return WebDriverWait(self.driver,num).until(EC.presence_of_element_located(element))

    def waits(self,num,elements):
        try:
            WebDriverWait(self.driver,num).until(EC.presence_of_all_elements_located(elements))
        except Exception:
            self.getScreenShot('error')
        finally:
            return WebDriverWait(self.driver,num).until(EC.presence_of_all_elements_located(elements))



