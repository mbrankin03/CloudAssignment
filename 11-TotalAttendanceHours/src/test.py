import unittest
from flask import Flask
from app import app
from totalAttendanceHours import count

class testHours(unittest.TestCase):

    def test_hours(self):
        self.assertEqual(count(1, 2, 3, 4), 10)

    def test_RejectsMissingParams(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"error": true, "status": 400, "message": "Error: x should be an integer and also less than or equal to 33."}')
 
    def test_VowelCountRequest(self):
        tester = app.test_client(self)
        response = tester.get('/?x=12&y=4&z=3&a=5', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"error": false, "status": 200, "totalAttendanceHours": 24.0, "string": "Total ATTENDANCE hours: 24.0."}')


if __name__ == '__main__':
    unittest.main()
