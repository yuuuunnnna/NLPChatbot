from flask import Flask, render_template, request, url_for
from flask_ngrok import run_with_ngrok

import tensorflow as tf
from tensorflow import keras
import numpy as np
import sware_detector as sd

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/',  methods=['GET', "POST"])

def main():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        # 페이지에서 데이터 받아오기
        sentence=str(request.form['sentence'])
                
        result=sd.sentence_predict(sentence)
        
    return render_template("index.html", result = result)

if __name__ == "__main__":
    app.run()


# from flask import Flask, render_template, make_response, jsonify, json, request
# from flask_ngrok import run_with_ngrok


# import sys
# application = Flask(__name__)
# run_with_ngrok(application)
 

# @application.route("/", methods = ["GET"])
# def index_page_landing():
#     return render_template("index.html")


# @application.route("/webhook", methods = ["GET"])
# def webhook():
#     #return make_response(json.dumps(results()))
#     body = request.json

#     #전체 json 데이터 출력
#     print.print(body)
#     print("\n\n\n")

# def results():
#     req = request.get_json(force=True)
#     print(req)
#     queryText = req.get("queryResult").get("queryText")
#     print(queryText)
        
#     params = req.get('queryResult').get("queryResult")
    
#     respText = {
#         "fulfillmentMessages": [
#             {
#                 "text":{
#                     "text":[
#                         #str(req.get("queryResult").get("fulfillmentMessages"))
#                         str("미안합니데이. 잘 모르겠심더.")
                        
#                     ]
#                 }
#             }
#         ]
#     }
    
#     return respText
    
# if __name__ == "__main__":
#     #application.run(host='0.0.0.0', port=5000, debug=True)
#     application.run()