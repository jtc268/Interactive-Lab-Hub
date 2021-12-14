## Lumineer - A Motivated Walking Experience

TL;DR? Skip Straight to the Video Index below. Otherwise, check out the documentation and process! 

This project was completed as a final project for a class called Interactive Device Design at Cornell Tech in fall of 2021. Special thanks to everyone that helped with this project, whether it was advice, encouragement, lending spare parts or otherwise: Jennie Shapira, Rei Lee, Alexandra Bremers, Wendy Ju, and David Opatrny.

## Video Index

*   Full demo https://youtu.be/7WhpFnoeqFg
*   Functional Check off (Step Counter test 1) https://youtu.be/9p4TcYc1kkY
*   Step Counter Test 2 https://youtu.be/JExaj05UZHY
*   Full Flow test - view of terminal and MQTT [https://youtu.be/DcHa4ZB9qEw](https://youtu.be/DcHa4ZB9qEw)

## Code

https://github.com/jtc268/Interactive-Lab-Hub/blob/Fall2021/Final_Project/v6_wearable_walking_meter.py

## Parts Requirement List

*   Raspberry Pi - I used a Raspberry Pi 4 (Previous models will also work) https://www.raspberrypi.com/products/raspberry-pi-4-model-b/
*   I2C Bus - I used https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi
*   Accelerometer - I used https://www.adafruit.com/product/3886
*   LED light stick - I used https://www.sparkfun.com/products/14783
*   External battery **with** power delivery (PD) - I used this [https://www.amazon.com/mophie-powerstation-Plus-USB-C-Universal/dp/B07CK2CV83](https://www.amazon.com/mophie-powerstation-Plus-USB-C-Universal/dp/B07CK2CV83)
*   Small fanny pack (optional and recommended). [https://www.amazon.com/gp/product/B0747JBNXT/](https://www.amazon.com/gp/product/B0747JBNXT/) Otherwise you can build the setup into the shirt via sewn pouches
*   Fabric tape or duct tape
*   Mobile phone with wireless hotspot enabled

## Documentation and Process

I was sitting and thinking, "I really need to walk today." I recently saw my friends humble bragging about how they closed their Apple Watch "circles" or "activity rings". (see below)

![](https://user-images.githubusercontent.com/89586838/145913519-632d7004-baa3-4718-b5cf-8479707b69e0.png)

I was jealous of their rather competitive talks and conversations and noticed they pointed out their activity rings to others that didn't have the Apple Watch. I thought - how might we expand this ecosystem and display the progress of an Apple Watch to the general public so they can engage in this motivated exercise experience? The Apple Watch is usually always on a user throughout the day, and starting the conversation about for activity rings requires you to open the app and engage in a conversation. What if we removed this friction to show the visual? Building in a similar experience to clothing, projecting activity rings out to the world, I figured could engage others into an interactive experience and inspire people to walk more, or at least ask a question - "what is that glowing on your shirt?". The premise is that it's hard to motivate yourself to exercise and interactive games, apps, and social motivators could make people more healthy all while having fun.

I set out to build LED lights into clothing to broadcast an activity "status". Based on how much you walked in a day, your activity meter would increase. You'd start the day with 0, or no light. As you walked, the light bar would fill up! 

It turned out that this wasn't enough of a motivator for me to keep walking. So I kept thinking through the experience (see initial ideation sketches below). I wanted to imagine a way to get more people involved in this walking experience that was rewarding for all users. Taking inspiration from video games, I wanted to work in elements of progress, leveling up, and rewards/badging/achievements in a simple LED light system. The interface was limiting and simple, which was fun to work with.

Below is a story board of the intended user experience:

This is a game of walking in 1 mile chunks. You gain your "entry level" / level 1 to the game by walking 1 mile and filling your LED light meter that is built into your shirt. Once you fill your LED meter, you can invite someone else to walk a mile. There is no limit to how many people you can invite to walk a mile after you have walked one mile.

*   This is a 3 user scenario (however, this experience is highly scalable and meant to motivate as many people to walk as possible)
*   User 1, puts on cool new shirt with LED lights in the sleeve
*   User 1, is motivated to walk 1 mile to get LED light meter to fill up on sleeve
*   LED light bar fills, and changes color to indicate Level 1 has been reached. Yay! Now what?
    *   Then, and only then, User 1 can invite someone else with a shirt to walk 1 mile. If they do, User 1 will level up!
    *   User 1 asks User 2 to walk one mile so they can level up - User 2 says, "OK!"
*   User 2 enters the game
    *   User 1 is now "subscribed" or "following" User 2
*   User 2 walks a mile and fill their LED light meter
*   No matter where User 1 currently is, their LED light meter "parties" or goes into party rainbow mode!
    *   User 1 knows that User 2 completed their mile
    *   After the "party", User 1's LED bar is leveled up to a new color and they feel rewarded for encouraging another person to walk
*   User 1 proceeds to invite another person to walk, User 3
*   User 3 walks a mile
    *   User 1 is, again, rewarded by a "party" on their LEDs and levels up to level 3 (a new color)
*   All users can invite others to walk in order to level up their

Not only can users fill their meter (e.g. close their Apple Watch "activity rings"), but they can upgrade there "encouragement status" via leveling up by inviting other users to walk. This encourages users to motivate others and improve everyone's health. Users that are invited will feel motivated to walk in order to cause a fun party on their motivator's arm and level them up. There's a sense of fun obligation. There's also a sense of needing to "nudge" the invited person to finish their mile, so it actually gets done! The project started out with trouble motivating myself to walk each day. I feel this user experience could help.

### Sketches:

![image](https://user-images.githubusercontent.com/89586838/145755375-17f29d3d-b9af-4040-90f8-dca42900eb03.png)

![image](https://user-images.githubusercontent.com/89586838/145755519-e33bf4c9-c69a-40ce-84a4-1a3d5cee6c57.png)

![image](https://user-images.githubusercontent.com/89586838/145755533-ef7282c5-9909-4850-9953-8374bb49d870.png)

![image](https://user-images.githubusercontent.com/89586838/145755539-ee09d249-36f3-43d8-992d-caff7f5ba0fe.png)

![image](https://user-images.githubusercontent.com/89586838/145755552-cb5fd347-b67b-4a3c-9ab4-728bad521037.png)

## Wireless hardware setup

Note 1: Battery life of the Mophie 12000MaH pack was impressive. There were 4 "bars" on the battery pack and one hour of Lumineer shirt use didn't reduce a single "bar" on two separate occasions.

Note 2: For a truly wireless, networked setup, a mobile phone with hotspot functionality was enabled for the Pi to connect to a network while walking outside. This was also required to send and receive signals to/from the MQTT server.

I needed to measure steps (to calculate one 1 mile, which is ~2000 steps) - the accelerometer covers this. I also needed to indicate progress via LED. A simple addressable RGB LED stick could output the light patterns I needed. I needed multiple colors and each LED to be addressable individually to power up the "meter". I needed colors for user rewards and level-up indicators.

![](https://user-images.githubusercontent.com/89586838/145911515-e8c275f3-a9df-4048-8280-dfd4b10747ea.png)

With Labels:

![](https://user-images.githubusercontent.com/89586838/145912427-c007a166-f8cd-4a1a-bda4-9e24932dc105.png)

### Writing and testing the app

Link to code [https://github.com/jtc268/Interactive-Lab-Hub/blob/Fall2021/Final_Project/v6_wearable_walking_meter.py](https://github.com/jtc268/Interactive-Lab-Hub/blob/Fall2021/Final_Project/v6_wearable_walking_meter.py)

Simple IF and WHILE loops were used to taking readings from the accelerometer and trigger the LED light stick to fill up. Here is a video testing the initial step counter system, triggering the LED light stick to fill up [https://youtu.be/9p4TcYc1kkY.](https://youtu.be/9p4TcYc1kkY.) For other users to get involved, I used MQTT server. Luckily, the server was already hosted by an individual at my university. I simply used the server to create brokers and subscribers [https://mqtt.org/.](https://mqtt.org/.) This was extremely useful for testing, as I could trigger certain interactions to test without walking a mile! For example, I could trigger the action remotely of User 2 walking a mile by simply "publishing" a command from MQTT, see video - full Flow test - view of terminal and MQTT [https://youtu.be/DcHa4ZB9qEw](https://youtu.be/DcHa4ZB9qEw)

How to trigger a "walking rainbow" from [https://qwiic-led-stick-py.readthedocs.io/en/latest/ex8.html](https://qwiic-led-stick-py.readthedocs.io/en/latest/ex8.html) 

Below is a guide on what MQTT commands could be published in this app. Again, see this [video](https://youtu.be/DcHa4ZB9qEw) for a demo (same as above)

![](https://user-images.githubusercontent.com/89586838/145921530-09f2a1ca-0e5b-42c2-b6b9-a1a316fab45a.png)

In the final system design, user "jumpluff" and "sneasel" would actually be other shirts or people you follow. Once they walk a mile, a signal would be sent to MQTT, which User 1 is subscribed to. User 1 could react to an event sent by other users, creating the Lumineer network.

If you were to recreate this yourself, you would have to host your own MQTT server with an always on machine that had availability outside of your network, just like any other web server.

Notes while coding and testing:

*   Tweaks were available for brightness of the LED stick. Staring directly at it was painful to the eyes on max brightness "31". Turn it down below 10 so you don't scorch your eyes. Line 44 `stick.set_all_LED_brightness(31)`
*   Use MQTT to design commands to "wizard" or test interactions for product design. It's much more useful than stepping to get the accelerometer to increment up to the desired LED light bar status in order for other interactions to occur. This tests and end-to-end internet enabled experience from the beginning and technically sets you up for a shippable app.
*   Sometimes the 6050 accelerometer would go "out of whack" and start to log steps when I was not stepping, even when the device was secure and stable in the fanny pack. It's worth spending extra time to set thresholds to upgrade the accuracy of the step counter.

### Visual System Design using Universal Modeling Language

Referencing the [core python program](https://github.com/jtc268/Interactive-Lab-Hub/blob/Fall2021/Final_Project/v6_wearable_walking_meter.py)

![image](https://user-images.githubusercontent.com/89586838/145696669-ae55f5a3-d962-43ee-8401-2e1d0b820c64.png)

### Building the shirt and attaching the computer to the human

The LED light stick stuck inside shirt with duct tape (Quite resilient and integrated feel! I wore the shirt for an entire day and forgot the light stick was inside. There were no issues of the light stick falling off.) You must connect a longer I2C cable to this LED light stick from the fanny pack. (shown later) The wire connection port on the LED stick should be on the bottom side of the LED stick (facing down on the sleeve) to work correctly with this code.

![](https://user-images.githubusercontent.com/89586838/145911731-312efa22-f0bc-4bba-90d4-72251f435bb3.png)

With the stick attached, I needed to attach a a battery, pi, wiring, etc. to a human. This items are rather heavy to be sewn or taped into a shirt and I didn't want the stretch effect on the shirt. Using a fanny pack with a shirt draped over it ended up being the way forward for this case. See the below photo blog on building the fanny pack system, to then be wired to the shirt:

![](https://user-images.githubusercontent.com/89586838/145917537-0929620c-c074-4501-ab23-6d09254f46ab.png)

![](https://user-images.githubusercontent.com/89586838/145917837-ab0fc1b4-409f-42d4-b083-6bb37ec34d9a.png)

![](https://user-images.githubusercontent.com/89586838/145917672-90a4910e-0406-404e-927e-506c7d94d021.png)

![](https://user-images.githubusercontent.com/89586838/145917742-d29520fb-f1f7-45d9-ba13-30aef4182517.png)

![](https://user-images.githubusercontent.com/89586838/145917953-c872b313-5d97-47c7-8b74-38fe9da4b39d.png)

Eventually, a hole can be made through the fanny pack to integrate this single connection to the shirt more cleanly.

### Examples of final looks:

Thanks to Jennie for user testing this product!

![](https://user-images.githubusercontent.com/89586838/145918099-a46561a3-510f-4d1b-a3b5-0c08aca689d5.png)

I wanted a subtle feel with the LEDs, not too loud. (for users that want a minimalist aesthetic) So I chose a black shirt. While hard to see, I feel people may have a higher chance at wearing this. I found a shirt an Uniqlo that embodied the design language. (Dots) 

![](https://user-images.githubusercontent.com/89586838/145918236-979a1557-85ec-4c2d-bf8b-64b31d8d583a.png)

Pulling shirt over the fanny pack simulated the final experience of a very small electronic integration, with lights you can hardly feel in the shirt. Wearing the shirt all day, I forgot the lights were even attached. It was great.

![](https://user-images.githubusercontent.com/89586838/145918543-25e412e2-bffe-48de-bcd6-3173a13fd4b7.png)

![](https://user-images.githubusercontent.com/89586838/145918396-04baabc6-0852-4ef0-8106-5d961f815229.png)

### Testing and feedback

*   The walker or main user couldn't always see the lights on their arm to enjoy the "party" or increasing status. While the intent was to show status to the outside world to inspire walking, this proved to be a lacking approach based on multiple comments when user testing. Users wanted to more easily see the light status.
    *   To change this, I would either wrap a flexible LED strip around the sleeve of the shirt or integrate LEDs somewhere where the user could see them easier.
*   People generally enjoyed the rainbow LED "party" when leveling up and thought it was fun.
*   Feedback was mixed on the "level up". Generally people thought it was "cool", however that may not be a fully excited user. I couldn't gauge if this was rewarding for users and this would need to be further tested.
    *   Perhaps something additional is needed as a reward for encouraging others to walk. This is a major thing to ask of users and the core purpose of the product - to spread walking virally via networking.

### Reflections and what I would improve on the next version

Overall, this was an extremely fun project. It was my first time thinking through clothing design and lighting on clothes. To improve, I would change a few things on V2:

*   Sew in wiring from fanny pack so the user isn't tickled by wiring on their back or arm
*   Use MQTT more for testing from the beginning! I know I mentioned this before, but it's worth mentioning again. Triggering events remotely is a great way to test interactions early on in the design process and is invaluable. This can also be useful to trigger commands on a headless computer (no monitor or no way to remote into the computer)
*   If possible, integrate a smaller computer completely in the shirt. Make a more "thin client" computer that only receives a Bluetooth signal of sorts.
*   Think through the "following" or "subscribing" interaction. This needs to be some sort of app.
    *   To follow someone, three ideas:
        *   QR code scan on shirt
        *   NFC tap on shirt to trigger app to follow from phone [https://www.amazon.com/NFC-tags/s?k=NFC+tags](https://www.amazon.com/NFC-tags/s?k=NFC+tags)
        *   Simply looking up the user within an app environment, similar to following someone on Instagram
*   While I did try to integrate a second raspberry pi into the system, I ended up bricking the device (to my knowledge) by trying to update the kernal to be compatible with an I2C bus. Perhaps the pi can be recovered. I spent too much time on setting up a 2nd pi and wish I put more work into the overall product design as a trade for this time, as MQTT could replace the 2nd pi to replicate the intended user experience.

After demoing this shirt and experience to 10+ people, I feel that the shirt created some delight with users. This may be something to explore further in terms of gamifying and _wearing_ your walking with LEDs.

## Additional link to the full demo if you decided to read before watching [https://youtu.be/7WhpFnoeqFg](https://youtu.be/7WhpFnoeqFg)

Thanks for reading and please don't hesitate to reach out with questions or feedback.
