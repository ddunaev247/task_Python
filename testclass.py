import unittest
from task_02 import valid_status, valid_content, valid_flag
import task_02
import requests
from excepion import StatusError, ContentError

class Test_function(unittest.TestCase):

    def setUp(self) -> None:
        """req - valid data, req2 - invalid data"""

        self.req = requests.get('https://cdn.pixabay.com/photo/2019/02/23/19/28/vw-4016326_1280.jpg', stream=True)
        self.req2 = requests.get('https://google.com/u/me?utm_source=develdfdfopers.google45454.com', stream=True)
        self.content1 = self.req.headers['Content-Type'].split('/')[0]
        self.content2 = self.req2.headers['Content-Type'].split('/')[0]
        self.flag1 = '1'
        self.flag2 = 'dfdsf'


    def test_valid_status(self):
        self.assertEqual(valid_status(self.req.status_code), True), 'test status no passed'
        self.assertRaises(StatusError, valid_status,self.req2.status_code), 'test status no passed'


    def test_valid_content(self):
        self.assertEqual(valid_content(self.content1), True), 'test content no passed'
        self.assertRaises(ContentError, valid_content, self.content2), 'test status no passed'


    def test_valid_flag(self):
        self.assertEqual(valid_flag(self.flag1), True), 'test status no passed'
        self.assertRaises(ValueError, valid_flag, self.flag2), 'test status no passed'


if __name__ == '__main__':
    unittest.main()


