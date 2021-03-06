from flask import Flask, render_template, request
import requests
import json
import pdb



app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/airquality')
def render():
    return render_template('weatherform.html')

@app.route('/weatherresult')
def render_2():
    if request.method == 'GET':
        result = request.args
        temp = {}
        option = result.get('indexx')
        temp["parameter"]=option
        temp["city"]=result.get('city')
        resp = requests.get("https://api.openaq.org/v1/measurements?",params =temp)
        
        data = json.loads(resp.text)
        if not data['results']:
            return render_template('flase.html',gas=option,city=temp["city"])
        else:
            return render_template('correct.html',datas=data['results'])
    
if __name__ == '__main__':
    app.run()
