import time
import requests
import telegram
from dotenv import load_dotenv 
import os


load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
TOKEN = os.getenv('TOKEN')



def get_status(user_id):
    params = {
        'access_token':TOKEN,
        'user_ids':user_id,
        'v':'5.120',
        'fields':'online'
    }
    response = requests.post('https://api.vk.com/method/users.get', params=params)
    return response.json()['response'][0]['online']

def send_message(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    return bot.send_message(chat_id=CHAT_ID, text=message)


if __name__ == "__main__":
    vk_id = 'id3003609'
    while True:
        if get_status(vk_id) == 1:
            send_message(f'Ира {vk_id} сейчас онлайн!')
            time.sleep(100)
            continue
        else:
            time.sleep(100)
            continue
    
