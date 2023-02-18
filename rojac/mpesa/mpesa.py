from codecs import utf_16_be_encode
import base64

import requests
from requests.auth import HTTPBasicAuth

import os
import environ

# os.environ.get
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


def generate_password(time_stamp):
    data_to_encode = f"{env('BUSINESS_SHORT_CODE')}{env('LNM_PASSKEY')}{time_stamp}"

    encoded_passkey = base64.b64encode(data_to_encode.encode())
    decoded_passkey = encoded_passkey.decode('utf-8')
    return decoded_passkey


def get_access_token():
    consumer_key = env('CONSUMER_KEY')
    consumer_secret = env('CONSUMER_SECRET')

    try:
        response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials',
                                    auth=HTTPBasicAuth(consumer_key, consumer_secret))
    except:
        response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials',
                                    auth=HTTPBasicAuth(consumer_key, consumer_secret), verify=False)

    json_response = response.json()
    my_access_token = json_response["access_token"]
    return my_access_token
