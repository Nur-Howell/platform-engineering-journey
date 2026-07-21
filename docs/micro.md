# Microproccesors 21 July 2026
- `Port B 0`
- `8-bit microcontroller`
- `Port can have a max of 8 pins`
- `GPIO (General Purpose I/O)`
- `Assign Input/Output to the pin`
## Arduino Functions
- `pinMode(pin, MODE)`
- `digitalRead(pin)`
- `digitalWrite(pin, VALUE)`
## Button Simulation
[Example](https://wokwi.com/projects/470150171830602753)
```
const int buttonPin = 2;

void setup() {
  
pinMode(buttonPin, INPUT);
Serial.begin(9600);

}

void loop() {
  
int buttonState = digitalRead(buttonPin);
Serial.println(buttonState);
delay(100);

}
```
Reading the state of the pin, pull down resistor allows for better accuracy.
`void setup()` allows to setup the configurations
`void loop()` allows for functionality

