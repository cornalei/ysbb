from businessView.message import Message
from commons.multi_devices import appium_desired,devices_start_sync

def multi_message(self,*desired):
    driver=appium_desired(self,*desired)
    m = Message(driver)
    m.delete_message()

if __name__ == '__main__':
    devices_start_sync(multi_message)