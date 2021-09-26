BOT_TOKEN	= "PASTE_YOUR_BOT_TOKEN_HERE"

CHAT_ID		= "PASTE_YOUR_CHAT_ID_HERE"

TG_NAME		= "PASTE_YOUR_PSEUDO_HERE"

all:
	@docker build -t tgbot:latest .
	@docker run -d --rm -e BOT_TOKEN=$(BOT_TOKEN) -e TG_NAME=$(TG_NAME) -e CHAT_ID=$(CHAT_ID) tgbot

stop:
	@docker stop $$(docker ps -aq)

clean:
	@docker system prune --volumes --all --force

fclean:	stop clean

re:	clean all

.PHONY: all stop clean re
