# Ph-UI!!!

For lab this week, we focus on both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

### Start brasinstorming ideas by reading: 
* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). In this lab, we will continue to use the `circuitpython` virtual environment we created before. Activate `circuitpython` and `cd` to your Lab 4 folder to install the requirements by:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" width=200>

Connect it to your pi with Qwiic connector and try running the three example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python color_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separated breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">
<img src="https://cdn-shop.adafruit.com/970x728/4991-01.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick

A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### (Optional) Distance Sensor

Note: We did not distribute this sensor to you, so if you are interested in playing with it, please come pick it up from the TA!

Earlier we have asked you to play with the proximity sensor, which is able to sense object within a short distance. Here, we offer [Qwiic Multi Distance Sensor](https://www.sparkfun.com/products/17072), which has a field of view of about 25° and is able to detect objects up to 3 meters away! 

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/0/3/4/17072-Qwiic_Multi_Distance_Sensor_-_VL53L3CX-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python distance_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_VL53L1X_Py) to learn more about the sensor and see other examples!

All sensors are tested and working! It was great that you could daisy chain all of the sensors together.

![image](https://user-images.githubusercontent.com/89586838/137832490-bd844bca-8504-41bb-a6bb-a47d12d7c869.png)


### Part C
### Physical considerations for sensing

Usually, sensors need to positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.

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


Here is an Pi with a paper faceplate on it to turn it into a display interface:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>



This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibily be mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***
![IMG-0024](https://user-images.githubusercontent.com/89586838/137832254-98226bb4-1e2a-401d-9120-b9afdf6bb83e.jpg)
![IMG-0025](https://user-images.githubusercontent.com/89586838/137832259-19c70d9b-e83a-48a0-ace4-55cb955a4bdc.jpg)
![IMG-0026](https://user-images.githubusercontent.com/89586838/137832265-8156c33d-07d9-4373-8c7c-84e6b6944b50.jpg)

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to answer those questions?\*\*\***

Do I really need light on the screen to display if items are there or not? What happens if the indicator for "item present" is opposite if I code the system to toggle the state? Would I need a button to reset the state? What if my items aren't in the baskets before bedtime? Should I add a speaker to let the user know to find their items before bed in case they lost something during the course of a day? What if the user can't see the items in the baskets? Would they need a light indicator then to know for sure? What if light indicators are useless? 

I need to physically prototype the position of the basket inside or outside the box as well as the screen position. This way I can interact with the device to see which features may be neccessary.

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

I ultimately chose display design 1 to integrate into my physical prototype.

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

The size of the device is based on how many items I need to remember to put away each day. If I lose track of a few key items (including keys and airpods) I cannot leave the house. I figured the device can be less than a foot wide for these small items and sit on top of a desk. The baskets that hold items need to sense when the items are dropped and be highly accessible for dropping/grabbing interactions. When standing further away from the device to check if items are present or not, the screen would have to be on the SIDE of the device (not the top). Using 50% of the screen to display basket status (red/green) felt like it'd be visible from across the room if I wanted to check if my items are stored properly. Sometimes the itmes would drop below the basket walls e.g. keys, and the indiciator light would remind me that the keys are there.

Build a cardbord prototype of your design.

**\*\*\*Document your rough prototype.\*\*\***

Pictures of prototype

![image](https://user-images.githubusercontent.com/89586838/137835501-79ea6e1e-126c-400d-8cb3-c3fd02ccbe75.png)

![image](https://user-images.githubusercontent.com/89586838/137835470-a5fc4ec8-a39b-42be-8631-632c01164978.png)

![image](https://user-images.githubusercontent.com/89586838/137835447-40f1989f-b620-411b-a08f-64c8b248a9b9.png)

Video of the interaction with cardboard prototype
https://youtu.be/Tuscs7qTD1E


LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E (Optional)
### Servo Control with Joystick

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which we will be distributing the battery packs in the class. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.

<img src="https://scontent-lga3-1.xx.fbcdn.net/v/t1.15752-9/245605956_303690921194525_3309212261588023460_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_ohc=FvFLlClTKuUAX9nJ3LR&_nc_ht=scontent-lga3-1.xx&oh=b7ec1abc8d458b6c1b7a00a6f11398ac&oe=618D7D96" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.

Now that you have a basic idea of what a servo motor is, look into the script `qwiic_servo_example.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degree. Try running the servo example code now and see what happens:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!

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
Removing keys: https://youtu.be/NcZUdo75FOk
-Light is on triggering the user to take care of there disorganization problem. Put your things where they belong!

Adding keys: https://youtu.be/ibrr9OlsYwg
-Lights go out per bin. This is satisfying for the user.

In the future, I may make the lights blink to indicate more urgency for the user to get organized. A blinking light is annoying and the user will want to turn it off only by putting their things away.

### Some issues worth noting:
- I had overclocked my raspberry pi and running in the box, it frequently hit 80C. Outside of the box it was always under 70C. Noting to underclock the Pi for such applications inside enclosures.
- The capacitive touch sensors don't always work consistently with key drops. Adjusting the insulating layer of cardboard inside the box did help with cross talk. However, key drops and removals still weren't perfectly consistent. (or trigger was too sensitive) See blooper reels below!
  -  Blooper 1 https://youtu.be/tR5WC_N6n9s
  -  Blooper 2 https://youtu.be/3hxXqPuFrto





