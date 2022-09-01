# comment
from urllib import request
from flask import Flask,request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello_world():
    if request.method=='POST':
        print(request.json)
        return request.json,200

if __name__ == "__main__":
    app.run(debug=True)