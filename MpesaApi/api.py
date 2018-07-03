from flask import Flask
import requests
import json
import base64
from requests.auth import HTTPBasicAuth


consumer_key = "zSpnYAiEOOfPGDymZjNgpLfSTByzyG71"
consumer_secret = "QJTeUkEAxyBv6csW"
short_code = 174379
passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
timestamp = "20180702110120"

access_token = "whegiJEMwBPD1Oy64ZC3oi4RdfcK"

api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

data = r.json()
access_token = "Bearer" + '' + data['access_token']



app_data = ("short_code" + "passkey" + "timestamp")


password = base64.b64encode(app_data.encode('utf=8'))

#password = "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNzAyMTEwMTIw"

app = Flask(__name__)

@app.route("/")
def message():

    payload = {

        "Business_short_code": short_code,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": "254703473377",
        "PartyB": short_code,
        "PhoneNumber": "254703473377",
        "CallBackURL": "http://mpesa-requestbin.herokuapp.com/xc9fkkxc",
        "AccountReference": "test",
        "TransactionDesc": "test"
    }

    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
        }

    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    response = requests.post(url, json=payload, headers=headers)

    return response.text

if (__name__ == "__main__"):
    app.run(debug=True, port = 5070)