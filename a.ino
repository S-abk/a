#define PROXIMITY_PIN 7

void setup() {
  Serial.begin(9600);
  pinMode(PROXIMITY_PIN, INPUT);
}

void loop() {
  int proximityState = digitalRead(PROXIMITY_PIN);

  Serial.print("Proximity: ");
  if (proximityState == HIGH) {
    Serial.println("Detected");
  } else {
    Serial.println("Not Detected");
  }

  delay(1000); // Read every second
}
