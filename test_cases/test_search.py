#搜索
from commons.multi_devices import devices_start_sync
from businessViews.search import multi_search
import unittest
import logging

class TestSearch(unittest.TestCase):
    # @unittest.skip('test_multi_search')
    def test_multi_search(self):
        logging.info('======test_multi_search=====')
        devices_start_sync(multi_search)


if __name__ == '__main__':
    unittest.main()