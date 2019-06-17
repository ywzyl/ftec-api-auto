# -*- coding:utf-8 -*-
from interface.baseConfigModule.getBaseConfig_api import GetBaseConfig_API
import unittest
class GetBaseConfigTest(unittest.TestCase):
    def test_getBaseConfig(self):
        res = GetBaseConfig_API().getBaseConfig_api()
        self.assertEqual(res[0],'请求成功')
        self.assertEqual(res[1],200)

if __name__=='__main__':
    unittest.main()