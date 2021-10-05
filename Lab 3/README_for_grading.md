
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
https://youtu.be/700MsZwSrlE

\*\***The dialogue was different than I expected. The respndent say "Yeah, sure." instead of the expected "Yes" or "No" and I know I will have to add some extra vocabulary to the response validation code. I also didn't expect the respondent to say "thanks". I may consider adding "you're welcome" before the response saying "Charging to full now". I was glad that the respondent understood the prompt and wanted their battery charged.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
3. Make a new storyboard, diagram and/or script based on these reflections.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*

### What worked well about the controller and what didn't?

\*\**your answer here*\*\*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**your answer here*\*\*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*
