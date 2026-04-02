
// Libraries
#include <Servo.h>

Servo thumbServo;
Servo indexServo;
Servo middleServo;
Servo ringServo;
Servo pinkyServo;

// Variables
int(servoAngle) = 0;

void setup() {
// Pin Assignments
thumbServo.attach(5);
indexServo.attach(11);
middleServo.attach(12);
ringServo.attach(15);
pinkyServo.attach(16);

// Serial Monitor
Serial.begin(9600);
Serial.print("Ready!");
}

void loop() {
  if (Serial.available() > 0) {
    
    servoAngle = Serial.parseInt();
    
    Serial.println(servoAngle);
  }
}