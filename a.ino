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
  int reading = digitalRead(PROXIMITY_PIN);

  // Check if the reading has changed
  if (reading != lastProximityState) {
    lastDebounceTime = millis();
  }

  // If the reading is stable for a period longer than the debounce delay, update the state
  if ((millis() - lastDebounceTime) > DEBOUNCE_DELAY) {
    if (reading != currentProximityState) {
      currentProximityState = reading;

      // Invert the logic here: HIGH means not detected, LOW means detected
      Serial.print("Proximity: ");
      if (currentProximityState == LOW) { // Adjusted logic
        Serial.println("Detected");
        digitalWrite(LED_PIN, HIGH);  // Turn on LED when proximity is detected
      } else {
        Serial.println("Not Detected");
        digitalWrite(LED_PIN, LOW);   // Turn off LED when no proximity is detected
      }
    }
  }

  lastProximityState = reading;
  delay(100); // Check every 100ms
}
