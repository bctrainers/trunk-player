#!/bin/sh
# Change to your path
cd /home/radio/trunk-player

. env/bin/activate
ts=`date +%Y%m%d%H%M%S`

cp -f daphne.log logs/daphne.$ts.log
nohup daphne trunk_player.asgi:channel_layer --port 7055 --bind 0.0.0.0 > daphne.log 2>&1 &
d_pid=$!
cp -f runworker1.log logs/runworker1.$ts.log
cp -f runworker2.log logs/runworker2.$ts.log
cp -f runworker3.log logs/runworker3.$ts.log
cp -f runworker4.log logs/runworker4.$ts.log
cp -f runworker5.log logs/runworker5.$ts.log
cp -f runworker6.log logs/runworker6.$ts.log

nohup ./manage.py runworker --threads 16 > runworker1.log 2>&1 &
r1_pid=$!
nohup ./manage.py runworker --threads 4 > runworker2.log 2>&1 &
r2_pid=$!
nohup ./manage.py runworker --threads 4 > runworker3.log 2>&1 &
r3_pid=$!
nohup ./manage.py runworker --threads 4 > runworker4.log 2>&1 &
r4_pid=$!
nohup ./manage.py runworker --threads 4 > runworker5.log 2>&1 &
r5_pid=$!
nohup ./manage.py runworker --threads 4 > runworker6.log 2>&1 &
r6_pid=$!


echo "Started $ts" > running.pid
echo "daphne:$d_pid" >> running.pid
echo "runworker1:$r1_pid" >> running.pid
echo "runworker2:$r2_pid" >> running.pid
echo "runworker3:$r3_pid" >> running.pid
echo "runworker4:$r4_pid" >> running.pid
echo "runworker5:$r5_pid" >> running.pid
echo "runworker6:$r6_pid" >> running.pid
