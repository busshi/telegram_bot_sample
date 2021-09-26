import random, os, requests, urllib.request, subprocess
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen


token = os.environ['BOT_TOKEN']
api = 'https://api.telegram.org/bot{}'.format(token)
chat_id = os.environ["CHAT_ID"]


def sendMessage(dest, txt):
    url = '{}/sendMessage'.format(api)
    data = dict(chat_id=dest, text=txt, disable_notification=True)
    requests.post(url, data=data).json()


def sendNotif(dest, txt):
    url = '{}/sendMessage'.format(api)
    data = dict(chat_id=dest, text=txt, disable_notification=False)
    requests.post(url, data=data).json()


def deleteMessage(dest, msg_id):
    url = '{}/deleteMessage'.format(api)
    data = dict(chat_id=dest, message_id=msg_id)
    requests.post(url, data=data).json()


def sendSticker(dest, sticker):
    url = '{}/sendSticker'.format(api)
    data = dict(chat_id=dest, sticker=sticker, disable_notification=True)
    requests.post(url, data=data).json()


def sendDice(dest, dice):
    url = '{}/sendDice'.format(api)
    data = dict(chat_id=dest, emoji=dice, disable_notification=True)
    requests.post(url, data=data).json()


def unknownUser(msg, content, dest, user):
    try:
        txt = msg['text']
    except KeyError:
        txt = 'empty message'

    smileyList = ["🎲","😎", "🤪", "🤫", "🤑", "👻", "💩", "🦾", "👀", "🍆", "🍾", "🥇"]
    smiley = random.choice(smileyList)
    sendMessage (dest, smiley)
    try:
        last = msg['from']['last_name']
    except KeyError:
        last = ""

    try:
        first = msg['from']['first_name']
    except KeyError:
        first = msg['user']['first_name']

    sendMessage (chat_id, "🚨 Unknown user attempting to control the bot 🚨")
    sendMessage (chat_id, "Pseudo [@{0}]\nName [{1}]\nFirstname [{2}]\ndest [{3}]\nMessage [{4}]\nContent-Type [{5}]".format(user, last, first, dest, txt, content))


def kb(dest, txt, keyboard, markup, extra):
    keyboard = {" ":keyboard}
    keyboard = urlencode(keyboard, quote_via=quote_plus, safe='%')[2:]
    txt = {"text":txt}
    txt = urlencode(txt, quote_via=quote_plus)

    if extra == 'mute':
        mute = 'disable_notification=true'

    else:
        mute = 'disable_notification=false'

    if markup == 'keyboard':
        url = '{0}/sendMessage?chat_id={1}&{2}&{3}&reply_markup=%7B"{4}":{5},"resize_keyboard":true%7D'.format(api, dest, txt, mute, markup, keyboard)

    elif markup == 'inline_keyboard':
        url = '{0}/sendMessage?chat_id={1}&{2}&{3}&reply_markup=%7B"{4}":{5}%7D'.format(api, dest, txt, mute, markup, keyboard)

    elif markup == 'remove_keyboard':
        url = '{0}/sendMessage?chat_id={1}&{2}&{3}&reply_markup=%7B"{4}":true%7D'.format(api, dest, txt, mute, markup)

    r = urllib.request.urlopen(url).read()



def editKb(dest, keyboard, msg_id):
    keyboard = {" ":keyboard}
    keyboard = urlencode(keyboard, quote_via=quote_plus, safe='%')[2:]
    msg_id = {"message_id":msg_id}
    msg_id = urlencode(msg_id, quote_via=quote_plus)
    url = '{0}/editMessageReplyMarkup?chat_id={1}&{2}&reply_markup=%7B"inline_keyboard":{3}%7D'.format(api, dest, msg_id, keyboard)
    r = urllib.request.urlopen(url).read()


def editMessageText(dest, keyboard, txt, msg_id):
    keyboard = {" ":keyboard}
    keyboard = urlencode(clavier, quote_via=quote_plus, safe='%')[2:]
    txt = {"text":txt}
    txt = urlencode(txt, quote_via=quote_plus)
    msg_id = {"message_id":msg_id}
    msg_id = urlencode(msg_id, quote_via=quote_plus)
    url = '{0}/editMessageText?chat_id={1}&{2}&{3}&reply_markup=%7B"inline_keyboard":{4}%7D'.format(api, dest, txt, msg_id, keyboard)
    r = urllib.request.urlopen(url).read()


def answerCallbackQuery(rep_id, txt):
    txt = urlencode({"text":txt}, quote_via=quote_plus)
    url = '{0}/answerCallbackQuery?callback_query_id={1}&{2}'.format(api, rep_id, txt)
    r = urllib.request.urlopen(url).read()
