## Contents

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

## Part A. Plan 

_Setting:_ 
This interaction is happening in a mock "bedroom" near my front door. The office chair is staged as a bed.

_Players:_ 
I am in the setting with my girlfriend. We both care about the front door being locked before bed for safety. We welcome the red light as a reminder if we completely forget. Sometimes I have to get up to check if the front door is locked and find that it is. This is bothersome not to know the status.

_Activity:_ 
The user going to bed is very tired and not thinking about all of their responsibilities as part of their routine to go to bed. Something as simple as locking the front door can be easily forgotton and become a safety issue. Building in a mechanism to prevent a safety issue (the front door being unlocked) is the goal.

_Goals:_
The goal of the player is go to bed safely. Safety means that the front door of the apartment is locked when sleeping.

### Storyboard

1. User wants to go to bed, needs sleep now
2. Gets in bed
3. Tries to turn off light
3. Light turns red instead of turning off - error
4. Why? Because the front door isn't locked
6. Goes to lock front door
7. Light turns back to normal color so user can see when returning to bed
8. User returns to bed, and turns off light. Light turns off successfully since the front door is locked

### Sketch

 ![Sketch](https://user-images.githubusercontent.com/89586838/131934452-9b41c3f3-6a0f-4b01-b9e8-02559df1f2b4.jpg)


**Feedback Check**

I received feedback from our Zoom breakout group during class, including TA Rei Lee, on the idea and a few people agreed this would be a valuable solution. People seemed to agree that forgetting to lock the front door can be common and having a reminder before bed would be valuable.

## Part B. Act out the Interaction

**Are there things that seemed better on paper than acted out?**

  - When someone lays down to go to sleep, sometimes they need the light to stay on longer after they lay down. So I staged the switch close enough to reach from bed to simulate a lamp.
  - I found out the feedback from the light changing color must be near instant so the user would associate the action of turning off the light with the error. This was difficult to coordinate with my smart lights by controlling manually. I figured this could be easily be automatic in a final version.

**Are there new ideas that occur to you or your collaborators that come up from the acting?**

- Yes, Initially, I thought that the light should turn off after the door was locked, but I realized the person trying to go to sleep wouldn't be able to see when they were returning to bed.
- Maybe a color other than red could be better for this warning. Red seems like something is urgent and this is more of a warning. I was thinking of using yellow, but yellow was too close to the color of the ambient light we started with.
- I realized that maybe the user wouldn't know what the red light error was associated with and I thought it could be cool if a laser line highlighted the route to fix the error. e.g. a line that connected from where the user is laying (bed) to the door (lock). That way the system could be exapnded upon and trace more errors in the house.

## Part C. Prototype the device

- The chosen device was a philips hue smart light system in the end. I experimented with tinkerbelle as well.

**Feedback on Tinkerbelle.**

- Sometimes when restarting the application, the port wasn't freed. I had to learn how to free ports.

## Part D. Wizard the device

My collaborator, Jennie, manually controlled the philips hue smart lights in coordination with the user actions for the video.

**First attempts at recording the set-up video**

First attempt at video - https://youtu.be/0k1K3RUhpGk. 

**Follow-up work**

The practice video ended up very similar to the final video. We just worked on timings, framing, and exposure. We also made sure the actions were mapped to the storyboard and the actor showed the appropriate emotions and gaze direction.

## Part F. Record

**Video of prototyped interaction.**

https://youtu.be/w-EmX2z1SGo

**Collaborators**

My girlfriend, Jennie, was the videographer and light controller! Many thanks.

## Staging Interaction, Part 2

**Peer Feedback**

"Great idea! one thing to consider is if you have roommates, that might become a privacy issue or might disturb someone's sleep."

"...I really like your design, and I think your design would be adopted by many of those who care about safety a lot. I can also see how versatile your design is from its potential to apply to all kinds of smart home safety alerts!

**Thoughts from feedback:**

The light turning red could annoy other roommates. If the final design only turns the light red in the bedroom of the person going to bed, and not the main hallway, this concern can be mitigated.

Applying a red light or different color lights depending on the home safety concern could be a great idea for iterations in the future!

**Documentation for V2**

After acting out the interaction again, I thought that a user may not know what the red light means. How could I point to the problem? (e.g. the lock is unlocked) I used a laser that would theorhetically be triggered from the error. This way, the user would know why the light turned red and potentially how to address the error. This would open the door to expand the funcionality of the system to say, find lost items around the house or resolve other errors. A red light can indicate an error and the laser could show you exactly where the error was coming from. The second benefit of using a laser would potentially be to remove the red error light completely. This could address the peer feedback I received about the red light being disutrbing to roommates. The laser seems less obstrusive.

Storyboard for V2 - Laser

![IMG_0017](https://user-images.githubusercontent.com/89586838/133180745-0148b446-bfcd-4bbf-937a-d331c8e5524c.jpg)

Video demonstrating addition of laser indicator for lock (when unlocked) 

https://youtu.be/AdA0c4MfJBQ
