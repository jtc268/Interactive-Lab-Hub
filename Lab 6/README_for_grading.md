Joseph Cera jtc268

Agustin Forero agf48 (for part E)



# Little Interactions Everywhere

## Prep

1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop.
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.

![publish settings](imgs/mqtt_explorer_2.png?raw=true)


### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment, we will continue to use the `circuitpython` environment we setup earlier this semester:
  ```
  pi@ixe00:~ $ source circuitpython/bin/activate
  (circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 6
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python sender.py
  pi@ReiIDDPi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/ReiTesting
  now writing to topic IDD/ReiTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...
  ```
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```
<img width="1268" alt="image" src="https://user-images.githubusercontent.com/89586838/141667891-1d7bfb10-0008-41db-8377-ef749300487d.png">
<img width="1278" alt="image" src="https://user-images.githubusercontent.com/89586838/141667921-84106e3f-1054-4a3e-a1cc-3505922f2a44.png">
<img width="492" alt="image" src="https://user-images.githubusercontent.com/89586838/141667925-e27eca6a-55c8-4eb4-9a3b-e6b751eb8db8.png">


**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***

1.) Sending a request for a coffee to a local barista by tapping a button on your desk, the coffee would then be delivered. The button would send a message of "address, 1 coffee" to the barista. If the person hit the button twice or multiple in a row (within a 10 second window) the message would say "address, 2 coffees" etc. This would be ideal for someone that just likes their coffee black.

2.) If someone faced to their right side and spoke into a directional mic, the message could be recorded and streamed to MQTT. A group of employees working from home would hear this message in their apartment. Announcment type messages could easily be send just by turning your head, similar to the old days when you would just turn and talk to a group of employees in the office.

3.) Someone could type "play X band" (any artist) at their friends house to cheer them up. The message would be posted to MQTT then received by a friend's machine to start Spotify.

4.) A wake up button could be pressed, and a signal sent to MQTT. A person that has slept in could be physically woken (remotely) by pressing a button. One press makes a sound, two presses shoots a rubber band at the person, and three presses shoots water at the person. If you keep pressing the button water would keep shooting out. Each shot would correspond with sound as well, for the best chance at waking someone up.

5.) A lighting sync system would randomize colored light in two homes. Couples in long distance relationships could feel more synced since they're living the same, unique experience together. A random color picker would stream to MQTT and each member in the couple would subscribe to the stream to change their smart lights to the same color.

### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. We will also be running this example under `circuitpython` virtual environment.

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***

I saw a my capacitive touch sensors streaming data into MQTT explorer. One was a coin, and the other was a dogecoin.

<img width="604" alt="image" src="https://user-images.githubusercontent.com/89586838/141879338-002b9df2-922a-4578-ab21-922715a7816a.png">

<img width="734" alt="image" src="https://user-images.githubusercontent.com/89586838/141879185-6713669f-9e88-4c78-a3de-2302e93b99d3.png">

<img width="777" alt="image" src="https://user-images.githubusercontent.com/89586838/141879165-e67bf494-cf9c-4a9c-b459-eee621b182ac.png">


**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***

I chose the distance sensor. The idea was to set a pokeball "trap" for Bagon the pokemon. If Bagon gets close enough to the trap, it could catch him! The sensor measures how far Bagon the pokemon was from my distance sensor and if he gets less than 50mm away, the trap would close on him. If you set a remote pokemon trap, you could monitor it and see when you wanted to try to catch! See video below of the test:

### Bagon Trap Video!

https://youtu.be/frU7MlvovEc


<img width="883" alt="image" src="https://user-images.githubusercontent.com/89586838/141879129-4e516e1d-78b8-4171-8205-37e042575067.png">

<img width="816" alt="image" src="https://user-images.githubusercontent.com/89586838/141879206-113c77ce-b7e3-4804-9219-43ac6a8f9d8f.png">


### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our heart, minds and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to ativate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

You may ask "but what if I missed class?" Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can go to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs. Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 

**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***

Yes! I was successful running color.py and changing the color on one true colornet. I also received signals from classmates changing the color net and the right side of my screen changed color per the photo below.

<img width="902" alt="image" src="https://user-images.githubusercontent.com/89586838/141878978-75bd4695-8969-4e3d-8c3f-0ac3cb65d852.png">

### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** 

The world of cryptocurrency is confusing and many people want to join in on the hype. Some just want to participate and others really want to make some money. The problem is, they don't have time to read about cryptocurrency trends all day to know when to invest. If a crypto analyst or other expert knew the time to buy a cryptocurrency, like dogecoin, they could tap a button on their desk to send the signal to others. The receiver of the signal could act on it how they wish. They would know it's a reliable signal from an expert. The expert would hit a button, and a single flash or strobing effect would alert the buyer to act on the recommendation. The whole screen changing color acts as an alert light on the buyer's desk.

**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

Actors:

1.) Crypto Analyst (sender)

2.) Crypto buyer (receiver)

Input (capacitive touch sensor): Metal coin attached to capacitive touch center via alligator clip. Coin is attached to 3d printed "doge" figure so the analyst knows which coin they are recommending to buy. One touch = one flash on the recipient's screen. 

Computation client 1, Crypto Analyst side: signal is processed and streamed to MQTT topic = 'IDD/joe/test/cap'
<img width="508" alt="image" src="https://user-images.githubusercontent.com/89586838/141878453-dee60db0-4d59-4983-a592-ced6415ed4a7.png">

Server side: message is posted "Dogecoin has been touched!"
![image](https://user-images.githubusercontent.com/89586838/141878611-ff47f952-a98d-4a9a-ab52-e2dbcc442cdc.png)

Computation client 2, Crypto buyer side: Detects new message "Dogecoin has been touched!" and script runs to light up OLED screen, indicating buy signal for Dogecoin.

Output (OLED screen): Lights up every time the Dogecoin "button" is pressed from Client 1, Crypto Analyst.

**\*\*\*3. Build a working prototype of the system.\*\*\***

The coin attached to the 3d printed dog would be part of a crypto analyst's array of high profile coins one could buy. I imagine the 3d printed dog (doge) would stand out amongst others and the analyst would know that this means "dogecoin". They would tap the coin as the "button" to send the buy signal to the receivers.

Interaction 1: (Crypto Analyst, sender)

<img width="632" alt="image" src="https://user-images.githubusercontent.com/89586838/141881787-908c893f-62d5-4fe6-809d-020adca9ae1b.png">

Interaction 2: (Crypto buyer, receiver)

<img width="630" alt="image" src="https://user-images.githubusercontent.com/89586838/141881845-ee6afdea-e59d-4373-a19a-1fec88891a42.png">

**\*\*\*4. Document the working prototype in use.\*\*\***

### Dogecoin Buy Light Interaction Demo

https://youtu.be/Opvp9KRdRm4

Thanks to Agustin Forero (agf48) for being an awesome partner!

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

