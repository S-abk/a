#define PROXIMITY_PIN 7
#define LED_PIN LED_BUILTIN
#define DEBOUNCE_DELAY 50

bool lastProximityState = LOW;
bool currentProximityState = LOW;
unsigned long lastDebounceTime = 0;

void setup() {
  Serial.begin(9600);
  pinMode(PROXIMITY_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(LED_PIN, HIGH);
    } else if (command == '0') {
      digitalWrite(LED_PIN, LOW);
    }
  }

  int reading = digitalRead(PROXIMITY_PIN);
  if (reading != lastProximityState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > DEBOUNCE_DELAY) {
    if (reading != currentProximityState) {
      currentProximityState = reading;
      Serial.print("Proximity: ");
      if (currentProximityState == HIGH) {
        Serial.println("Detected");
      } else {
        Serial.println("Not Detected");
      }
    }
  }

  lastProximityState = reading;
  delay(100); // Read every 100ms
}
