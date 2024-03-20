import json
from flask import Flask, request, jsonify, Response
from totalAttendanceHours import count

app = Flask(__name__)

@app.route('/')
def totalAttendanceHrs():
    x = request.args.get("x")
    y = request.args.get("y")
    z = request.args.get("z")
    a = request.args.get("a")

    if x is None or not x.isdigit() or int(x) > 33:
        jsonErrorRes = errorMessage("x", 33)
    elif y is None or not y.isdigit() or int(y) > 22:
        jsonErrorRes = errorMessage("y", 22)
    elif z is None or not z.isdigit() or int(z) > 44:
        jsonErrorRes = errorMessage("z", 44)
    elif a is None or not a.isdigit() or int(a) > 55:
        jsonErrorRes = errorMessage("a", 55)
    else:
        answer = count(x, y, z, a)
        jsonRes = {
            "error": False,
            "status": 200,
            "totalAttendanceHours": answer,
            "string": "Total ATTENDANCE hours: " + str(answer) + "."
        }
        reply = json.dumps(jsonRes)
        response = Response(response=reply, status=200, mimetype='application/json')
        response.headers["Content-Type"] = "application/json"
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response

    reply = json.dumps(jsonErrorRes)
    response = Response(response=reply, status=400, mimetype='application/json')
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

def errorMessage(param, max_value):
    msg = f"Error: {param} should be an integer and also less than or equal to {max_value}."
    return {
        "error": True,
        "status": 400,
        "message": msg
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2003)
