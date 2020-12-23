#!/bin/sh
# Wrapper script to import new audio files into trunk-player
# * Encode the wav files into mp3
# * If the wav is from an analog TG increase the volume to match the digital groups
# * Upload the new mp3 to amazon s3
#
# Dylan Reinhold dreinhold@gmail.com
#--------------------------------------------------------------------------

BASE_DIR="/home/radio/trunk-player"
AUDIO_DIR="/trunk-player-audio"
LOG="$BASE_DIR/logs/encode.log"

. $BASE_DIR/env/bin/activate

basename="$1"
folder="$2"
filename="$basename.wav"
mp3encoded="$basename.mp3"
json="$basename.json"
echo "\nSanity Check: $1 ->  $filename -> $mp3encoded + $json -> $folder / $2" >> $LOG	#printf "%s" "$(<$basename)"
#echo "$basename : `date` encode $basename" >> $LOG
#echo "$basename : `date` digital" >> $LOG

if [ ! -f "$BASE_DIR/audio_files/$filename" ]
then 
	return 0
else
	ffmpeg -i "$BASE_DIR/audio_files/$filename" -codec:a mp3 -b:a 24k -hide_banner -loglevel quiet -cutoff 8000 "$BASE_DIR/mp3_files/$mp3encoded" >> $LOG
	sleep 1
		if [ ! -f "$BASE_DIR/mp3_files/$mp3encoded" ] 
		then
			echo "ERROR: FILE DOES NOT EXIST: $AUDIO_DIR/audio_files/$mp3encoded - ENCODING AGAIN"
			sleep 2
			ffmpeg -i "$BASE_DIR/audio_files/$filename" -codec:a mp3 -b:a 24k -hide_banner -loglevel info -cutoff 8000 "$BASE_DIR/mp3_files/$mp3encoded" >> $LOG
			sleep 1
		fi
sleep 1

mkdir -p $AUDIO_DIR/audio_files/$folder
mv $BASE_DIR/mp3_files/$mp3encoded $AUDIO_DIR/audio_files/$folder/$mp3encoded -f
#$BASE_DIR/trunk-player/utility/trunk-player/upload_to_s3_delete.py $BASE_DIR/audio/$mp3encoded $S3_BUCKET >> $LOG 2>&1
# /home/radio/trunk-player/ utility/trunk-player
$BASE_DIR/utility/trunk-player/load_audio_file.sh $basename $folder
rm -f $BASE_DIR/audio_files/$filename

fi
