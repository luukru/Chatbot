# basic telegram bot
# https://www.codementor.io/garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay
# https://github.com/sixhobbits/python-telegram-tutorial/blob/master/part1/echobot.py

import json 
import requests
import time
import urllib
import CartmanBot
import urllib

TOKEN = "592338204:AAHtLQqd4cxqg_qdctQjekjDdCj0AsI_wyI" # don't put this in your repo! (put in config, then import config)
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text) # (python3)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    last_update_id = 438765863
    bot = CartmanBot.CartmanBot()
    print("\nReady to receive messages...\n")
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            for update in updates['result']:
                # Get the update and which chat it is from.
                print(update)
                message = update['message']
                chat = message["chat"]["id"]
                print('Chat: {}'.format(chat))
                
                # If a new member joins group with CartmanBot or new group is started.
                if 'new_chat_members' in message.keys() or 'group_chat_created' in message.keys():
                    greeting = bot.send_greeting()
                    send_message(greeting, chat)
                elif 'text' in message.keys():
                    text = message["text"]
                    print('Text: {}'.format(text))
                    # User starts hat with CartmanBot
                    if (text == '/start'):
                        greeting = bot.send_greeting()
                        send_message(greeting, chat)
                    # User types something to CartmanBot
                    else:
                        reply = bot.generate_reply(text)
                        print('Reply: {}'.format(reply))
                        send_message(reply, chat)
            
        time.sleep(0.5)


if __name__ == '__main__':
    main()
