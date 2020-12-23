#!/bin/sh

BASE="/home/radio/trunk-player"
LOG="$BASE/logs/add_audio.log"

echo "load_audio.sh args: $1 - $2" >> $LOG
cd $BASE/
. $BASE/env/bin/activate
./manage.py add_transmission $1 --web_url=$2 >> $LOG 2>&1

