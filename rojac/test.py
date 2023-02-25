# from django.conf import settings as conf
import requests


def user_account_activation(uid, token):
    """gets the activation request, captures the activation id and token from the request link
    and posts them to the djoser account activation url"""

    # if conf.PRODUCTION:
    #     protocal = 'https://'
    # else:
    protocal = 'https://'
    web_url = protocal + "njeveh.pythonanywhere.com"
    post_url = web_url + "/accounts/users/activation/"
    post_data = {'uid': uid, 'token': token}
    try:
        result = requests.post(post_url, json=post_data)
        if result.status_code == 204:
            print("success")
        else:
            print(result.status_code)
            print(result.json())
    except Exception as e:
        print(e)


# user_account_activation('MET', 'QAbbageTEXT')


def test():
    x = requests.get(
        'https://njeveh.pythonanywhere.com/rojac/activate-account/MTM/bk3dhs-0553f82bcefdf660836b5ff8c35a3a88/')
    print(x.text)


test()
