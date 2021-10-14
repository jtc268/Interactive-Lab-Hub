
Testing voice greeting with Pi:
https://github.com/jtc268/Interactive-Lab-Hub/blob/Fall2021/Lab%203/pi_greeting_lab_3.sh

Shell script that asks how many pets the user has and records the count:
https://github.com/jtc268/Interactive-Lab-Hub/blob/02f3cb47fe3dbe45f57321387b222c414b99ddcf/Lab%203/pet_question.sh

Python program that runs the interation:
https://github.com/jtc268/Interactive-Lab-Hub/blob/cd7af297bff0b1b6e17fe8d95cc2a7a9226d9619/Lab%203/test_words_pet.py

### Storyboard and research

Research shows that keeping your laptop battery at 80% charge prolongs the life and capacity of the battery. When the laptop is sitting at home for prolonged period, it should only be charged to 80%. Apple has adopted this methodology as default for all mac laptops running the latest operating system. Remembering when to charge the laptop to full before an event can be difficult since charging from 80-100% takes about an hour. You need to think in advnace. Using sound / voice confirmation for the reminder and interaction to charge the laptop feels like an appropriate use of the sound/voice interaction medium. If you're busy with something else (say showering, or getting dressed) you either won't remember, or won't have time to engage directly with your laptop to "charge to full". The computer would check your calendar to see if you had any events coming up and ask if you'd like your laptop charged to full while you're getting ready to go. This would maximize the effectiveness of Apple's battery preservation feature while also maximizing the utility of a full battery when needed. Since the user is asked if they want to charge t, say, 1 hour before a calendar event, they would have the option to say "No" if they were attending via zoom. (therefore remaining plugged in)

![image](https://user-images.githubusercontent.com/89586838/135945070-53f0fe37-5de5-4b18-8520-fd9df2ebdbb7.png)

Imagined Diagloue:

Scenario 1:

Computer: You have an event in 1 hour, your laptop is currently 80% charged. Should I charge to full?

Human: Yes

Computer: Charging to full now.

Scenario 2:

If human says "No"

Computer: Okay.

\*\***My process included finding a real user pain point before thinking about if voice/sound could help solve the problem. I found many voice interaction ideas to be annoying for the user. Generally I found myself feeling that if a computer is going to start talking, it better be extremely useful. You risk a feature becoming very annoying for a user if a real problem isn't being solved. The majority of my ideas felt gimmicky until I landed on the laptop battery charge problem. Apple introduced a feature without enough options/support. Someone with a busy lifestyle may be left with a partially charged battery when they need a full charge the most.**\*\*

### Acting out the dialogue

Zoom recording to test the interaction:

https://youtu.be/4cKgaBUcMus

\*\***The dialogue was different than I expected. The respndent say "Yeah, sure." instead of the expected "Yes" or "No" and I know I will have to add some extra vocabulary to the response validation code. I also didn't expect the respondent to say "thanks". I may consider adding "you're welcome" before the response saying "Charging to full now". I was glad that the respondent understood the prompt and wanted their battery charged.**\*\*

# Lab 3 Part 2

**Reflection**

I reflected on the interaction and feedback and decided that reminding the user to charge a laptop battery by calendar events wouldn't be a reliable trigger for this function. If someone just has a zoom calendar event, they don't want a voice assistant to ask them to charge their battery, since they will be staying home. I thought about signals within a house that would tell a computer when a user is officialy "leaving" to go somewhere else about 40 minutes before it happened. 4- minutes is about the time it takes to charge a laptop battery from 80% to 100%. One thing I usually do before leaving the house is shower. If I could detect when the user is showering, I could ask them if they want to charge their laptop battery to full. (Remember, the battery % on an apple laptop at home, plugged in, is always at 80% to preserve the battery per Apple defaults)

**New storyboard:**

1. User is in a rush and needs to get to campus for class
2. The user frequently forgets to charge laptop battery to full, since the Apple default is to "hold" the battery at 80% while plugged in at home. This is annoying since the user needs fully battery power for class!
3. User need to shower before they leave, and it takes some time to get ready after that
4. User closes shower curtain
5. Voice assistant: "It sounds like you're getting ready to go. Would you like me to charge your laptop battery to full?"
6. User: "Yes!"
7. Voice assistant: "charging battery to full now"
8. User is happy :) and feels prepared

I need to figure out how to detect if a shower curtain is closed. I detrmined a gyro sensor would be appropriate for this job if I could attach the gyro or Pi to the shower curtain.

**Gyro setup**

My goal is to detect movement of a closed shower curtain.

I used the Adafruit MPU-6050 6 DoF Accel & Gyro Sensor and connected it to a Raspberry Pi via stemma QT connector and cable through the SparkFun Qwiic OLED Display. (already installed) I then installed libraries on my Pi via https://github.com/adafruit/Adafruit_CircuitPython_LSM303_Accel. Running the "Usage Example" then provided the gyro readings. I rubber banded the gyro onto my Pi case and attached the entire device to the shower curtain, as shown below.

![image](https://user-images.githubusercontent.com/89586838/137240644-880e6a51-1f07-4420-b856-86f80508bea0.png)


**Documentation: Data Interpretation and Usage**

The first time taking data from the gyro, I was not familiar with tuples. I had to look this up and now I understand how to select which axis from the gyro I'd like to read and calculate against. (e.g. x, y, and z axis on gyro for acceleration would equal 0,1, or 3 in a tuple)

With my girlfriend Jennie's help to wizard the interaction (thanks for the help!) one monitored the gyro readings and the other opened and closed the shower curtain to determine which axis on the gyro would determine a "close". I landed on the code below to detect a "close". It worked quite well. The x-axis would drop below 1 when the curtain accelerated to the closed position.

![image](https://user-images.githubusercontent.com/89586838/137240680-ac991d9b-7fcc-4317-94e9-b7df07f2ec98.png)

Next, it was time to set up the shell script to run in the following sequence:

	1. Shower curtain closed (detected by gyro)
	2. Speaker asks if you want to charge laptop battery - "It sounds like you're getting ready to go. Would you like me to charge your laptop battery to full?"
	3. Speaker listens and records for positive affirmation
	4. User says "Yes"
	5. "Charging your laptop battery to full."

The end result of the shell script is below:

python3 charge_alert_gyro.py
sleep 2
espeak -ven+f2 -k5 -s150 --stdout  "It sounds like you're getting ready to go. Would you like me to charge your laptop battery to full?" | aplay
arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
python3 charge_alert_listener.py recorded_mono.wav
espeak -ven+f2 -k5 -s150 --stdout  "Charging your laptop battery to full." | aplay

Through acting out the interaction, I learned that I needed to put a wait step e.g. "sleep 2" after the shower curtain closed, otherwise the user wouldn't be able to hear the message. The message started playing as the shower curtain was closing, and the shower curtain made a loud sound. It was best to wait until the user finished closing the curtain so they could hear the message.

For the speech listener, I didn't know how to read the format and figured out it was JSON. Ihen figured out how to parse the JSON and that was successful. Now I can trigger more conversational elements from my shell script.

**Here is a video showcasing the pain point and use case for the device.**

https://www.youtube.com/watch?v=R6AoLRRHxrQ

### What worked well about the system and what didn't?
\*\**The gyro sensor worked much better than expected to measure if a shower curtain has closed or moved. I was delighted by this sensor. The voice assistant was not loud enough and sometimes felt slower than something like an Alexa or Google home voice assistant. The power cable needed for the Pi was dargging around on the floor by the shower and I feel this could be improved.*\*\*

### What worked well about the controller and what didn't?

\*\**Overall the voice controller was great and easy to develop on. It made it easy to alert a user and then take commands on actions for next steps. After the controller listens, to respond it felt a little slow. The words the controller heard weren't always exact, e.g. "yea" versus "yes". This caused a deeper dictionary build out and matching system for what I called a "positive affirmation" in this project.*\*\*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**THere are always more nuanced signals to pick up on from a user at home if you are trying to cater to their life. They have many habits and home interactions that can be detected. Wizarding allows you to see how users are acting in the moment so you can adjust sensors, timings, and what the bot actually says to intengrate more tightly into their life. This is very important for voice interactions since they can be very annoying or not helpful.*\*\*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**My system could be expanded upon to pick up on flags when a user is about to leave the house. If we know when the user is getting ready to leave, many systems can be triggered to make sure they don't forget items, forget to charge their batteries, forget to turn the oven off, etc. I would add a temperature sensor near the oven to detect high ambient temperature and ask the user if they'd like to turn the oven off since they're getting ready to leave the house. *\*\*
