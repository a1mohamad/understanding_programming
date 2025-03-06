import requests
from urllib import response
text = '''Happy New Year!!!
-Amir Askari'''
filename = './numbers.txt'
def read_phone(filename):
    with open(str(filename)) as h:
        content = h.readlines()
        content = [number.strip() for number in content]
        return content

def send_sms(number, text):
    API_Key = '4A2F647477707A5961453373694D586A6A4E7A48724D625534706C45536348716A2B457A633350432F306B3D'
    url = 'https://api.kavenegar.com/v1/%s/sms/send.json' %(API_Key)
    payload = {
        'sender' : '10008663',
        'receptor' : '%s' %(number),
        'message' : '%s' %(text),
    }
    response = requests.post(url=url, data=payload)
    return print(response)

phones = read_phone(filename)
for phone in phones:
    send_sms(phone, text) #we know Response 200 is OK!so with this method,
                          #we can debug our program better