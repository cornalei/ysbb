from businessView.search import Search
from businessView.message import Message
from common.multi_devices import appium_desired,devices_start_sync

def multi_search(self,*desired):
    driver=appium_desired(self,*desired)
    s=Search(driver)
    s.search_action('a')
    # self.assertTrue(s.check_voice())
    # self.assertTrue(s.check_user())
    # self.assertTrue(s.check_album())
def multi_message(self,*desired):
    driver=appium_desired(self,*desired)
    m = Message(driver)
    m.delete_message()

if __name__ == '__main__':
    devices_start_sync(multi_search)
    devices_start_sync(multi_message)








