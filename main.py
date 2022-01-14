from flask import Flask,request,jsonify
from data import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data":data,
        "message":"Successful"
    }),200

@app.route("/variant")
def variant():
    name = request.srgs.get('variant')
    v_data = next(item for item in data if item["variant"]== variant)
    return jsonify({
        "data":v_data,
        "message":"Successful"
    }),200

if __name__ == "__main__":
    app.run()