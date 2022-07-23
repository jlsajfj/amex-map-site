"""
honestly this isn't really even a backend- its simply a wrapper for another api
"""

import requests
import api_url

"""
querystring = {"recent_active_indicator":"false","lat_lng":"40.7579747,-73.9855426","page_size":"100"}

payload = ""
headers = {}

response = requests.request("GET", api_url.url, data=payload, headers=headers, params=querystring)

# print(response.text)
"""

import flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def home():
    return "you shouldn't be seeing this", 403

@app.route('/', methods=['POST'])
def main_api():
    if app.debug: print("recieved request")
    f_headers = flask.request.headers
    # if app.debug: print(f_headers)
    # if app.debug: print('lat_lng' in f_headers)
    
    if not 'lat_lng' in f_headers:
        if app.debug: print('lat/lng missing from request')
        return 'missing lat/lng', 400
    
    lat_lng = flask.request.headers['lat_lng']
    if app.debug: print("lat, long:", lat_lng)
    
    query_string = {"recent_active_indicator": "false", "lat_lng": lat_lng, "page_size": "100"}
    query_response = requests.request("GET", api_url.url, data = "", headers = {}, params = query_string)
    if app.debug:
        print(query_response)
        print(query_response.status_code)
    if query_response.status_code != 200:
        return f"Internal server faced {query_response.status_code} error", 500
    
    data = query_response.json()
    return data, 200

app.run()