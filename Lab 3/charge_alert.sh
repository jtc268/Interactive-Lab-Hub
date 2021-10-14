

python3 charge_alert_gyro.py

sleep 2
espeak -ven+f2 -k5 -s150 --stdout  "It sounds like you're getting ready to go. Would you like me to charge your laptop battery to full?" | aplay
arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav

python3 charge_alert_listener.py recorded_mono.wav

espeak -ven+f2 -k5 -s150 --stdout  "Charging your laptop battery to full." | aplay
