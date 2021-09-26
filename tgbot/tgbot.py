#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests, os, urllib.request
from api import unknownUser, sendMessage, sendNotif, sendSticker, sendDice
from command import action
from callbackQuery import callbackQuery

api = 'https://api.telegram.org/bot{}'.format(os.environ['BOT_TOKEN'])
chat_id = os.environ["CHAT_ID"]
tg_name = os.environ["TG_NAME"]

def parse(msg, content, dest, user):
    print ('Content-Type : {}'.format(content))
    if content == 'text':
        msg_id = msg['message_id']
        action (msg, dest, user, msg_id)

    elif content == 'sticker':
        sticker = msg['sticker']['file_id']
        sendSticker (dest, sticker)

    elif content == 'dice':
        dice = msg['dice']['emoji']
        sendDice (dest, dice)

    elif content == 'answerCallbackQuery':
        msg_id = msg['message']['message_id']
        rep = msg['data']
        rep_id = msg['id']
        callbackQuery (rep_id, rep, dest, msg_id, user)

    else:
        sendDice (dest, '🎲')


def getContent(res):
    print (res)

    try:
        msg = res['message']
    except KeyError:
        try:
            msg = res['callback_query']
            content = 'answerCallbackQuery'
        except KeyError:
            try:
                msg = res['poll_answer']
                content = 'poll_answer'
            except KeyError:
                msg = res
                content = 'unknown'


    if 'msg' in locals():
        print('msg:')
        print (msg)


    if 'text' in msg:
        content = 'text'
    elif 'sticker' in msg:
        content = 'sticker'
    elif 'dice' in msg:
        content = 'dice'

    try:
        dest = msg['from']['id']
    except KeyError:
        try:
            dest = msg['user']['id']
        except KeyError:
            dest = " "
    print('dest:')
    print (dest)

    try:
        user = msg['from']['username']
    except KeyError:
        try:
            user = msg['user']['username']
        except KeyError:
            user = " "
    print('user:')
    print (user)

    if (user == tg_name) and ('content' in locals()):
        parse (msg, content, dest, user)
        print ('[OK]')

    else:
        if not 'content' in locals():
            content = 'unknown'
        if not dest == ' ':
            unknownUser (msg, content, dest, user)


def main():
    offset = 0
    getUpdates = '{}/getUpdates'.format(api)
    print ('Telegram Bot running... Waiting for commands...')

    while True:
        data = dict(offset=offset, timeout=60)
        try:
            req = requests.post(getUpdates, data=data, timeout=None).json()
        except ValueError:
            continue

        if not req['ok'] or not req['result']:
            continue

        for res in req['result']:
            try:
                getContent (res)
            except urllib.error.HTTPError:
                err_msg = '[KO] HTTP Error => offset + 1'
                print (err_msg)
                sendMessage (chat_id, err_msg)
            except:
                err_msg = '[KO] Error => offset + 1'
                print (err_msg)
                sendMessage (chat_id, err_msg)

            offset = res['update_id'] + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ('Stopping bot in progress...')
        exit()

