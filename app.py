from flask import Flask, request, jsonify
import requests
import os 
port = request.server.port
lead = None
app = Flask(__name__)

def get_sub_id(token):
    url_sub = f'http://217.25.93.249/r/click_api/v3?token={token}&info=1'
    response_sub = requests.get(url_sub).json()
    print(response_sub)
    sub_id = response_sub['info']['sub_id']
    return sub_id

@app.route('/', methods=['GET'])
def hello():
    return jsonify("hi")  # Return the sub_id in JSON format


@app.route('/getsub', methods=['POST'])
def getsub():
    global lead
    data = request.get_json()  # Get the JSON data from the request
    token = data.get('token')  # Extract the token from the JSON data
    lead = get_sub_id(token)  # Call the function to get the sub_id
    return jsonify(lead=lead)  # Return the sub_id in JSON format


def info_item(_name, _phone, _offer_id, _utm_campaign, _utm_content, _click_id, _subhype) -> None:
    data = {
        'name': _name,
        'phone': _phone,
        'offerId': _offer_id,
        'utm_campaign': _utm_campaign,
        'utm_content': _utm_content,
        'clickid': _click_id,
    }

    _url = 'https://lead.culture-offer.com/api/v3/lead/add'
    headers = {
        'Content-Type': 'application/json',
        'X-Token': _subhype,
    }

    response = requests.post(_url, headers=headers, json=data)
    http_code = response.status_code
    response_json = response.json()

@app.route('/create_lead', methods=['POST'])
def create_lead_item():
    data = request.json  # Extract JSON data
    _name_ = data.get('name')  # Get name from JSON
    _phone_ = data.get('phone')
    _offer_id_ = data.get('offer_id')
    _utm_campaign_ = data.get('utm_campaign')
    _utm_content_ = data.get('utm_content')
    _subhype_ = data.get('subhype')
    _click_id_ = get_sub_id(data.get('token')
    return jsonify(info_item(_name_, _phone_, _offer_id_, _utm_campaign_, _utm_content_, _click_id_, _subhype_))
if __name__ == '__main__':
    app.run()

from myproject import app
if __name__ == "__main__":
    app.run(port=port)


