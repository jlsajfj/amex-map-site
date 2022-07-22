"""
honestly this isn't really even a backend- its simply a wrapper for another api
"""

import requests
import api_url

querystring = {"recent_active_indicator":"false","lat_lng":"40.7579747,-73.9855426","page_size":"100"}

payload = ""
headers = {}

response = requests.request("GET", api_url.url, data=payload, headers=headers, params=querystring)

# print(response.text)

import flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def home():
    return "you shouldn't be seeing this"

@app.route('/', methods=['POST'])
def main_api():
    print(flask.request.headers.get('lat_lng'))
    return response.text

app.run()