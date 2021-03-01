import unittest
from task_02 import valid_status, valid_content
import requests
from excepion import StatusError, ContentError

class Test_function(unittest.TestCase):

    def setUp(self) -> None:
        """req - valid data, req2 - invalid data"""

        self.req = requests.get('https://cdn.pixabay.com/photo/2019/02/23/19/28/vw-4016326_1280.jpg', stream=True)
        self.req2 = requests.get('https://google.com/u/me?utm_source=develdfdfopers.google45454.com', stream=True)
        self.content1 = self.req.headers['Content-Type'].split('/')[0]
        self.content2 = self.req2.headers['Content-Type'].split('/')[0]

    def test_valid_status(self):
        self.assertEqual(valid_status(self.req.status_code), True), 'test status no passed'
        with self.assertRaises(StatusError) as context:
            valid_status(self.req2.status_code)
        self.assertTrue('the requested page was not found' in str(context.exception)),'test status no passed'

    def test_valid_content(self):
        self.assertEqual(valid_content(self.content1), True), 'test content no passed'
        with self.assertRaises(ContentError) as context:
            valid_content(self.content2)
        self.assertTrue('the downloadable content is not an image' in str(context.exception)), 'test content no passed'


if __name__ == '__main__':
    unittest.main()


