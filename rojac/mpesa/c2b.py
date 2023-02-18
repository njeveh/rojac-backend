import requests
from requests.auth import HTTPBasicAuth
from mpesa import get_access_token
import os
import environ

os.environ.get
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


def register_url():

    my_access_token = get_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {
        'Authorization': f"Bearer {my_access_token}"
    }

    data = {
        "ShortCode": env('SHORT_CODE'),
        "ResponseType": "Completed",
        "ConfirmationURL": "https://rojac.herokuapp.com/rojac/c2b-confirmation/",
        "ValidationURL":   "https://rojac.herokuapp.com/rojac/c2b-validation/",
    }

    try:
        response = requests.request(
            "POST", 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl', headers=headers, json=data)
    except:
        response = requests.request(
            "POST", api_url, json=data, headers=headers, verify=False)

    print(response.text)


# register_url()


def c2b_transact():

    api_url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v2/simulate'
    access_token = get_access_token()

    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    payload = {
        "ShortCode": env('SHORT_CODE'),
        "CommandID": "CustomerPayBillOnline",
        "Amount": "1",
        "Msisdn": env('TEST_MSISDN'),
        "BillRefNumber": "00000"
    }

    try:
        response = requests.request(
            "POST", api_url, headers=headers, json=payload)
    except:
        response = requests.request(
            "POST", api_url, json=payload, headers=headers, verify=False)
    print(response.json())


c2b_transact()
