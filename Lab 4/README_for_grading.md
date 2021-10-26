# Ph-UI!!!

All sensors are tested and working! Daisy chaining all of the sensors together was delightfully easy.

![image](https://user-images.githubusercontent.com/89586838/137832490-bd844bca-8504-41bb-a6bb-a47d12d7c869.png)


### Part C
### Physical considerations for sensing

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***

![IMG-0022](https://user-images.githubusercontent.com/89586838/137832168-539fb7be-c90c-4c24-baf6-2f78f272dda4.jpg)
![IMG-0023](https://user-images.githubusercontent.com/89586838/137832197-8641af2f-f854-40a2-8752-6af47a77bf8b.jpg)

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

I found myself asking how the sensors would be mounted and how they would be positioned to collect accurate data. For exmaple, to measure how many "cheeses" were left in the cheese dispenser (sketch 2), I figured using distance from the top of the cheese stack would be easiest to increment the amount of cheeses that have gone missing. Then I would subtract that distance from the total of the maximum cheese stack to create a cheese counter. In Sketch 3, the jar filling detector, I realized I would not only need sensor to test if the jar was full, but I would need a way to turn off the faucet once done. I scrapped this idea since I didn't have a way of turning off the faucet. I also would need to test if the motion direction sensor would be able to detect water flowing upward in a clear container. Design 5 raised the question if a foil wrapped container would work with the capacative sensor. I tested this "key drop" interaction with just foil before moving forward with the idea as shown in the video below.

https://youtu.be/J8uYPUukQi4

The keys successfully tripped the capacitive sensor!

**\*\*\*Pick one of these designs to prototype.\*\*\***

Design 5 shows an item collector using the capacitive touch sensor, which indicates with red or green light if the item is in the "basket". I chose design 5 to move forward with because it seemed the most useful on a day-to-day basis. Design 5 will help me to keep track of items I need every day, like keys and airpods.

### Part D
### Physical considerations for displaying information and housing parts
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

![IMG-0024](https://user-images.githubusercontent.com/89586838/137832254-98226bb4-1e2a-401d-9120-b9afdf6bb83e.jpg)
![IMG-0025](https://user-images.githubusercontent.com/89586838/137832259-19c70d9b-e83a-48a0-ace4-55cb955a4bdc.jpg)
![IMG-0026](https://user-images.githubusercontent.com/89586838/137832265-8156c33d-07d9-4373-8c7c-84e6b6944b50.jpg)

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to answer those questions?\*\*\***

- Do I really need light on the screen to display if items are there or not? 
- What happens if the indicator for "item present" is opposite if I code the system to toggle the state? 
- Would I need a button to reset the state? What if my items aren't in the baskets before bedtime? 
- Should I add a speaker to let the user know to find their items before bed in case they lost something during the course of a day? What if the user can't see the items in the baskets? 
- Would they need a light indicator then to know for sure? What if light indicators are useless? 

I need to physically prototype the position of the basket inside or outside the box as well as the screen position. This way I can interact with the device to see which features may be neccessary.

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

I ultimately chose display design number 1 to integrate into my physical prototype.

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

The size of the device is based on how many items I need to remember to put away each day. If I lose track of a few key items (including keys and airpods) I cannot leave the house. I figured the device can be less than a foot wide for these small items and sit on top of a desk. The baskets that hold items need to sense when the items are dropped and be highly accessible for dropping/grabbing interactions. When standing further away from the device to check if items are present or not, the screen would have to be on the SIDE of the device (not the top). Using 50% of the screen to display basket status (red/green) felt like it'd be visible from across the room if I wanted to check if my items are stored properly. Sometimes the itmes would drop below the basket walls e.g. keys, and the indiciator light would remind me that the keys are there.

Build a cardbord prototype of your design.

**\*\*\*Document your rough prototype.\*\*\***

Pictures of prototype

![image](https://user-images.githubusercontent.com/89586838/137835501-79ea6e1e-126c-400d-8cb3-c3fd02ccbe75.png)

![image](https://user-images.githubusercontent.com/89586838/137835470-a5fc4ec8-a39b-42be-8631-632c01164978.png)

![image](https://user-images.githubusercontent.com/89586838/137835447-40f1989f-b620-411b-a08f-64c8b248a9b9.png)

### Video of the interaction with cardboard prototype
https://youtu.be/Tuscs7qTD1E


LAB PART 2

### Part F
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:

Alternative design sketches:
![image_6487327 (2)](https://user-images.githubusercontent.com/89586838/138789271-51e08f03-52a4-4bc7-895f-656da2292be4.JPG)

### "Looks like": shows how the device should look, feel, sit, weigh, etc.

Committing to Idea 5 from Part 1, and optimizing the design. Diving into continued prototyping! I didn't like the alternative ideas as much since they lacked function. I would like a device that helps with my day to day life.

![image_6487327 (1)](https://user-images.githubusercontent.com/89586838/138789279-fa4a2f5c-26f3-463e-8988-6f092d14f022.JPG)
![image_6487327](https://user-images.githubusercontent.com/89586838/138789284-df40c576-9d88-423c-91c8-f2e0dd3d68f8.JPG)

Work in progress is shown below to recess the "bins", move screen to the top, and turn the device black since it needs to be more aesthetically pleasing than a cardboard box. This device is something that will sit in the home, out in the open.

Progress pictures:

![20211025_202646](https://user-images.githubusercontent.com/89586838/138790447-3ffe1af8-dd9e-4ba1-9a20-67e759cb6a47.jpg)
![20211025_202657](https://user-images.githubusercontent.com/89586838/138790448-6bef38f5-5a4a-4cd6-a8c3-61acacadc18b.jpg)

Final form before powered on:

![image](https://user-images.githubusercontent.com/89586838/138800483-1b77a397-33f9-443e-9683-6c80b979cf1f.png)
![image](https://user-images.githubusercontent.com/89586838/138800538-378f0fef-95f6-43bd-a3b6-caf4a1662443.png)


Visual change log, internals:

![image](https://user-images.githubusercontent.com/89586838/138790528-0ca1312e-62d2-458c-af23-2c720abd1f8e.png)

Testing capacitive sensors in new box design with key drops:
https://youtu.be/prOnuft0rPQ

### "Works like": shows what the device can do

Various states of the device:
- Light OFF indicates item is in bin - user responsibility is complete
- Light ON indicates item is **not** in bin - indicates the user has not completed their responsibility to stay organized. This is like a notification to complete a task.

Examples of states:
![image](https://user-images.githubusercontent.com/89586838/138798042-a94b964c-9a57-48cd-b952-1118b5c38d29.png)
![image](https://user-images.githubusercontent.com/89586838/138798165-1af20344-672d-48fb-834b-9d4972447d0e.png)
![image](https://user-images.githubusercontent.com/89586838/138798064-a59347c8-dfd6-4f92-a749-089cae2fb763.png)
![image](https://user-images.githubusercontent.com/89586838/138798894-c032dec5-8b2c-4d94-a200-ace31273261f.png)

### Final interactions ("Acts like")

### Removing keys: https://youtu.be/NcZUdo75FOk
- Light is on triggering the user to take care of there disorganization problem. Put your things where they belong!

### Adding keys: https://youtu.be/ibrr9OlsYwg
- Lights go out per bin. This is satisfying for the user.

### "Lights out" Program
- Capacitive sensors trigger lights to toggle on/off on 50% of the OLED screen.
- https://github.com/jtc268/Interactive-Lab-Hub/blob/Fall2021/Lab%204/lights_out.py

In the future, I may make the lights blink to indicate more urgency for the user to get organized. A blinking light is annoying and the user will want to turn it off only by putting their things away.

### Some issues worth noting:

- I had overclocked my raspberry pi and running in the box, it frequently hit 80C. Outside of the box it was always under 70C. Noting to underclock the Pi for such applications inside enclosures.
- The capacitive touch sensors don't always work consistently with key drops. Adjusting the insulating layer of cardboard inside the box did help with cross talk. However, key drops and removals still weren't perfectly consistent. (or trigger was too sensitive) See blooper reels below!
  -  Blooper 1 https://youtu.be/tR5WC_N6n9s
  -  Blooper 2 https://youtu.be/3hxXqPuFrto





