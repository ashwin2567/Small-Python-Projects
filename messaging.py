import requests
import json

def send_sms(number, message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    params = {
        'authorization' : 'oPhNtdxjH8rfeLX2OYMcy7TzRlG9SpkZn4uam3DEWJwUK10iFscUixMp9kdbv2eKEa5VQ6sz8ATtwRGP',
        'route' : 'p',
        'sender_id' : 'FSTSMS',
        'message' : message,
        'language' : 'english',
        'numbers' : number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)

send_sms("8318566008", "This is a test message")
