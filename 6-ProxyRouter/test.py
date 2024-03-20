import unittest
from flask import Flask
from app import app
from buildURL import buildURL

class testProxy(unittest.TestCase):
    
    def test_buildURL(self):
    # Define additional parameters
        additional_params = {"y": "11", "z": "11", "a": "11"}

    # Call the buildURL function with the specified parameters
        result_url = buildURL("totalattendancehours", "x=11", **additional_params)

    # Define the expected URL based on the configuration and additional parameters
        expected_url = (
        "http://totalattendancehours.40297935.qpc.hal.davecutting.uk/?x=11&y=11&z=11&a=11"
        )

        # Assert that the result URL matches the expected URL
        self.assertEqual(result_url, expected_url)
        
    def test_CallTotalAttendanceHours(self):
        tester = app.test_client(self)
        response = tester.get("/?func=totalattendancehours&x=10&y=20&z=30&a=40", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"error": false, "status": 200, "totalAttendanceHours": 100.0, "string": "Total ATTENDANCE hours: 100.0."}')

    def test_CallStudentEngagementScore(self):
        tester = app.test_client(self)
        response = tester.get("/?func=studentengagementscore&w=10&x=20&y=30&z=40", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"Answer": 67, "Error": false, "Status": 200, "Message": "67 is the student engagement score "}')

    def test_CallRiskOfStudentFailure(self):
        tester = app.test_client(self)
        response = tester.get("/?func=riskofstudentfailure&w=10&x=10&y=10&z=10&a=10", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"string": "Student Engagement score is 33 and the cut off is 10", "answer": "Student is not at risk of failing", "status": 200}')
    
    def test_CallCanvasActivityIntensity(self):
        tester = app.test_client(self)
        response = tester.get("/?func=canvasactivityintensity&x=10", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"error": false, "string": "Activity Intensity: Medium intensity activity", "status": 200, "answer": "Medium intensity activity"}')

    def test_CallMaxMin(self):
        tester = app.test_client(self)
        response = tester.get("/?func=maxmin&item_1=a&item_2=value2&item_3=value3&item_4=value4&attendance_1=11&attendance_2=22&attendance_3=33&attendance_4=44", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"error": false, "items": ["a", "value2", "value3", "value4"], "attendance": ["11", "22", "33", "44"], "max_item": "value4 - 44", "min_item": "a - 11"}')

    def test_CallSort(self):
        tester = app.test_client(self)
        response = tester.get("/?func=sort&item_1=a&item_2=value2&item_3=value3&item_4=value4&attendance_1=11&attendance_2=22&attendance_3=33&attendance_4=44", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"error": false, "items": ["a", "value2", "value3", "value4"], "attendance": ["11", "22", "33", "44"], "sorted_attendance": [{"item": "value4", "attendance": "44"}, {"item": "value3", "attendance": "33"}, {"item": "value2", "attendance": "22"}, {"item": "a", "attendance": "11"}]}')

    