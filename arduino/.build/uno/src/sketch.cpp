#include <Arduino.h>

void setup();
void loop();
#line 1 "src/sketch.ino"

int ledPin = 13;                 // LED connected to digital pin 13
int buttonPin = 12;                 // Button connected to digital pin 12
char incomingByte = 0; 
int buttonPressed = false;
void setup()
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);      // sets the digital pin as output
  pinMode(buttonPin, OUTPUT);      // sets the digital pin as output
}

void loop()
{
if(Serial.available()>0)
  {
    incomingByte = Serial.read();
    if(incomingByte == 'p')
    {
      digitalWrite(ledPin, HIGH);   // sets the LED on
      digitalWrite(buttonPin, HIGH);   // sets the LED on
      Serial.println("pressed");
      delay(1000);                  // waits for a second

    } 
    else if(incomingByte == 'u')
    {
      Serial.println("unpressed");
      digitalWrite(ledPin, LOW);    // sets the LED off
      digitalWrite(buttonPin, LOW);    // sets the LED off
      delay(1000);                  // waits for a second
    }
}
}






