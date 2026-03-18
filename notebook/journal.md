# Notebook Information
Hey guys, this document will be where I track my progress on this project.  
## Engineering Design Process
Throughout this project, I will be using the engineering design process to iterate on my designs:

Identify the problem  
Brainstorm Solutions  
Implement The Best One  
Build The Model  
Test For Problems  

# Notebook Entries
## February 6th, 2026 - Friday - ~3 hours of progress
Today, I designed the first prototype of the index finger. This design will be the base of each finger besides the thumb.  

### CAD
![image](/notebook/assets/Finger-Prototype1.png)  

Since fingers mainly move in I decided to use a resolute/hinge joint for each segment of the finger. For the pins of each hinge, I took inspiration from my school's VEX V5 team. We often use screws to act as pins for hinges, so I decided to use that in my design. I designed each hole to have a diameter of 3.2mm to account for the tolerance of my 3D printer and used M3 screws.  

![image](/notebook/assets/fingerMuscles.jpg)  
Above, you can see a chart that shows the different muscles controlling your fingers. Something unique about the fingers is that there are no actual muscles located inside them. Instead, your body uses muscles in your forearm to move your fingers. These muscles pull on tendons which control how much your fingers are bent. To replicate this, I bought fishing line to act as the tendons and used servos I already had to act as the muscles.

### Build
I sliced the 3D model in Bambu Slicer and used lightning infill because the printed model is just a prototype. I used black PLA for this, and it took approximately 20 minutes.  
After I was done printing it, I aligned all the segments together and put in a M3x20mm screw to act as the pin for the hinges. The screw didn't fit in that well so I drilled the hole with a 3mm drill bit. Tying the fishing line was definetly the hardest part because it didn't want to tie no matter what.

### Testing and Identifying Problems
#### Problem 1
I quickly realized that the finger had no way to lift back up after being pulled down.

#### Problem 2
I also noticed that the finger could bend backwards. This was not only unnatural but made it so I couldn't pull it back down.

## February 7th, 2026 - Saturday
Hey guys! Today, I worked on the second prototype of the finger, addressing some of the major problems I found with the first prototype.
### CAD
#### Solution to Problem 1
1. **Use another servo and more fishing line**
    I could use another servo to act like another muscle.
2. **Use elastic cord**
    This solutions is cheaper and easier to implement, so I will choose this. 
#### Solution to Problem 2
Instead of positioning the pin at the very bottom of each joint, I can put it half way. This way, the flat part below the pin will stop the finger from being bent back. 

### Build
Once again, I sliced it in Bambu studio and kept all the settings the same. However, since theres now a holder for the elastic cord, I had toprint it sideways with support. I used PETG for support interface to make sure the support is easy to remove. 
After I was done printing it, I assembled it again. 

### Testing and Identifying Problems
The new design worked good and I was ready to move on to the servos.
#### Problem 1
The servos I tested, SG90 and HS-422 were not powerful enough to overcome the elastic cord.

#### Problem 2
Each bolt sticks out a little, making it hard to make the hand compact. 

### Brainstorming Solutions
#### Solution to Problem 1
I will be purchasing stronger servos on Amazon, specifically DS3225 servos.
#### Solution to Problem 2
I found these small metal pins on Amazon that should fit the fingers perfectly.
![image](/notebook/assets/metalDowels.jpg)
I might also consider printing plastic rods instead to save cost. 
## February 8th, 2026 - Sunday
Today, I recieved the new servos and tested them. The servos ended up working fine and were perfect for the job.

## February 9th, 2026 - March 12th, 2026
I worked on filling out the notebook. I also took a break from this project at this time.

## March 13th, 2026 - Friday - ~1 hour of progress
### CAD
Today, I modeled the DS3225 servo so I could have an easy refrence when modeling the palm for the hand. 
![image](/notebook/assets/DS3225.webp)
## March 14th, 2026 - Saturday - ~1 hour of progress
### Identifying Problems
When testing the fingers that I modeled, I noticed that I had to pull on the string a lot for the fingers to fully close. There was no way that the motors could close that far.

### Solution
Since the circumfrence of a circle is always larger than  it's diameter, I decided to model a tiny spool, which would help with increasing the length of string it could pull. 

## March 15th, 2026 - Sunday - ~3.5 hours
### CAD
Today, I decided to start working on the palm of the hand. One of the goals I had for the hand was to make it look natural, so I wanted it to be compact. Unfortunately, the design I came up with today was really chunky, but I will improve on the design in the future.

I only modeled part of the hand because I was only going to print a small portion of it to test if it would fit.
![image](/notebook/assets/PalmV1.png)

### Build and Testing
I printed the small portion in PLA.
![image](/notebook/assets/palmPrototype_v1_1.jpg)

#### Problem 1
I didn't account for the wires on the servo, so the servo can't fit into the palm.

#### Problem 2
Since the servo is so close to the finger, the finger can't close all the way without hitting the servo.

#### Problem 3
This design uses a LOT of filament. The slicer estimated around 132g of PLA for the whole palm. If I kept this design, I would quickly waste all of my filament. 

### CAD
I completely overhauled the design. I made the base thinner so that the wire could pass through the palm completely. This thinner design helped reduce the cost of filament as well. The cost went down from 42g to 12g for a single finger. I also moved the servo back so that the finger would never contact the servo when its being pulled down.

![image](/notebook/assets/palmPrototype_v2_1.png)

### Build and Testing
Once again, I printed this out of PLA. 

#### Problem 1
This new design didn't fix problem 1 because I couldn't get the stub through the hole because the hole was designed for the servo without the stub.

#### Problem 2
Although the finger doesn't touch the servo anymore, it can't fully close because it is blocked by the palm.

![image](/notebook/assets/palmPrototype_v2_2.jpg)

### CAD
Third times the charm! I hope... 
#### Solution 1
I cut a hole into the palm so that the stub could pass through cleanly.
![image](/notebook/assets/palmPrototype_v3_2.png)
#### Solution 2
I moved the hole for the pin even higher up so that the finger tip wouldn't hit the palm anymore. 
![image](/notebook/assets/palmPrototype_v3_1.png)

### Build and Testing
Not so surprisingly, I printed this out of PLA. This design solved all the problems that I noticed in my old iterations, but other problems showed up quickly. 

![image](/notebook/assets/palmPrototype_v3_3.jpg)

#### Problem 1
There's no way for the elastic cord to attach to the palm, so it has no way to return to the normal position. Instead, it stays at a 90 degree angle with the palm when not activated. 

#### Problem 2
Theres no way to route the fishing line, so when the finger is pulling, it gets blocked by the fishing line. 

## March 16th, 2026 - Monday - ~0.5 hours of progress
### CAD
Today, I couldn't spend much time on this project because of school. However, I modeled a better design of the palm. For this new iteration, I want to implement a forearm which will hold all my servos instead of storing the servos in the palm. I haven't modeled the forearm with the servo holders yet, but here's what I modeled!

![image](/notebook/assets/fullpalmprototype_v1_1.png)

I still need to figure out how to model the thumbs but it's getting late. Good night!

## March 17th, 2026 - Tuesday
Today, I wanted to start coding so I could test my servos. I think that coding will take the longest so I want to start now.
To control the finger, I want to use an Arduino R3 I have.
![image](/notebook/assets/ArduinoUnoPinout.png)
The servos are controlled with PWM, so I can only use pins 5, 11, 12, 15, 16, 17. This should be enough pins because I only have 5 fingers. In the future, I might upgrade to an esp32 for more PWM pins if needed.

This is one of my first times programming in C++ so this might take a while.

### Identify the Problem
I need a way to find how much my servo needs to pull for the hand to fully close.

### Brainstorm Solutions
I can write a program where I can tell the servo to go to a certain angle. When I find the write angle, I can write it down.

### Implement the Best Solution
I've started coding the servos on Arduino IDE. 

### Identify the Problem
The overall goal of this hand is to be able to see my fingers and it's position and mimic that onto the hand. 

### Brainstorm Solutions
When researching ways for the computer to see and process my hand, I stumbled across OpenCV. OpenCV is a library thats made for computer vision. Using computer vision, I can see what angle each segment of my fingers are at. 

I've read through this article by OpenCV and it seemed to match what I wanted.
https://opencv.org/wp-content/uploads/2020/11/Universal-Hand-Control.pdf