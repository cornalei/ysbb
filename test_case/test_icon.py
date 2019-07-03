#个人信息
from common.myunit import StartEnd
from businessView.icon import Icon
import unittest
import logging
import random

class TestIcon(StartEnd):
    # @unittest.skip('test_personal')
    def test_personal(self):
        logging.info('======test_personal=====')
        i = Icon(self.driver)
        name = '小仙女' + str(random.randint(0, 1000))
        describe = '小仙女的个性签名：' + str(random.randint(0, 1000))

        self.assertTrue(i.personal(name, describe))



if __name__ == '__main__':
    unittest.main()