import requests
import time


url='https://api.telegram.org/bot'
token='8111643516:AAEHWfdahTAy7Kp3gI9_zTcI6gFZVTWWw4o'
cats_url='https://api.thecatapi.com/v1/images/search'
error_text='try again pls'

max_counter=10
offset=-2
counter=0
cat_response: requests.Response
cat_link:str
chat_id=1794031398


while counter<max_counter:
    print('attempt =', counter)

    updates = requests.get(f'{url}{token}/getUpdates?offset={offset +1}').json()

    if updates['result']:
        for result in updates['result']:
            offset=result['update_id']
            #chat_id=result['message']['from']['id']
            cat_response=requests.get(cats_url)
            if cat_response.status_code==200:
                cat_link=cat_response.json()[0]['url']
                requests.get(f'{url}{token}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={error_text}')
    time.sleep(1)
    counter +=1