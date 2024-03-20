from flask import Flask
from flask import request
from flask import Response
from tinydb import TinyDB, Query
import json
import funcs

app = Flask(__name__)

@app.route('/save')
def statefulSaving():
  x = request.args.get("x")
  key = funcs.insertInDB(db, x)
  jsonSaveRes = {
    "error": False, 
    "status": 200, 
    "answer": key
  }
  reply = json.dumps(jsonSaveRes)
  response=Response(response=reply, status=200, mimetype='application/json')
  response.headers["Content-Type"]="application/json"
  response.headers["Access-Control-Allow-Origin"]="*"
  return response

@app.route('/load')
def statefulLoading():
  x = request.args.get("x")
  string = funcs.getFromDB(db, x)
  jsonLoadRes = {
    "error": False, 
    "status": 200, 
    "answer": string
  }
  reply = json.dumps(jsonLoadRes)
  response=Response(response=reply, status=200, mimetype='application/json')
  response.headers["Content-Type"]="application/json"
  response.headers["Access-Control-Allow-Origin"]="*"
  return response


if __name__ == '__main__':
    db = TinyDB('db.json')
    app.run(host='0.0.0.0',port=5015)
