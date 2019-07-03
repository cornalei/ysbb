import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BaseView(object):
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self,start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def wait(self,num,element):
        return WebDriverWait(self.driver,num).until(EC.presence_of_element_located(element))

    def waits(self,num,elements):
        return WebDriverWait(self.driver,num).until(EC.presence_of_all_elements_located(elements))



