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

### Design
![image](/assets/Finger-Prototype1.png)  

Since fingers mainly move in one axis I decided to use a resolute/hinge joint for each segment of the finger. For the pins of each hinge, I took inspiration from my school's VEX V5 team. We often use screws to act as pins for hinges, so I decided to use that in my design. I designed each hole to have a diameter of 3.2mm to account for the tolerance of my 3D printer and used M3 screws.  

![image](/assets/fingerMuscles.jpg)  
Above, you can see a chart that shows the different muscles controlling your fingers. Something unique about the fingers is that there are no actual muscles located inside them. Instead, your body uses muscles in your forearm to move your fingers. These muscles pull on tendons which control how much your fingers are bent. To replicate this, I bought fishing line to act as the tendons and used servos I already had to act as the muscles.

### Build
I sliced the 3D model in Bambu Slicer and used lightning infill because the printed model is just a prototype. I used black PLA for this, and it took approximately 20 minutes.  
After I was done printing it, I aligned all the segments together and put in a M3x20mm screw to act as the pin for the hinges. The screw didn't fit in that well so I drilled the hole with a 3mm drill bit. Tying the fishing line was definitely the hardest part because it didn't want to tie no matter what.

### Testing and Identifying Problems
#### Problem 1
I quickly realized that the finger had no way to lift back up after being pulled down.

#### Problem 2
I also noticed that the finger could bend backwards. This was not only unnatural but made it so I couldn't pull it back down.

## February 7th, 2026 - Saturday
Hey guys! Today, I worked on the second prototype of the finger, addressing some of the major problems I found with the first prototype.
### Design
#### Solution to Problem 1
1. **Use another servo and more fishing line**
    I could use another servo to act like another muscle.
2. **Use elastic cord**
    This solutions is cheaper and easier to implement, so I will choose this. 
#### Solution to Problem 2
Instead of positioning the pin at the very bottom of each joint, I can put it half way. This way, the flat part below the pin will stop the finger from being bent back. 

### Build
Once again, I sliced it in Bambu studio and kept all the settings the same. However, since theres now a holder for the elastic cord, I had to print it sideways with support. I used PETG for support interface to make sure the support is easy to remove. 
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
![image](/assets/metalDowels.jpg)
I might also consider printing plastic rods instead to save cost. 
## February 8th, 2026 - Sunday
Today, I received the new servos and tested them. The servos ended up working fine and were perfect for the job.

## February 9th, 2026 - March 12th, 2026
I worked on filling out the notebook. I also took a break from this project at this time.

## March 13th, 2026 - Friday - ~1 hour of progress
### Design
Today, I modeled the DS3225 servo so I could have an easy reference when modeling the palm for the hand. 
![image](/assets/DS3225.webp)
## March 14th, 2026 - Saturday - ~1 hour of progress
### Identifying Problems
When testing the fingers that I modeled, I noticed that I had to pull on the string a lot for the fingers to fully close. There was no way that the motors could close that far.

### Solution
Since the circumference of a circle is always larger than  it's diameter, I decided to model a tiny spool, which would help with increasing the length of string it could pull. 

## March 15th, 2026 - Sunday - ~3.5 hours
### Design
Today, I decided to start working on the palm of the hand. One of the goals I had for the hand was to make it look natural, so I wanted it to be compact. Unfortunately, the design I came up with today was really chunky, but I will improve on the design in the future.

I only modeled part of the hand because I was only going to print a small portion of it to test if it would fit.
![image](/assets/PalmV1.png)

### Build and Testing
I printed the small portion in PLA.
![image](/assets/palmPrototype_v1_1.jpg)

#### Problem 1
I didn't account for the wires on the servo, so the servo can't fit into the palm.

#### Problem 2
Since the servo is so close to the finger, the finger can't close all the way without hitting the servo.

#### Problem 3
This design uses a LOT of filament. The slicer estimated around 132g of PLA for the whole palm. If I kept this design, I would quickly waste all of my filament. 

### Design
I completely overhauled the design. I made the base thinner so that the wire could pass through the palm completely. This thinner design helped reduce the cost of filament as well. The cost went down from 42g to 12g for a single finger. I also moved the servo back so that the finger would never contact the servo when its being pulled down.

![image](/assets/palmPrototype_v2_1.png)

### Build and Testing
Once again, I printed this out of PLA. 

#### Problem 1
This new design didn't fix problem 1 because I couldn't get the stub through the hole because the hole was designed for the servo without the stub.

#### Problem 2
Although the finger doesn't touch the servo anymore, it can't fully close because it is blocked by the palm.

![image](/assets/palmPrototype_v2_2.jpg)

### Design
Third times the charm! I hope... 
#### Solution 1
I cut a hole into the palm so that the stub could pass through cleanly.
![image](/assets/palmPrototype_v3_2.png)
#### Solution 2
I moved the hole for the pin even higher up so that the finger tip wouldn't hit the palm anymore. 
![image](/assets/palmPrototype_v3_1.png)

### Build and Testing
Not so surprisingly, I printed this out of PLA. This design solved all the problems that I noticed in my old iterations, but other problems showed up quickly. 

![image](/assets/palmPrototype_v3_3.jpg)

#### Problem 1
There's no way for the elastic cord to attach to the palm, so it has no way to return to the normal position. Instead, it stays at a 90 degree angle with the palm when not activated. 

#### Problem 2
Theres no way to route the fishing line, so when the finger is pulling, it gets blocked by the fishing line. 

## March 16th, 2026 - Monday - ~0.5 hours of progress
### Design
Today, I couldn't spend much time on this project because of school. However, I modeled a better design of the palm. For this new iteration, I want to implement a forearm which will hold all my servos instead of storing the servos in the palm. I haven't modeled the forearm with the servo holders yet, but here's what I modeled!

![image](/assets/fullpalmprototype_v1_1.png)

I still need to figure out how to model the thumbs but it's getting late. Good night!

## March 17th, 2026 - Tuesday
Today, I wanted to start coding so I could test my servos. I think that coding will take the longest so I want to start now.
To control the finger, I want to use an Arduino R3 I have.
![image](/assets/ArduinoUnoPinout.png)
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

## March 19th, 2026 - Thursday - ~0.5 Hour
Today, I drew out the schematic of the robotic arm. It's pretty simple but it doesn't need to be very complicated. 
![image](/assets/roboticHand_schematic_1.png)

I'll be using a DC Power Supply to power the servos. The Arduino will be powered by my PC through the USB port. I'm a bit worried that the servos will draw too much current. However, my power supply has overcurrent protection so it shouldn't burn my house down.  

On Tuesday, I'm not sure why I thought 12, 15, and 16 had PWM function. I looked closer at the board today and realized that the pins with the tilde were the only ones with PWM features.  

Thats all I did today! See you tomorrow!

## March 21st, 2026 - Saturday
Happy Saturday! I'm so glad that it's the weekend. Today, I want to work on the design of the hand and address a problem that I have with my current finger design.

### Design
#### Identifying Problems
The problem that I have with the current design is that the current aligners for the elastic cord stick out the top of the finger. The current design doesn't look good and is hard to 3D print.

![image](/assets/elasticProblem.png)

#### Solution
I plan to fix this by cutting holes into the finger. This will likely need completely new design because the slots of the holes take up too much space. I might switch to 1 or 2mm pins instead of 3mm pins to save space.

Now that we have identified our solution, lets start designing!

Here's my updated design!

|New|Old|
|---|---|
|![image](/assets/fingerPrototype_v4_2_1.png)|![image](/assets/fingerPrototype_v3_2_1.png)|

As you can see, I've moved the holes to inside the finger and used a smaller pin hole. This has allowed me to increase the filet on the finger. making it look better.

I've printed the segment in PLA on my Bambu P1S. I also printed one in TPU because I want to test if it will give me extra grip when holding items.

I think the new design works fine. I still need to model the other finger segments, so I won't know if the design is perfect until then. I'll start working on the next segments now. 

TADA!
|Segment 1|Segment 2|Segment 3|Full Assembly|
|---|---|---|---|
|![image](/assets/fingerPrototype_v4_1_1.png)|![image](/assets/fingerPrototype_v4_2_1.png)|![image](/assets/fingerPrototype_v4_3_1.png)|![image](/assets/fingerPrototype_v4_full_1.png)|

Since I didn't have any m2 bolts and nuts, I just modeled a 2mm cylinder to act as a pin. Hopefully this will reduce the overall cost of the hand.

#### Testing and Identifying Problems
I printed all the segments and the pin out of Black PLA. It didn't really work after putting it together because the circles were misshaped. 

#### Solution
I think this is because I printed it in a different orientation that I usually print it. I tried this different orientation because I didn't want to use support, but I will print again and see.

#### Testing and Identifying Problems
It worked! You should definitely print circles and arcs parallel to the print bed for better accuracy. 

Here's the assembled finger!
![image](/assets/fingerPrototype_v4_full_2.jpg)
It looks so clean compared to the old one.

## March 22nd, 2026 - Sunday
Today I want to continue modeling the hand and maybe code for a little bit. Let's get started!
### Design
Last week, I identified a few problems with the hand. One of which was that the string could not be routed so the finger ends up just hitting the string. I think I will completely redesign the hand because I now use 2mm holes instead of 3mm.

Drum Roll Please!

poof

![image](/assets/fullHandprototype_v2_1.png)

The hardest part was definitely making the holes for routing the fishing line. It took me a while for me to line the two holes up perfectly. 

I still need to make a way for the elastic cord to be routed and the thumb.

I'm not sure how I'll model the thumb because it behaves so much differently from the other fingers. Like the other fingers, it has 3 segments, but one segment is build into your palm, so I likely need to cut a hole in the palm to mount it. 

It's kinda crazy how important your thumb is to holding things. I don't thing you can grip things well without your thumbs. Like try gripping picking stuff up without your thumbs. You'll quickly miss using your thumbs.

I decided not to print out the palm yet because it takes around 50g of filament to print. I'm trying to save costs as much as possible so I'm holding off until I model the thumb. 

I think that's it for today! I'll probably code a little bit over the week and continue the design over the next weekend. I also have spring break next week so I hope to finish the design and get a lot of the code done then. 

## March 29th, 2026 - Sunday
Hi guys! Today, I'll design the thumb of the hand. Like I mentioned earlier, this will likely be the hardest part of the hand to model, simply because of the different mechanism.

### Design
![image](/assets/thumbPrototype_v1_3_1.png)

Here's my first prototype! modeled the first segment at an angle because your thumb's first section is shaped like a triangle. kinda...

I had a big of trouble modeling the holes because they didn't enter or exit on the same axis. However, I learned about the sweep cut tool in SolidWorks. It basically stitches your two holes on different faces together.

Thinking I had a good design, I decided to build the full thumb in assembly. I decided to use segments from the other fingers. 
![image](/assets/thumbPrototype_v1_full_1.png)

## March 30th, 2026 - Monday
Today, I started by finishing up the palm design.

### Design
Again, I used the sweep tool in SolidWorks to converge the fishing line from the fingers down to the wrist area. 
![image](/assets/palmPrototype_v4_1.png)

I also added the holes I need for the elastic cords to connect the the palm.
![image](/assets/palmPrototype_v4_2.png)

After that, I finished the assembly of the palm.
![image](/assets/fullHandprototype_v2_2.png)

To connect the 4 other fingers to the palm, I'm planning on printing a long rod so it'll be easy to pin 4 of them instead of having an individual pin for each finger. 

I'm pretty happy with this design. I'll have to print it all out and test it next.

## April 1st, 2026 - Wednesday
Happy April Fool's Day!

Today, I wanted to work on assembling and coding the hand. 

### Code
Through my research, I figured out how to have the microcontroller read my inputs to the serial monitor. I ran into some problems setting it up, but I think it's just a syntax problem.

I've referenced the example code in the Arduino docs and wrote code off of that to test out the serial monitor. The code is supposed to return the value that I put in, but it doesn't do that. Instead it returns a random string of numbers when I do. For example, when I input "1", it spits out "49 10"
![image](/assets/servoCode_1.png)

Okay... I've figured it out. After looking at the Arduino forums and docs, I found that I need to use "serial.parseInt" instead of "serial.read". Basically, "serial.parseInt" reads the whole string of numbers I give it and keeps it in decimal form. "serial.read" on the other hand, only reads the first number and converts it to ASCII.

After testing it, it now outputs the right numbers, but outputs a 0 after everytime I input. After reading a bit more, I found that I need to change the settings from "New Line" to "No Line Ending".

Next, I need to see how I'm gonna select a finger to control. I want to add a prefix to each number. The microcontroller will read the prefix, then the angle. This way, it'll know which finger I'm talking about when telling it an angle.

### Build
I printed out the parts for the thumb in PLA. 

![image](/assets/thumbPrototype_v1_full_2.jpg)

After building the thumb, I found that the holes from segments 2 and 3 aren't aligned well, so I decided to take another look at the assembly. 

In the assembly, the fingers weren't lining up either, so it wasn't a 3D printer problem. 

Turns out, I've been using the same cut path/angle for both the elastic cord and the fishing line. This is a problem because the hole for the elastic cord is longer than the hole for the fishing line. Although the path was perfect for the elastic cord, it wasn't for the fishing line. 

To solve this, I created a new path just for the fishing line. Now they line up perfectly in the assembly.

Another problem I faced when building the finger was the tolerances on the pin holes between each finger segment. The pins would just fall straight out. To solve this, I will change the rod diameter from 2mm to 2.2mm.

I also wanted to start building the electrical circuit for testing. Turns out, I was running super low on male to male Dupont wires, so I couldn't color coordinate the wires well. I also accidentally released the magic smoke on one of those breadboard power supplies.

Anyways, here's the final product:

![image](/assets/electronics_1.jpg)

Underwhelming? Yeah I swear I'll clean it up one day. The Dupont wires are coming on Friday, so I want to complete the code tomorrow. I'll also print the palm tomorrow. 

## April 2nd, 2026 - Thursday
Hello! Today, I'll finish the servo testing/callibration code.

I finally got it working! It now outputs the finger and the angle that I want. When I input "T90," it outputs "Thumb90". 

Now that it's working, let's move on to controlling actual servos. 

Under each of my elif statements, I've added a "fingerServo.write(servoAngle)" function.

![image](/assets/code_1.png)

The microcontroller should be able to control the servos now.

## April 3rd, 2026 - Friday
### Design
Hey guys! Today, I want to design the forearm where it will house the servos that control the movement of the fingers. It'll be difficult to cram 5 servos into the forearm, but I'll try my best to make it work. 

Now, I'm thinking of designing the forearm around the servo housing, so I will need to make the servo housing first. 

Since the forearm is wider than it is deep, I'm thinking of positioning the servos horizontally as opposed to vertically. 

This was my first design.
![image](/assets/forearm_v1_1.png)

I quickly noticed a problem in this design. Since the top and bottom servo would be in the same level, the string of the bottom servo would knock into the horn of the top servo. 

To negate the issue, I decided to position the servos kinda like this instead.

![image](/assets/forearm_v1_2.jpg)

Here's another design based off of that

![image](/assets/forearm_v1_3.png)

I dont really like this design either because it is too wide. I have one more design idea that might work. It involves stacking the servos vertically on it's side instead. 

![image](/assets/forearm_v1_4.png)

Although this sketch doesn't show much, I like this design way more since it expands vertically instead of horizontally. The only downside of this design is that the bottom servo has to be on the same height/direction of one of the other servos. This runs into the same problem that I addressed with my first design. I could fix this by making that final servo face forward instead of being on its side. 

I'll fix this problem and start extruding the forearm.

![image](/assets/forearm_v1_5.png)

I designed it so each servo can slot into it's designated slot. The each servo will also be screwed into the bar above for more security. I can then drop it right into the the forearm casing. 

I'm thinking of rotating the fifth servo casing 90 degrees. This will align it's horn to the middle of the forearm.

I'm done! 

![image](/assets/forearm_v1_6.png)

I added the screw holes and the proper casing for the rotated servo. I made the holes 2.9mm because I didn't have threaded inserts to make the hold stronger. 

Next, I'll print it out and test the tolerances for the print.

I KEEP MAKING THE SAME MISTAKES ON EVERY PRINTTTTTTTTTTT. I forgot to account for the wire stub again so it doesn't fit when the wire stub is facing the flat portion.

![image](/assets/forearm_v1_7.png)

The fix is rather simple: just narrow down the main body of the servo holder. It's kind of annoying that I made this mistake but at least it's a fairly easy fix.

Time to send the print to the printer!
### Code
Today, I also wanted to get started on the OpenCV code. I'm a beginner to python and I've never worked with the OpenCV library so it might be a bit difficult for me to program it.

Okay so this is way more complicated than I thought it would be. I think my goal for today will be for OpenCV to open my camera. 

After installing OpenCV, I decided to take a look at some of the example codes on the internet. I learned that you need to declare what camera you plan to use. Since I only have 1 camera, I used the default, "0"

Something cool thats kinda obvious now that I've learned about it is that OpenCV processes each frame individually instead of just looking at the video. I'm not sure if that makes sense or not. 

Anyways, after running my code, the window thats supposed to show what my camera sees just straight up crashed without displaying anything. After looking up my problem, I found out that I need to add a line of code that tells my PC how long the pictures need to be shown for, otherwise it'll overload the computer. 

After the fix, everything showed up fine! Until... I wanted to close the window, but it came back! I had indeed forgot to add a way to escape the "while True" loop.

Once again, Google came to the rescue and told me how to put in a line that would detect whenever the window is closed and terminate the running code.

AFTER ANOTHER GOOGLE SEARCH, I found out that "waitkey(1)" doesn't just wait until 1ms has passed, it outputs the ASCII code of the key that is pressed within that period! So, I just need to add an if statement that checks if that ASCII code is equivalent to, lets just say, the escape key. When I press the escape key, it should stop the program entirely.

And it works!

I still have a bit of time to work on the project today, so I'll get started on the hand tracking.

After some research, I found that there are two ways to do hand tracking, contour detection and landmark detection. contour detection works by detecting colors similar to the target. So it's kinda like a green screen thing. Landmark detection, on the other hand, works by plotting points at specific places on the target. So for your hands, it would plot points on each of your finger joints. I'll probably choose landmark detection because it seems cooler and more accurate. 

For landmark detection, I can use a library or train my own model. Since I'm still a beginner and short on time, I'll choose an existing library. One of these libraries is google's Media Pipeline. On it's website it says that its compatible with python, which is perfect for my project.

![image](/assets/MediaPipe.png)

Okay, apparently OpenCV outputs in BGR and MediaPipe reads in RGB, so I'll need to convert it. In the while loop, I'll add a function that automatically converts each frame after it is taken. I hope it doesn't add lag to the stream.

Something that I don't like about OpenCV is that it takes a long time to boot up after I run the code. I'm estimating around 1-2 minutes. I'm not sure what to do about it but yeah.

Anyways, I've converted the BGR to RGB so I'm kinda curious what everything will look like. Well, after I started the code, it looks identical so I'm not sure. Then I realized I forgot to change the image it's showing to the RGB feed. 

WOW it looks weird. Everythings more blue now instead of red. Anyways, back to coding.

All of the code that people have used in the past uses a different type of MediaPipe which uses different functions so it looks like I'm on my own.

This project is honestly a lot harder than I thought it'd be but I think I'm on the final stretch.

After running my code, I ran into the problem of "serial.serialutil.SerialException: could not open port 'COM3': PermissionError(13, 'Access is denied.', None, 5)". Another simple fix. I had the serial monitor running on Arduino IDE so it interfered with my python code.

After running into error after error, I decided to just use mediapipe's example code as a base to start off of.

Right off the bat, I was running into less errors. My goal is just to feed the camera stream into mediapipe's hand detection function, and it should just spit out a video that has hand detection. However, like everything, it isn't as simple as it seems. Running into more errors, I realized I need to have the bundle downloaded. After downloading the bundle, I still ran into more errors with the path to the bundle not being right, despite it being right. 

I decided to just go to bed since I was just tired of the errors. Maybe it'll fix its self tomorrow.

## April 4th, 2026 - Saturday
### Design
Last night, while waiting for OpenCV to boot up, I would work on attaching the servos to the servo mount. It's kind of impressive how heavy it is. I'm glad I decided to put it all in the forearm instead of the hand.
![image](/assets/forearm_v1_8.jpg)

Next I need to design a forearm where the hand will mount to. I'm thinking of making the bottom of the hand a little more narrow to look more like a hand. I also might have to change the location of the fishing line holes.

Progress Check!

![image](/assets/fullarm_v1_1.png)

I'm a little worried that the fishing line will be rubbing against things when being pulled and retracted, so I'll slip a piece of PTFE tubing over the line when I'm building it.

![image](//assets//fullarm_v1_2.png)

This is going to be what the final product is going to look like. I still have to make some minor adjustments but it should be ready for printing soon

![image](/assets/forearm_v1_9.png)

I added holes for the servo mount to screw into the back plate. I also added a big hole for the fishing line to come out of the hand and into the forearm. Lastly, I extruded a triangle support to help with the stress placed on the backplate. The sliced model came out to 73.4g, but I think I can get the model to weigh a bit less. 

Firstly, the big block supporting the last servo has no use since gravity is not pulling in the direction of the block. Removing this will remove a whopping 5g. I could also round out the corders of forearm. This brings the final filament cost to 65.8g. BUT WAIT, THERES MORE!! By reducing the infill percentage to 7%, I bring it down to 62g. 

Wow I saved a total of 10 cents...

Anyways let's print it out.

10% through the print, I realized that I did not add screw holes for attaching the hand to the forearm. I canceled the print and added the holes. I decided to print out the hand first at a smaller layer height to make the circles more circular.

After printing the palm out, I wanted to test out the tunnels for the fishing line, but I could not thread a line through any of the tunnels.

To solve this, I'll expand the holes to 2mm and redoing the paths.

I learned how to use 3D sketching to draw out proper paths for the sweep cuts. 3D sketching is kinda weird since I'm used to just sketching on a plane/face. I had to adjust each point in all 3 axis.

![image](/assets/palmPrototype_v4_5.png)

After slicing it it came out to 22g, cheaper than ever! It's probably because I used wider tunnels this time.

Next, I'll have to print out the fingers. For the big pin that connects the fingers to the palm, I'm planning on using filament as the pin. The filament I use has a thickness of 1.75mm. Although the holes of the finger are 2mm, I can use filament because of it's tendency to bend due to being on a spool.

Time for forearm print take 2. Slicer says it'll take 60g, so let's print it. It'll finish around midnight so I'll update you then.

### Code
AHHHH NO MORE CODE PLEASE.

Welcome back to the_idk's coding session where you see a beginner absolutely suffer through coding in python.

Today, I want to debug my code from yesterday and finally have hand tracking.

OMG IT FINALLY WORKS, I JUST MADE A TYPO!!! So a few minutes ago, I gave up and put my code into Claude, and it told me I just made a one word mistake. I'm kinda disappointed but at east it finally detects my hand.

![image](/assets/landmarkDetection.png)

This is so cool. I can't believe it actually works. 

Next, I'll move on to detecting whether each of my fingers are open are closed, then sending that to my microcontroller. I'll do this by comparing the node distance between each finger tip and and its respective MCP. The MCP is the joint that connects the finger to the palm.

## April 5th, 2026 - Sunday
### Build
Today, I want to assemble the whole hand and calibrate all the servos.

First, I need to assemble the hand. I inserted all the pins between each finger segment, binding the fingers together. After repeating that 5 times, I took a spool of filament and threaded it through MCPs. I also put in a pin for the thumb's MCP. 

After that, I threaded and tied all of the fishing line and elastic cord. I made sure it leave a lot of extra fishing line to ensure I'd have enough to tie onto the servo. 

Third, I threaded all the fishing line into the hole in the forearm and bolted down the hand. At first, I used a M3x16mm bolt and it didn't go down all the way. During my attempt of removing the screw, I stripped it's head. I had to use pliers to get the bolt out. I then replaced it with a M3x8mm bolt which fit perfectly.
![image](/assets/fullarm_v1_3.png)

Then, I bolted down the servo mount onto the forearm. I honestly think that I dont even need to screw it down, but it's better for strength and security.
![image](/assets/fullarm_v1_4.png)

### Testing
After I was done, I wanted to test each individual servo to see if it was working. I hooked up the top servo to my Arduino and PSU. However, when I said "T90," it spun, but started twitching like crazy. Looking it up, apparently I need to have a common ground between the servo and Arduino. This basically means that I need to bridge the grounds of my PSU and Arduino Uno. This was hard, since I somehow lost my breadboard, which my already sketchy wiring was going to be way worse.

After connecting the grounds, it seemed to work perfectly. I sent "T0," and it turned to 0 degrees. But when I sent "T180," it turned way past 180. Once again, my best friend, Google, comes to the rescue! The function, "servo.write(angle)," only works with 180 degree servos like the SG90. The servo library, however, does have another function, "servo.writeMicroseconds(Microseconds)". I'll have to tune the PWM signal now, not the angle. Which also means I have to rewrite some code. AHHHHHHHHHHHHHHHH

## April 6th, 2026 - Monday
Well, yesterday was the end of my spring break. I was hoping to finish this project but I guess not. 

I worked on the README and BOM of this project.

## April 10th, 2026 - Friday
Hey guys! The breadboards came earlier this week but I didn't come around to wiring up the hand until today. My wiring is kinda messy but it got the job done.

![image](/assets/electronics_2.jpg)

Unfortunately, one of the servos I bought spins in the opposite direction, so I'll have to swap its places with another servo, probably the middle one. It's a bit inconvenient but at least I don't have to buy a new servo.

I calibrated the servos that turn in the right direction. 1845 microseconds seems to be perfect for turning 180 degrees. 

Dang I wish VS Code had a spell check for markdown, I'm probably making so many spelling mistakes in this journal lol. 

WAIT THERE'S AN EXTENSION!!! Okay, so I just installed it and it shocked me how many spelling mistakes there are in my journal. I'm glad I downloaded it.

That's it for tonight, I'll hopefully finish calibrating the servos tomorrow.

## April 11th, 2026 - Saturday
Hey guys! Today I started by swapping the counter clockwise servo with the middle finger servo. 

Next, I want to make some adjustments to the python script. Since I changed the servo.write to servo.writemicroseconds, I need to swap out the 180 for 1845. 

Now, I want to test if the servos actually spin when I start the program.

Ther servos did not even move. After an hour of debugging, I finally found out that I need to use Serial.parseInt(SKIP_NONE). I think the parseInt was timing out so it didn't read all of the digits I was sending it. 

Now, I just need to tie down all the fishing line to the servo horns. 

You know what's funny about hardware? Everytime you think you're close to finishing your project, there's another problem that shows up out of nowhere. While I was trying to tie down the string to the servo, I found it very hard to tension the wire. Additionally, the wire is kind of stretchy, that didn't help with the tension either. A few weeks ago, I made a spool that attaches to the servo horn, but that design isn't good so I'll redesign it. For this new design, I want to take inspiration from [Made by Horizon](https://www.youtube.com/watch?v=aHFo-7ZK1Bk&t=697s), who made a really good spool roller for his hand. His spool design fits better onto the servo horns because it sits on top of it instead of in it, like mine does. His two sided design also makes it easier to print and construct.

![image](/assets/Horn_v2_1.png)

As opposed to Made by Horizon's project, I used one hole because I am not running a dual string system like he is. 

I'll be printing this prototype on my newly fixed Ender 3 because I'm printing something on my P1S right now. 

I also realized that I'll need to update the dimensions of the forearm so that it can freely rotate. The current backplate of the forearm doesn't let the horn rotate 360 degrees. Instead, it just blocks it from moving.

Actually... I think I'll just see if I can get away with not redesigning the forearm backplate.

After the the I printed out one of the spools, I noticed that it was way too thin. To fix this, I extruded the inner circle 3mm and the outer circle to 2mm.

Unfortunately, the old spools were so thin that they were cemented to the glass bed. It took some time, but I eventually got the spools off with my fingers. I then started the print using black PLA. Almost instantly, the print failed. I cleared the print bed and tried again... and again... and again. I had to reset it so many times that my P1S was done printing. I ended up just printing it on my P1S and it came out perfectly.

While attaching it to the servo, I found it very hard to thread the fishing line through the small hole. I also feel like the circumference was too small so the fishing line didn't really get pulled enough.

I designed a new one with a bigger thread hole and a larger circumference. However, this means I can't get away without making a new forearm back plate. Before designing a new backplate though, I want to test if this new spool is better.

While testing, I noticed that OpenCV would freeze up when I put my hand in front of my camera. It doesn't completely freeze up, but it works very slowly. To solve this, I decided to do some research. The first fix was to lower the camera resolution. 4k webcams, like mine, don't improve the accuracy of MediaPipe much, so it's just a performance sacrifice. I lowered by resolution to 480p, hoping for a fix. I also put in the "cv2.CAP_DSHOW" so that the program would boot up faster.

I did fix the slow boot up problem, but the lag was still there.

AHA! I found the fix! First, I fixed the code to only send updates to the Arduino if the my hand changed from open to close, or from closed to open. Also, I removed the delay I placed in the Arduino code that I forgot about. Finally, I changed the camera from 2fps to 4fps. 

Actually? I want to change it to 60fps. I don't think I'll have lag problems anymore. 

![image](/assets/landmarkDetection_2.png)

Next, I need to move on to my most dreaded task... Redesigning the forearm. I'll make a list of improvements I need to make below:

1. Make it wider, 10mm?
    - This is a maybe fix. I want to make the complete assembly first to see if I really need it.
2. Move hand to the front
    - The line is rubbing against sharp corners. 
    - It's also very hard to thread the fishing line if one is broken/needs to be replaced
3. Make the forearm deeper.
    - I'm not sure by how much yet. I haven't calculated it yet.

I just realized I have to reprint the whole forearm. Reminder to everyone making a project and myself. **ALWAYS** make a full assembly of your project before printing the parts out. You will make a mistake that you'll only find out near the end of your project. 

I can tell that I'm almost done with this project. But everytime I feel like that there's always another bug/design issue that I missed. 

Back to making the assembly. I made this servo model.

![image](/assets/servomodel_1.png)

Wait it's past midnight so I'll start another journal entry and push this to Github.

## April 12th, 2026 - Sunday
While testing my servos, I found that the monofilament fishing line I was using was deforming after stretching. This caused my robot to lose a ton of tension and not work anymore. Doing some research, I found that other people doing my project used braided fishing line instead. It's roughly the same cost, stronger, and not stretchy at all. 

Looking for the cheapest option, I went with [this](https://a.co/d/0gZXuDRI). It has 100lbs tensile strength, perfect for this project. 

Anyways, it's getting late, so I'll continue this in the morning. 

Good morning guys! Today, I want to finish the new assembly and print out the new parts I'll need. 

I started by finishing the assembly of the servo. 
![image](/assets/servomodel_2.png)

As you can see, I've modeled the original horn onto it. 

Next, I must redesign the servo mounts. 

I made each mount taller by around 18mm so that the horns can spin freely. 

![image](/assets/forearm_v2_1.png)

I also added the little wire stub that every servo has because I keep forgetting to account for that in my 3d prints.

Anyways, I just need to add the mount for the fifth servo and the screw holes and then I can remodel the back plate. 

![image](/assets/forearm_v2_2.png)

As you can see, I also made the legs a bit thinner to save on filament and time. Now I need to model the back plate. 

Here's the full new assembly of the arm!

![image](/assets/handAssembly_v2.png)

I don't like how there's so much behind it but I'm not sure how I would correct it. Other than that, I addressed all of my fixes. Moving the hand ensures that the every fishing line can reach each spool successfully. In my old design, the fishing line would run and rub into something. This adds friction and wears down the line. 

Anyways, I'm gonna print it and reconstruct the hand once the fishing line comes. 

## April 14th, 2026 - Tuesday
The fishing line arrived today! Right off the bat, I could tell that it was a lot stronger than the monofilament line I was using before. It also had no elasticity at all! When I was trying to cut it, it took a lot more effort. All in all, I think buying the new fishing line was a good choice. 

![image](/assets/newfishingline.png)

I disassembled the forearm and tried to restring the fishing line, but the new fishing line is double the thickness of the monofilament one. I think I'll have to expand the holes to 2mm instead of 1mm.

I only printed one finger of the new fingers so that I don't waste filament in case the holes are still too small. Thankfully, the holes were at the perfect size. The new finger feels a lot sturdier with the new fishing line as well. I dont know why.

![image](/assets/fingerPrototype_v4_full_3.png)

## April 15th, 2026 - Wednesday
Hey guys! Unfortunately, I was not able to work on the hand that much today because I came home really late today.

However, I did finish the finger redesigns by resizing the fishing line hole in the thumb segment. It was pretty easy since the paths were already planned out.

I sliced it in the slicer and used Bambu's Support for PLA as a support interface. I always either use Support for PLA or PETG as a support interface because it creates a smooth surface for the hinge mechanism.

![image](/assets/slicer_1.png)

As I'm writing this, I forgot to plug in the PTFE tube from the AMS to the main feeding tube for the extruder.  Gladly, I caught it early before it unspooled all the filament. 

Anyways, that's it for today! Waiting for the prints will take a while.

## April 16th, 2026
What's up guys! Today, I worked on reconstructing the hand. 

I first started by removing all of the support from the newly printed fingers. They basically fell of because of the support interface so it was really easy.

I then finished disassembling the old fingers so that I could reuse the old pins. I didn't want to reprint all the pins and waste filament. After I was done with that, I connected all the segments together. 

![image](/assets/fullHandprototype_v2_3.png)

I strung up all the elastic cord and then it was done! 

Next, I needed to finish reconstructing the forearm. I screwed in the servos into the new mount but my electric drill's battery was dying so I took a break to eat dinner while it charged.

After dinner, I finished screwing everything in and it looked really chunky. I'll fix this in future iterations.

Since the overall construction of the arm was done, I moved on to trying out the new fishing line. I had a bit of trouble tying the fishing line because it wouldn't stay tensioned. I eventually gave up and just decided to turn on the servo without fully tensioning it. To my surprise, it worked really well! The finger was able to pull all the way down.

![image](/assets/fullarm_v2_1.jpg)

Well that's it for today!

## April 17th, 2026 - Friday
It's finally the weekend! I can't wait to finish up this project. 

Now, something I didn't address yesterday was the flex of the back plate. When the string is pulled by the servos, the back plate tends to flex forward. On the old version, it didn't face this problem because it was not only smaller, but had a bit of support on the side. So to stop the flexing on the new design, I will model and print out supports for the top.

I just ended up extruding a long rectangular prism. I decided on a simple design because I dind't want to overcomplicate my current project too much. Here's the updated assembly!

![image](/assets/fullarm_v2_2.png) 

Like always, I'll print it in black PLA. 

I printed it out, but one of the sticks had a bit of problems with it's first layers. Additionally, everytime it would just fall out of the forearm everytime I try to fit it in. 

So, I redesigned it. I decided to use the existing screw holes from the hand. Now, it will mount securely onto the forearm, preventing any slippage. 

![image](/assets/support_1.png)

![image](/assets/fullarm_v2_3.png)

Earlier, I noticed that the string was losing tension, probably from my bad knots, so while I waited for the new support to print, I tried to untie it. However, I eventually gave up because it was taking too long and just cut it instead. Later, I plan to retie it tighter. 

## April 18th, 2026 - Saturday
Today I want to mount the support piece and redesign the spools. 

Installing the support was pretty easy.

I want to redesign the spool a little bit because the string was hard to attach when it was connected to the horn. The horn gets in the way of my fingers so I have to awkwardly push it in. 

For my first prototype, I made the side thinner again and a bit bigger. I can now use a 4mm hole instead of a 2mm, making it easier to push the string in. I also placed the hole for the string behind the horn instead of in front of it so it's now easier to push it in. 

![image](/assets/Horn_v2_2.png)

I sliced it at 100% infill because of how thin it is.

I screwed in the new horn once it was finished and it was really easy to tie down the fishing line. I started by setting every servo to 0 degrees. Then I screw down the new horn with the fishing line facing in the directions of the fingers. I make a loop around the spool so that the fishing line has a path to go through. Finally I tie the fishing line down.

![image](/assets/forearm_v2_3.png)

When testing, the hand worked perfectly with no problems! I'm finally so close to finishing! I'm so happy!

Next, I need to print out the rest of the spools so I can finish the rest of the hands

Sooooo I completely forgot that I need to calibrate each servo to a certain angle. The thumb servo went to it's max and broke my servo mount. So I'll have to reprint my servo mount. 

![image](/assets/broken_1.jpg)

I hope this doesnt mean I have to retie all the fishing line...

After the new mount finishes printing, I will calibrate all the servos.

Ayyy it's done printing!

I mounted all the servos to the servo mount and then I started calibrating. So far, each of the servos have had wildly different numbers. I only got three of the servos calibrated today: thumb, index, and middle. Since it's getting late, I'll probably calibrate the rest tomorrow. 

## April 19th, 2026 - Sunday
Hey guys! Today I wanted to redesign the forearm mount because of the lack of support. Even with the new support I added yesterday, it was still bending.

Like always, I want to model my parts so they use the least amount of support as possible. 

After thinking about it, I realized that I don't have to fully redesign the forearm back plate. I just need to add some parts to the support and cut more screw holes for the hand. 

First, I redesigned the support to screw in on both the top and bottom of the forearm. On the bottom, I will use two SHCS so that the bottom is flush with the table. On te top, I'll still stick with BHCS. 

I also extruded triangles on the top and bottom of the support to distribute the force of the servos. 
![image](/assets/support_2.png)

Lastly, I extruded a block on top of where the servo mount will sit. Since the servo mount pulls its self up when pulling down the servo, the block will hopefully absorb some of the force. 

Here's the full new design!

![image](/assets/forearm_v3_1.png)

Once the new parts finish printing, I'll put together the new, hopefully more strong arm!

Alright, it's done printing now and I put it all together. I forgot to mention this but I'm in the process of moving setups so all of my materials are split between two rooms. I have to run to and from that room when I'm missing a part. 

Somehow, one of the servos started spinning in one direction constantly, which I didn't even know was possible for a servo to do. I decided to just turn off the power supply. When I turned back on the power supply, it worked perfectly so I'm not sure what was wrong.

I also had a problem with the fingers getting stuck. It was probably a friction problem, but I don't have or know any lubricants that don't melt PLA. I just used a little water and it seemed to work. After the lubrication, none of the finger seemed to get stuck. 

Finally... the last part of the project... clicking run on the code...

AND IT WORKS!!!

FINALLY! AFTER 2 MONTHS OF WORK, ITS DONE!

![image](/assets/firehazard.jpeg)

Well, I think that's enough for today, I'll start preparing for submission tomorrow. 

## April 20th, 2026 - Monday
Since it's done, let's start prepping this for submission to fallout. 

Okay so apparently my project can't just be a big fire hazard so I'll clean it up.

To eliminate the breadboard, I'll solder all of the power cables together. I'll cut off one end of the dupont wire and solder the bare wire together. 

My soldered together wires looked kind of bad but they worked. 
![image](/assets/badlysolderedwires.jpeg)

I hooked everything back up and it looked way cleaner without the breadboard, I might also use some zip ties later to clean everything up. 

![image](/assets/nomorebreadboard.jpeg)

I felt kind of tired of working on the hardware so I just worked on organizing the repository for the rest of the day. 

## April 21st, 2026 - Tuesday
Happy tuesday! 

Today, I started by moving more files from my separate folder into the repository. I also added a bit more to the README. 

I opened up my assembly final to take another look at it, but turns out it broke somehow, so I had to re mate some parts. I also made it so the servo horn and spools actually line up in the assembly so I can properly define them. 

After I was done with the assembly, I wanted to render the 3D model in Blender, but after watching a few videos, I thought that it was way too complicated and decided to try and render it in SolidWorks. I added colored the support and servo mount white to act as a accent color. I also added a directional light which made it even better. Lastly, I added a scene and removed the cartoon lines from the edges of the parts. At first, I was admiring it, but then I noticed the jagged lines on the edge of the parts. I thought anti-aliasing was supposed to fix it, but I guess not.

![image](/assets/fullarm_v2_4.png)

Trying to fix this, I looked it up. Apparently I was supposed to use SolidWorks Visualize, which is SolidWork's rendering software, but it kept crashing. Doing some more research, I found that I probably needed to update my GPU drivers, but after I did, it still didn't work. 

Since It was getting late and I had some homework to do, I didn't dwell on it too much and decided to log off for the night. 

## April 22nd, 2026 - Wednesday
I didn't do much today, but I did work on the README! It looks a lot better since I took inspiration from notaroomba. 

I centered some of the titles and added the story of this project. Besides that, I didn't do much. 

![image](/assets/readme_1.png)