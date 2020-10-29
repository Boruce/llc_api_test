import requests
import unittest


class TestTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_001(self):
        """一个百度的接口"""
        url = "http://www.baidu.com"
        req = requests.get(url)
        print(f"状态码：{req.status_code}")
        print(f"响应文本：{req.text}")
