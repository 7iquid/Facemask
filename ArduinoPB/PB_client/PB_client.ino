// Complete Instructions: https://RandomNerdTutorials.com/esp8266-nodemcu-digital-inputs-outputs-arduino/

// set pin numbers
const int buttonPin1 = 3;     // the number of the pushbutton pin
const int buttonPin2 = 5;     // the number of the pushbutton pin
const int ledPin =  LED_BUILTIN; 
const int greedLED =  2;
// const int ledPin2 =  6;       // the number of the LED pin

// variable for storing the pushbutton status
int buttonState = 0;
// int buttonState2 = 0;
// bool buttonStatus = false;

void setup() {
	Serial.begin(115200); 
  // initialize the pushbutton pin as an input
  pinMode(buttonPin1, INPUT);
  // initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);
  pinMode(greedLED, OUTPUT);
}

void loop() {

  digitalWrite(ledPin, LOW);   // Turn the LED on (Note that LOW is the voltage level
  digitalWrite(greedLED, LOW);
  Serial.println("high Starte");
  // but actually the LED is on; this is because
  // it is active low on the ESP-01)
  delay(1000);                      // Wait for a second
  digitalWrite(ledPin, HIGH);  // Turn the LED off by making the voltage HIGH
  digitalWrite(greedLED, HIGH);
  Serial.println("low Starte");
  delay(2000);   


}
