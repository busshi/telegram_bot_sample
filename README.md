# TELEGRAM BOT


__Usage:__
- make
- make stop (stop containers)
- make clean (clean everything)
- make fclean (stop containers before cleaning)
- make re (clean and make again)


It will run inside a Docker container. Don't forget to change the variables in the Makefile :
- BOT_TOKEN: your bot token (you can create one with Bot Father inside the Telegram app)
- TG_NAME: your telegram name (pseudo)
- CHAT_ID: your chat instance (find it here: https://api.telegram.org/bot${BOT_TOKEN}/getUpdates)


__[Telegram API](https://core.telegram.org/bots/api)__


With this bot, 3 examples of commands are available:
- help/menu: show availables commands
- sudoku: run the sudolu solver
- holidays: show holidays in France (Zone A/B/C)


You can create more scripts and add them in the scripts directory:
- *.sh: scripts to run with arguments
- scripts without the extension .sh: scripts to run without arguments


It is uo to you to add more... Have fun ;)
