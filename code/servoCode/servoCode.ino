// Libraries
#include <Servo.h>

// Servo Names
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
thumbServo.attach(11);
thumbServo.attach(12);
thumbServo.attach(15);
thumbServo.attach(16);

// Serial Monitor
Serial.begin(9600);
Serial.print("Ready!");
}
void loop() {
  if (Serial.available() > 0) {
    servoAngle = Serial.read();
    
    Serial.println(servoAngle, DEC);
  }
}