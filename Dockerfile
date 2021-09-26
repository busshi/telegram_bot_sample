FROM		ubuntu:latest

RUN			apt-get update && apt-get install -y python3-pip curl clang xxd jq && pip3 install requests

RUN 		useradd -d /home/tgbot -m -s /bin/bash tgbot

WORKDIR		/home/tgbot

COPY		tgbot/ .

RUN			chown -R tgbot:tgbot /home/tgbot

USER		tgbot

RUN			cd scripts/sudoku && make

ENTRYPOINT	[ "python3", "tgbot.py" ]
