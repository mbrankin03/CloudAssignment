import json
import urllib
import MetricTests
import time
from discord_webhook import DiscordWebhook
from datetime import datetime
 
def sendMetrics(metrics):
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1177302498969661521/G8S4946GcYEMfkjeZe90kSPfTnPueTA8vdiciYOevDJSY-HW9OXP5Hcq_Ma7mpyyQ7Og', content=metrics)
    response = webhook.execute()

def getJsonFromURL(url):
    try:
        response = urllib.request.urlopen(url)
        reply = json.loads(response.read())
        return json.dumps(reply)
    except BaseException:
        response = "404 Error"
        return response

def fetchURL(func, text):
    config_file = open('config.json')
    URL_list = json.load(config_file)
    return (URL_list[func] + text)

def buildReport():
        
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    x = 0
    start = time.time()
    totalAttendanceHoursTest = MetricTests.totalAttendanceHours()
    if totalAttendanceHoursTest == "Success!":
        x = x+1
    studentEngagementScoreTest = MetricTests.studentEngagementScore()
    if studentEngagementScoreTest == "Success!":
        x = x+1
    riskOfStudentFailureTest = MetricTests.riskOfStudentFailure()
    if riskOfStudentFailureTest == "Success!":
        x = x+1
    canvasActivityIntensityTest = MetricTests.canvasActivityIntensity()
    if canvasActivityIntensityTest == "Success!":
        x = x+1
    maxMinTest = MetricTests.maxMin()
    if maxMinTest == "Success!":
        x = x+1
    sortTest = MetricTests.sort()
    if sortTest == "Success!":
        x = x+1
    proxyTest = MetricTests.proxy()
    if proxyTest == "Success!":
        x = x+1
    end = time.time()
    score = str(x)
    timeTaken = (end - start)
    timeTaken = str(timeTaken)[0:5]
    outputstring = "Metrics Report:  \n"
    outputstring+= ("Time: " + current_time + "\n")
    outputstring+= ("Total Attendance Hours : " + totalAttendanceHoursTest + "\n")
    outputstring+= ("Student Engagement Score : " + studentEngagementScoreTest + "\n")
    outputstring+= ("Risk Of Student Failure : " + riskOfStudentFailureTest + "\n")
    outputstring+= ("Canvas Activity Intensity : " + canvasActivityIntensityTest + "\n")
    outputstring+= ("Max Min : " + maxMinTest + "\n")
    outputstring+= ("Sort : " + sortTest + "\n")
    outputstring+= ("Proxy Router: " + proxyTest + "\n")
    outputstring+= (score + "/7 tests passed \n")
    outputstring+= ("Time Taken: "+timeTaken+"s \n")
    if x < 7:
        outputstring+= "@everyone Error has occured \n"
        # print the size of the output string
        print(len(outputstring))
    # Truncate the content if it exceeds 2000 characters
    if len(outputstring) > 2000:
        outputstring = outputstring[:1997] + "..."
        outputstring += "\nContent truncated due to character limit."
        
    return outputstring
