import os, subprocess, urllib
from api import sendMessage,answerCallbackQuery, kb, editKb, editMessageText, deleteMessage

token = os.environ["BOT_TOKEN"]

def callbackQuery(rep_id, rep, dest, msg_id, user):
    print ('Callback_query: {0} - {1}'.format(rep_id, rep))

    if rep[:4] == 'zone':
        zone = rep[4]
        cbtxt = 'Looking for French holidays for the zone {}'.format(zone)
        subprocess.check_call(["scripts/holidays {0} {1} {2}".format(dest, zone, token)], shell=True)
        deleteMessage (dest, msg_id)

    elif rep == 'done':
        cbtxt = "🗑  Deleting recents... 🗑"
        deleteMessage (dest, msg_id)

    elif rep == 'nada':
        cbtxt = 'You already clic on it...'

    if 'cbtxt' in locals():
        answerCallbackQuery (rep_id, cbtxt)
