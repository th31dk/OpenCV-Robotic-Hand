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
This project originally started as a ASL Interpreter. However, while researching ways to teach it signs, I discovered computer vision and how you can make robots copy you. Last year, I went to Prototype, a hackathon hosted by Hack Club. There, we had to train these [SO-101 robotic arms](https://huggingface.co/docs/lerobot/en/so101) to perform certain actions. The teleoperator part of the training stuck to me the most, so this project was born!

Once you are done assembling the hand and connecting all the wires, you can just start up the python code and it'll start working automatically! Just hold out **ONE HAND** and start making gestures! 

## Assembly
## [Bill of Materials](/BOM.csv)
### Hardware
|Part Number|Part Name            |Quantity|Sourcing Link                                        |
|-----------|---------------------|--------|-----------------------------------------------------|
|1          |Arduino Uno          |1       |https://www.aliexpress.us/item/3256808569187520.html |
|2          |Breadboard           |1       |https://www.aliexpress.us/item/3256806927240551.html |
|3          |Dupont Wires         |17      |https://a.co/d/0hN85zCM                              |
|4          |External Power Supply|1       |https://a.co/d/045DWk0g                              |
|5          |PLA FIlament         |500g    |https://a.co/d/06X4XeTI                              |
|6          |DS3225 Servo         |5       |https://a.co/d/0iK4KOZB                              |
|7          |M3x10mm Bolt         |14      |https://www.aliexpress.us/item/=2255800794906149.html|
|8          |USB-A to USB-B Cable |1       |https://a.co/d/0aNsTbvj                              |
|9          |Webcam               |1       |https://a.co/d/0bebSZXz                              |
### 3D Printed Parts
3D files can be found [here](BOM.csv)
|Part Number|Part Name|Quantity|Material|Total Grams|
|-----------|---------|--------|--------|-----------|

### Wiring Diagram
![image](/assets/roboticHand_schematic_2.png)
### Credits
Thank you to:
Hack Club for supporting me throughout this project

Made by Horizon on Youtube for inspiring me to make this project. Check his [robotic hand](https://www.youtube.com/watch?v=aHFo-7ZK1Bk&t=697s) out!

MateoTechLab for making the amazing videos that encouraged me to make this and pursue hardware! Go watch his video [here](https://www.youtube.com/watch?v=NimROnJeQDY&t=253s)!

notaroomba for his amazing README layout! His [Trace](https://github.com/notaroomba/trace) project is super cool!