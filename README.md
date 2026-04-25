<h1 align="center">
    EchoHand
</h1>
<h4 align="center">
    A robot hand that mirror's your every gesture
</h4>

![image](/assets/fullarm_v2_4.png)

<h2 align="center">
A Bit About This Project
</h2>
This project originally started as a ASL Interpreter. However, while researching ways to teach it signs, I discovered computer vision and how you can make robots copy you. Last year, I went to Prototype, a hackathon hosted by Hack Club. There, we had to train these SO-101 Robotic Arms to perform certain actions. The teleoperator part of the training stuck to me the most, so this project was born!

Once you are done assembling the hand and connecting all the wires, you can just start up the python code and it'll start working automatically. Just hold out a hand and start making gestures! 

## Assembly
### Hardware
#### [Bill Of Materials](/BOM)
|Part Number|Part Name            |Quantity|Sourcing Link                                       |Cost  |Notes|
|-----------|---------------------|--------|----------------------------------------------------|------|-----|
|1          |Arduino Uno          |1       |https://www.aliexpress.us/item/3256808569187520.html|$5.65 |     |
|2          |Breadboard           |1       |https://www.aliexpress.us/item/3256806927240551.html|$1.92 |     |
|3          |Dupont Wires         |17      |https://a.co/d/0hN85zCM                             |$8.99 |     |
|4          |External Power Supply|1       |https://a.co/d/045DWk0g                             |$59.99|     |
|5          |DS3225 Servo         |5       |https://a.co/d/0iK4KOZB                             |$90.00|     |
|6          |M3x10mm Bolt         |16      |https://www.aliexpress.us/item/2255800794906149.html|$1.86 |     |
|7          |USB-A to USB-B Cable |1       |https://a.co/d/0aNsTbvj                             |$7.21 |     |
|8          |Webcam               |1       |https://a.co/d/0bebSZXz                             |$25.00|     |
|9          |Fishing Line         |2000mm  |https://a.co/d/07G4QxGr                             |$9.98 |     |
|10         |Elastic Cord         |600mm   |https://a.co/d/07XXOlZX                             |$9.99 |     |
### 3D Printed Parts
3D files can be found [here](/Print%20Files/)

|Part Number|Part Name            |Quantity|Material                                            |Total Grams|Notes                        |
|-----------|---------------------|--------|----------------------------------------------------|-----------|-----------------------------|
|1          |Finger 1             |5       |PLA                                                 |17.69      |                             |
|           |                     |        |PETG                                                |0.34       |PETG for easy support removal|
|2          |Finger 2             |5       |PLA                                                 |20.15      |                             |
|           |                     |        |PETG                                                |0.38       |PETG for easy support removal|
|3          |Finger 3             |4       |PLA                                                 |14.95      |                             |
|           |                     |        |PETG                                                |0.37       |PETG for easy support removal|
|4          |Thumb                |1       |PLA                                                 |7.33       |                             |
|           |                     |        |PETG                                                |0.77       |PETG for easy support removal|
|5          |BackStand            |1       |PLA                                                 |133.6      |                             |
|6          |Palm                 |1       |PLA                                                 |28.9       |                             |
|7          |Pin                  |11      |PLA                                                 |0.71       |                             |
|8          |Spool                |10      |PLA                                                 |23.44      |                             |
|9          |Support              |1       |PLA                                                 |44.39      |                             |

### Wiring Diagram
![image](/assets/finalSchematic.png)
### Credits
Thank you to:
Hack Club for supporting me throughout this project

Made by Horizon on Youtube for inspiring me to make this project. Check his [robotic hand](https://www.youtube.com/watch?v=aHFo-7ZK1Bk&t=697s) out!

MateoTechLab for making the amazing videos that encouraged me to make this and pursue hardware! Go watch his video [here](https://www.youtube.com/watch?v=NimROnJeQDY&t=253s)!

notaroomba for his amazing README layout! His [Trace](https://github.com/notaroomba/trace) project is super cool!