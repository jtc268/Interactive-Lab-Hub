# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

Algorithm number 1 seems great at classifying borders and objects with distinct shapes. I could use this as a bird detector. A bird's shape is distinct like the toy I placed in the image below and different from say, a leaf. I could make a bird alert system so I can go look out the window to view birds only when they come.

<img width="651" alt="image" src="https://user-images.githubusercontent.com/89586838/139770798-412430f4-a4ae-4990-a2fe-985f04418b78.png">

Algorithm number 2 is detecting faces. This could be used to detect people when there are other moving objects in spaces. Potentially to count people walking across a city street to measure where foot traffic is the highest. You could then deploy traffic guards to protect pedestrians. The algorithm could distinguish between moving cars and people and have a reliable count.

<img width="651" alt="image" src="https://user-images.githubusercontent.com/89586838/139771196-d0677f96-d76d-476f-8e63-e328903cbce4.png">

Algorithm number 3 had an interesting point mapping to a continued flow detection. I could imagine this being used to trace movement paths of people to improve walking routes of a park.

<img width="678" alt="image" src="https://user-images.githubusercontent.com/89586838/139771739-37466ebc-26ec-4952-86bc-20555b8cd40b.png">

This can be used as a bird's eye view in a park, and streak colors where people like to walk. Then we can design better city path systems that map to where people truly want to walk and optimize walking UX.

<img width="586" alt="image" src="https://user-images.githubusercontent.com/89586838/139771827-e9554443-59a2-4974-b85c-4e328d03d8bb.png">


Algorithm number 4 seemed to detect objects and seemed the most laggy. I think this could be used in a very controlled environment to count how many objects entered a frame that were not touching each other. Through my tests of holding up objects, the object dtector had trouble disconnecting mount points (e.g. my fingers) from the actual objects. It's important to count how many bees are pollinating flowers on average to see if the bee population is going down in certain areas. I think this could be a useful application for ecosystem conservation initiatives.

<img width="655" alt="image" src="https://user-images.githubusercontent.com/89586838/139772286-00a04dab-9da4-4bef-b4a5-f42aa931dd15.png">

<img width="655" alt="image" src="https://user-images.githubusercontent.com/89586838/139772271-14cf3cd3-c579-4501-a461-82494c0d1b9c.png">

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

<img width="656" alt="image" src="https://user-images.githubusercontent.com/89586838/139773492-7f46188c-4797-4039-abfe-022290081582.png">
<img width="656" alt="image" src="https://user-images.githubusercontent.com/89586838/139773501-6236bbda-0b0f-4214-bb49-686b5cdbeb37.png">
<img width="656" alt="image" src="https://user-images.githubusercontent.com/89586838/139773515-19ec3b69-7cdc-47f0-8b53-267650fbbc86.png">

"Quiet coyote" didn't work by pinching middle finger to thumb, so I pinched pointer to thumb :) and got 0%. Great!

<img width="656" alt="image" src="https://user-images.githubusercontent.com/89586838/139773547-c10bf734-70fb-4d8f-b22e-1d8df464a9e5.png">

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

For hand tracking, this would be perfect for muting the volume on the tv when I need instant silence. The pointer to thumb pinch or "quiet coyote" would instantly mute the tv if you get a phone call or just need some silence. It would be a delightful feature to have.

A second idea would be to make a stretch timer automatically start when you bend over to touch your toes. It would count down from 20 seconds to make sure you get a good stretch. The count down would start automatically when you were say, 40% bent over. This would have to be tested.

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)

#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***

Teachable machines screenshot - program running

<img width="953" alt="image" src="https://user-images.githubusercontent.com/89586838/139774712-f91fd973-fe6f-48d7-a4cd-2829cf5bbae0.png">

I would use teachable machines on captive birds to classify a blue jay versus other types  of birds. The machine could classify blue jays among other birds in a given environment. This would be useful for birders that are measuring yearly migration increases or dropoffs for species that come through NYC.


*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


#### Filtering, FFTs, and Time Series data. (optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

I would like to use the object detection algorithm to classify birds outside my window. I see three types 1.) Bluejay 2.) Pigeon 3.) Robin. If a bluejay comes, I'd like an announcement from a speaker - "bluejay". That way I know to go to the window to look at the bluejay, my favorite bird.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do? - it's supposed to say "bluejay" when a bluejay lands outside my window on the fire escape.
1. When does it fail? - I expect it to fail when a moving object, like a leaf, floats by. We need to distinguish between leaves and other birds.
1. When it fails, why does it fail? - It fails based on incorrect color detection or objects moving like birds.
1. Based on the behavior you have seen, what other scenarios could cause problems? - the lighting being too dark could cause the object detection algorithm to miss the bird. Also, if the bluejay is standing on an object, it could "connect" to that object and no longer "look" like a bird.

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system? - No, if the machine says "bluejay" then they will think there is a bluejay. If they go to the window and it's not there, they would probably think they missed it.
1. How bad would they be impacted by a miss classification? - It wouldn't matter too much. It would just be a false alarm for a bluejay and cause the user to to walk to the window.
1. How could change your interactive system to address this? - We could say "bluejay, 50% confident!" or "bluejay, 100% confident!" that way the user knows to rush to the window or walk slowly and prepare to be disappointed.
1. Are there optimizations you can try to do on your sense-making algorithm. - Yes, we can optimize with the motion detection algorithm to distinguish between a bluejays movement and another bird's movements if that's possible.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for? - To count bluejays for conservation of the species or to detect bluejays for viewing pleasure.
* What is a good environment for X? - An apartment window in an area with bluejays.
* What is a bad environment for X? - An area that has a lot of bluejays, since they would be easy to spot without the detector.
* When will X break? - If a bird that looks similar to a bluejay (or any bird) enters the frame. Perhaps even a leave or inclement weather could trigger the alert. This has to be tested.
* When it breaks how will X break? - It will say "bluejay" and there won't be a bluejay. The user will be disappointed.
* What are other properties/behaviors of X? - The device will have an auto mute function for quiet hours.
* How does X feel? - If a weighted device that can sit on a window pain. It has a clear directional indicator on which end points outside.

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

I ran out of time to make a video for this lab.

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

After exploring the bird detector more, I decided that detecting a bluejay specifically would be very difficult for this lab (and my current skill levels) and pivoted to a compeltely different interaction.

I will be making a "Red Light Green Light" game interaction using the hand interaction algorithm. This idea is from the children's game where one leader says "red light" for stop and "green light" for go. Participants start a distance from the leader and the goal is to reach the leader. "Quiet coyote"/pinched fingers will be STOP (as if the participant stops running in the original game - RED LIGHT) and open fingers will be GO. (as if the participant is running in the original game - GREEN LIGHT)

Some inspiration was taken from the Netflix series, Squid Game. A picture of the more intense version of Red Light Green Light is below. I will not explain the game since it involves spoilers.

https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.gamesradar.com%2Fsquid-games-red-light-green-light-gets-an-unreal-engine-version%2F&psig=AOvVaw2-C_O3EikBNDboN2Oe5yI9&ust=1636515233224000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCMi2-bysivQCFQAAAAAdAAAAABAD![image](https://user-images.githubusercontent.com/89586838/140857399-1a2b9c8b-3ec0-404a-bce8-29af898a87cf.png)

Plan:
- Make replica of girl robot from Squid Game
- Place OLED screen behind her eyes to turn red or green, maybe half of the screen can cover each eye to make it scary
- First iteration: game starts from command line. Second iteration, game starts by pressing a "game start" button
- A game participant shows pinched index finger with thumb, signaling "ready to start game"
- After 5 seconds of observing pinched fingers, Girl robot says "Green light!", starting the game
- 5x random time increments between 2 and 7 seconds will alternate "Red light" and "Green light" commands
- If fingers are not pinched within 1 second of a "red light", a buzzer sounds, signaling loss of the game
- If game participant makes it through all 5 rounds, a winning bell sound is played. yay!


**\*\*\*Include a short video demonstrating the finished result.\*\*\***
