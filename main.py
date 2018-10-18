from flask import Flask, render_template
from flask_cors import CORS
import requests, json

app = Flask(__name__)
CORS(app, supports_credentials=True)


def get_token():

	url = "http://18.185.218.25:8081/api/v1/authentication/login"
	payload={'username':'sluleburgaz@protel.com.tr', 'password':'5JyRyO+$$&'}
	r = requests.post(url, data=payload)
	token = r.json()['access_token']
	return token
@app.route('/')
def main():
	token = get_token()
	return render_template('index.html', token=token)


