import requests
import time
url='http://api.telegram.org/bot'
token='8111643516:AAEHWfdahTAy7Kp3gI9_zTcI6gFZVTWWw4o'
text='hello'
max_counter=10

offset=-2
counter=0
#chat_id:int
chat_id=1794031398
while counter<max_counter:
    print('attempt =', counter)

    updates = requests.get(f'{url}{token}/getUpdates?offset={offset +1}').json()
    if updates['result']:
        for result in updates['result']:
            offset=result['update_id']
            #chat_id=result['message']['from']['id']
            requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}')
    time.sleep(1)
    counter +=1