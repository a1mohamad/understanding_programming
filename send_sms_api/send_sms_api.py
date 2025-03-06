import requests


response = requests.get('http://www.boredapi.com/api/activity?type=recreational')
text = response.json()['activity']


API_Key = '4A2F647477707A5961453373694D586A6A4E7A48724D625534706C45536348716A2B457A633350432F306B3D'
url = 'http://api.kavenegar.com/v1/%s/sms/send.json' %API_Key
payload = {
    'sender': '10008663', 
    'receptor': '09221895840', 
    'message': 'Amir its %s day!!!' %text
    }
response = requests.post(url=url, data=payload)
print (response)