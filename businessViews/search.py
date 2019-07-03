from businessView.search import Search
from commons.multi_devices import appium_desired,devices_start_sync

def multi_search(*desired):
    driver=appium_desired(*desired)
    s=Search(driver)
    s.search_action('a')
    assert s.check_voice()
    assert s.check_user()
    assert s.check_album()

if __name__ == '__main__':
    devices_start_sync(multi_search)