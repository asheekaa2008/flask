from flask import Flask,jsonify, request

app = Flask(__name__)

data = [
    {
        'id': 1,
        'contact': u'987656790',
        'name': u'raju', 
        'done': False
    },
    {
        'id': 2,
        'contact': u'8675312086',
        'name': u'Rahul', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': data[-1]['id'] + 1,
        'title': request.json['title'],
        'name': request.json.get('name', ""),
        'done': False
    }
    data.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)