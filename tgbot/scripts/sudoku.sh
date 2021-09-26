#!/bin/bash

Dest="$1"
token="$2"

sudoku()
{
a1=$( echo "$1" | cut -d" " -f1 )
a2=$( echo "$1" | cut -d" " -f2 )
a3=$( echo "$1" | cut -d" " -f3 )
a4=$( echo "$1" | cut -d" " -f4 )
a5=$( echo "$1" | cut -d" " -f5 )
a6=$( echo "$1" | cut -d" " -f6 )
a7=$( echo "$1" | cut -d" " -f7 )
a8=$( echo "$1" | cut -d" " -f8 )
a9=$( echo "$1" | cut -d" " -f9 )

x=0
scripts/sudoku/sudoku_solver "$a1" "$a2" "$a3" "$a4" "$a5" "$a6" "$a7" "$a8" "$a9" | while read line ; do
	grid+="$line\n"
	x=$(( $x + 1 ))
	if [ "$x" -eq 14 ] ; then
		grid=$( echo -e "$grid" )
		curl -s --data 'chat_id='$Dest --data-urlencode 'text='"$grid" 'https://api.telegram.org/bot'$token'/sendMessage' &> /dev/null
		grille=""
		x=0
	fi
done
}

if [ -n "$3" ] ; then
	sudoku "$3" &
	sleep 10 && killall -9 "sudoku.sh" "sudoku_solver"
else
	curl -s --data 'chat_id='$Dest --data-urlencode 'text='" " 'https://api.telegram.org/bot'$token'/sendMessage' &> /dev/null
	curl -s --data 'chat_id='$Dest --data-urlencode 'text='"Usage: Copy back each line separated with a space. Put a dot (.) instead of the empty boxes... For example:" 'https://api.telegram.org/bot'$token'/sendMessage' &> /dev/null
	curl -s --data 'chat_id='$Dest --data-urlencode 'text='"sudoku 9...7.... 2...9..53 .6..124.. 84...1.9. 5.....8.. .31..4... ..37..68. .9..5.741 47......." 'https://api.telegram.org/bot'$token'/sendMessage' &> /dev/null
fi

exit 0
