import helpers

def totalAttendanceHours():
    response = helpers.getJsonFromURL(helpers.fetchURL('totalattendancehours', 'x=11&y=11&z=11&a=11'))
    expected = '{"error": false, "status": 200, "totalAttendanceHours": 44.0, "string": "Total ATTENDANCE hours: 44.0."}'
    if expected != response:
        return "Error: Expected " + expected + " but got " + response
    return "Success!"

def studentEngagementScore():
    response = helpers.getJsonFromURL(helpers.fetchURL('studentengagementscore', 'w=11&x=11&y=11&z=11'))
    expected = '{"Answer": 37, "Error": false, "Status": 200, "Message": "37 is the student engagement score "}'
    if expected != response:
        return "Error: Expected " + expected + " but got " + response
    return "Success!"

def riskOfStudentFailure():
    response = helpers.getJsonFromURL(helpers.fetchURL('riskofstudentfailure', 'w=11&x=11&y=11&z=11&a=11'))
    expected = '{"string": "Student Engagement score is 37 and the cut off is 11", "answer": "Student is not at risk of failing", "status": 200}'
    if expected != response:
        return "Error: Expected " + expected + " but got " + response
    return "Success!"

def canvasActivityIntensity():
    response = helpers.getJsonFromURL(helpers.fetchURL('canvasactivityintensity', 'x=10'))
    expected = '{"error": false, "string": "Activity Intensity: Medium intensity activity", "status": 200, "answer": "Medium intensity activity"}'
    if expected != response:
        return "Error: Expected " + expected + " but got " + response
    return "Success!"

def maxMin():
    response = helpers.getJsonFromURL(helpers.fetchURL('maxmin', 'item_1=a&item_2=value2&item_3=value3&item_4=value4&attendance_1=11&attendance_2=22&attendance_3=33&attendance_4=44'))
    expected = '{"error": false, "items": ["a", "value2", "value3", "value4"], "attendance": ["11", "22", "33", "44"], "max_item": "value4 - 44", "min_item": "a - 11"}'
    if expected != response:
        return "Error: Expected " + expected + " but got " + response
    return "Success!"

def sort():
    response = helpers.getJsonFromURL(helpers.fetchURL('sort', 'item_1=a&item_2=value2&item_3=value3&item_4=value4&attendance_1=11&attendance_2=22&attendance_3=33&attendance_4=44'))
    expected = '{"error": false, "items": ["a", "value2", "value3", "value4"], "attendance": ["11", "22", "33", "44"], "sorted_attendance": [{"item": "value4", "attendance": "44"}, {"item": "value3", "attendance": "33"}, {"item": "value2", "attendance": "22"}, {"item": "a", "attendance": "11"}]}'
    if expected != response:
        return "Error: Expected " + expected + " but got " + response
    return "Success!"

def proxy():
    response = helpers.getJsonFromURL(helpers.fetchURL('proxy', '/test'))
    expected = '{"error": false, "status": 200, "answer": "Test Successful"}'
    if expected != response:
        return "Error: Expected " + expected + " but got " + response
    return "Success!"
