
// Libraries
#include <Servo.h>

Servo thumbServo;
Servo indexServo;
Servo middleServo;
Servo ringServo;
Servo pinkyServo;

// Variables
char finger = 'T';
int servoAngle = 0;

void setup() {
// Pin Assignments
thumbServo.attach(3);
indexServo.attach(5);
middleServo.attach(6);
ringServo.attach(9);
pinkyServo.attach(10);

// Serial Monitor
Serial.begin(9600);
Serial.print("Ready!");
}

void loop() {
  if (Serial.available() > 0) {
    char finger = Serial.read();
    int servoAngle = Serial.parseInt();
    
    if (finger == 'T') {
      Serial.print("Thumb");
      thumbServo.write(servoAngle);
    }
      else if (finger == 'I') {
        Serial.print("Index"); 
        indexServo.write(servoAngle);
      }
      else if (finger == 'M') {
        Serial.print("Middle");
        middleServo.write(servoAngle);
      }
      else if (finger == 'R') {
        Serial.print("Ring");
        ringServo.write(servoAngle);
      }
      else if (finger == 'P') {
        Serial.print("Pinky");
        pinkyServo.write(servoAngle);
      }
    }
  
    Serial.println(servoAngle);
  
}