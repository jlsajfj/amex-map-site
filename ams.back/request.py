"""
honestly this isn't really even a backend- its simply a wrapper for another api
"""

import requests
import api_url

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
    
    query_string = {"recent_active_indicator": "false", "lat_lng": lat_lng, "page_size": "100", "country_code": "CA"}
    query_response = requests.request("GET", api_url.amex, data = "", headers = {}, params = query_string)
    if app.debug:
        print(query_response)
        print(query_response.status_code)
        # print(query_response.text)
    if query_response.status_code != 200:
        return f"Internal server faced {query_response.status_code} error", 500
    
    data = query_response.json()
    
    # process data
    p_data = {'merchants':[]}
    merchants = data['merchants']
    for merch in merchants:
        name = merch['name']
        address_data = merch['address']
        address_lat = address_data['latitude']
        address_lng = address_data['longitude']
        address_lat_lng = str(address_lat) + ", " + str(address_lng)
        address_lines = address_data['address_lines']
        address_postal = address_data['postal_code']
        category_data = merch['category_details']
        category_main = category_data['name']
        open_data = merch['operating_hours']
        merch_data = {
            'name': name,
            'lat_lng': address_lat_lng,
            'address_long': address_lines,
            'postal_code': address_postal,
            'category': category_main,
            'open_hours': open_data
        }
        p_data['merchants'].append(merch_data)
    return p_data, 200

app.run()