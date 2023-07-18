import telegram
import requests

API_link = 'https://api.telegram.org/bot6265092148:AAENNgsiMnoUEYQcv2md5CIeHngSdAme76Y'

updates = requests.get(API_link + "/getUpdates?offset=-1").json()

print(updates)

message = updates['result'][0]['message']
chat_id = message['from']['id']
text = message['text']

sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Алоха")