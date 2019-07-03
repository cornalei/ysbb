#搜索
from common.myunit import StartEnd
from businessView.search import Search
import unittest
import logging

class TestSearch(StartEnd):
    # @unittest.skip('test_search')
    def test_search(self):
        logging.info('======test_search=====')
        s = Search(self.driver)

        s.search_action('a ')
        self.assertTrue(s.check_voice())
        self.assertTrue(s.check_user())
        self.assertTrue(s.check_album())

if __name__ == '__main__':
    unittest.main()