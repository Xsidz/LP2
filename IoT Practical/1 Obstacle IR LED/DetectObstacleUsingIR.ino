// Define the pin for the IR sensor
int irSensorPin = 2;   // OUT pin of IR sensor connected to digital pin 2
int ledPin = 12;        // Onboard LED pin (you can use another pin if needed)

void setup() {
  // Initialize the IR sensor pin as an input
  pinMode(irSensorPin, INPUT);
  
  // Initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);
  
  // Start serial communication for debugging (optional)
  Serial.begin(9600);
}

void loop() {
  // Read the state of the IR sensor
  int sensorValue = digitalRead(irSensorPin);
  
  // Print the sensor value to the serial monitor for debugging
  Serial.println(sensorValue);
  
  // If the sensor detects an object (LOW signal)
  if (sensorValue == LOW) {
    // Turn on the onboard LED
    Serial.println("Object Detected!");
    digitalWrite(ledPin, LOW);

  }
  // If no object is detected (HIGH signal)
  else {
    // Turn off the onboard LED
    Serial.println("No Object Detected!");
    digitalWrite(ledPin, HIGH);
  }

  // Add a small delay to avoid excessive serial printing
  delay(100);
}
