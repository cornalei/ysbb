#登录
from common.myunit_l import StartEnd
from businessView.loginView import LoginView
from businessView.wechatLogin import WechatLogin
import unittest
import logging

class TestLogin(StartEnd):
    csv_file='../data/account.csv'

    # @unittest.skip('test_login_wechat')
    def test_login_wechat(self):
        logging.info('======test_login_wechat=====')
        w = WechatLogin(self.driver)

        try:
            w.login_action()
            self.assertTrue(w.check_loginStatus())
        except BaseException as error:
            self.add_img()
            raise error

    # @unittest.skip('test_login_z3356')
    def test_login_z5630(self):
        logging.info('======test_login_15818695630=====')
        l=LoginView(self.driver)
        data=l.get_csv_data(self.csv_file,1)

        try:
            l.login_action(data[0],data[1])
            self.assertTrue(l.check_loginStatus())
        except BaseException as error:
            self.add_img()
            raise error
        # i=0
        # while i<=2:
        #     i=i+1
        #     if self.assertTrue(l.check_loginStatus()) is AssertionError:
        #         l.login_action(data[0], data[1])
        #     else:
        #         break


    @unittest.skip('skip test_login_1600')
    def test_login_1600(self):
        logging.info('======test_login_18328021600=====')
        l=LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 2)

        l.login_action(data[0], data[1])
        self.assertFalse(l.check_loginStatus(),msg='===密码错误===')

    @unittest.skip('test_login_error')
    def test_login_error(self):
        logging.info('======test_login_error=====')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 3)

        l.login_action(data[0], data[1])
        self.assertFalse(l.check_loginStatus(),msg='===账号未注册哦===')



if __name__ == '__main__':
    unittest.main()