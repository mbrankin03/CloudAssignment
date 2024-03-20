from flask import Flask
from flask import request
from flask import Response
import json
import urllib, json
from buildURL import buildURL

app = Flask(__name__)

@app.route('/')
def proxyrt():
    functionName = request.args.get("func")
    text = request.args.get("text")
    additional_params = {key: request.args.get(key) for key in request.args.keys() if key not in ["func", "text"]}
    url = buildURL(functionName, text, **additional_params)
    url = url.replace(" ", "%20")
    response = urllib.request.urlopen(url)
    print(url)
    reply = json.loads(response.read())
    reply = json.dumps(reply)
    response=Response(response=reply, status=200, mimetype='application/json')
    response.headers["Content-Type"]="application/json"
    response.headers["Access-Control-Allow-Origin"]="*"
    return response

@app.route('/test')
def testPath():

  jsonTestRes = {
    "error": False, 
    "status": 200, 
    "answer": "Test Successful"
  }
  reply = json.dumps(jsonTestRes)
  response=Response(response=reply, status=200, mimetype='application/json')
  response.headers["Content-Type"]="application/json"
  response.headers["Access-Control-Allow-Origin"]="*"
  return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5010)
