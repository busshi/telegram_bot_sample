import glob, subprocess, fnmatch, re
from glob import os
from api import sendMessage, sendSticker, kb, sendDice, deleteMessage

TG_NAME = os.environ['TG_NAME']
CHAT_ID = os.environ['CHAT_ID']
token = os.environ["BOT_TOKEN"]

def action(msg, dest, username, msg_id):
    content_type = 'text'
    message = msg['text']
    command = message.split(' ', 1)[0].lower()
    if command[0] == '/':
        command = command[1:]

    if len(message.split()) >= 2:
        args = " ".join(message.split()[1:])
        args = '"{}"'.format(args)
    else:
        args = ""

    print ('Message : {0}\nCommand : {1}\nContent-Type : {2}\nDest : {3}\nArguments : {4}'.format(message, command, content_type, dest, args))

######## Commands list #####
    script_list = [file.split('/')[-1][:-3] for file in glob.glob("scripts/*.sh")]
    nosh_list = [file.split('/')[-1] for file in glob.glob("scripts/[!sudoku]*[!h]")]
    cmd_list = ["🕳"]
    cmd_list.extend(script_list)
    cmd_list.extend(nosh_list)
    cmd_list = sorted(cmd_list)

####### Functions #######
    def menu(dest):
        keyboard = [cmd_list[i:i + 3] for i in range(0, len(cmd_list), 3)]
        keyboard = '{}'.format(keyboard).replace('\'','"')
        kb (dest, "🔽 Available commands 🔽", keyboard, 'keyboard', 'mute')
        deleteMessage (dest, msg_id)
        deleteMessage (dest, msg_id-1)

    def forbiddenAction(dest, username, command):
        sendMessage (dest, "⛔️")
        sendSticker (dest, 'CAACAgIAAxkBAAJKIV7GVm1qWHPOA7AJ-OzdDZaYdIotAAJ9AAP3AsgPLsm7Ct3LIkkZBA')
        sendMessage (chat_id, '⛔️ Command [{0}] asked by {1} ⛔️'.format(command, username))


####### Commandes #######

### Menu ###
    if command == 'help' or command == 'menu' or command == '🔙':
        menu (dest)

    elif command == '🕳':
        kb (dest, '✅', 'noKb', 'remove_keyboard', 'mute')
        deleteMessage (dest, msg_id)
        deleteMessage (dest, msg_id+1)


### sh list ###		 ==> FOR SCRIPTS WITH ARGUMENTS
    elif command in script_list:
        subprocess.check_call(["scripts/{0}.sh {1} {2} {3}".format(command, dest, token, args)],shell=True)


### nosh_list ###	MEANING SCRIPTS WITHOUT EXTENSION .sh ===> FOR CALLBACK QUERY
    elif command == 'holidays':
        keyboard = '[[%7B"text":"A","callback_data":"zoneA"%7D,%7B"text":"B","callback_data":"zoneB"%7D,%7B"text":"C","callback_data":"zoneC"%7D]]'
        kb (dest, 'Wich zone ?', keyboard, 'inline_keyboard', 'mute')


### No script list
    elif command == '🎲':
        sendDice (dest, '🎲')

    else:
        sendMessage (dest, "❓ Unknown command ❓")
        menu (dest)
