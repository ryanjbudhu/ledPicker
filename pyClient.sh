#!/bin/bash

cd LED_programs/RPi
j="off"
pid=99999
sleeptime=5
while true; do
	i=$(curl -s https://web.njit.edu/~rjb57/RPi/optionPicked.php)
	echo $i
	if [[ "$j" != "$i" ]]; then
		if [ $pid -lt 99998 ]; then
			echo "Killing $pid"
			sudo kill $pid
		fi
		j=$i
		if [[ "$j" == "off" ]]; then
			sleeptime=10
		else
			sleeptime=5
		fi
		sudo python3 pullRequest.py $j &
		pid=$!
	fi
	sleep "$sleeptime"
done
