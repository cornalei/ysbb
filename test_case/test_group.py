#群组
from common.myunit import StartEnd
from businessView.group import Group
import unittest,logging,random

class TestGroup(StartEnd):

    # @unittest.skip('test_group')
    def test_group(self):
        logging.info('======test_group=====')
        g = Group(self.driver)

        reason = 'join' + str(random.randint(10, 9000))
        name = 'test' + str(random.randint(10, 9000))
        desc = '这是一个测试描述' + str(random.randint(10, 9000))
        text = 'test send message' + str(random.randint(10, 9000))

        g.join_group(reason)
        self.assertTrue(g.check_join_group())

        if self.assertTrue(g.create_group(name,desc)) is AssertionError:
            logging.error('该用户好友<2个')
        else:
            self.assertTrue(g.check_create_group())

        g.send_message(text)
        self.assertTrue(g.check_send_message())

if __name__ == '__main__':
    unittest.main()