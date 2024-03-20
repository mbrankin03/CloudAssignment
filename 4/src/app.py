from flask import Flask
from flask import request
from flask import Response
import json
import calls
import threading

app = Flask(__name__)

@app.route('/OnDemand')
def invokeMetrics():
  metricCheck = calls.metrics()
  JsonRes = {
      "error": False, 
      "status": 200, 
      "answer": metricCheck
    }
  reply = json.dumps(JsonRes)
  response=Response(response=reply, status=200, mimetype='application/json')
  response.headers["Content-Type"]="application/json"
  response.headers["Access-Control-Allow-Origin"]="*"
  return response

if __name__ == '__main__':
  b = threading.Thread(name = 'intervalTest', target = calls.intervalTest)
  b.start()
  app.run(host='0.0.0.0',port=7007)