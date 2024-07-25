#define PROXIMITY_PIN 7

void setup() {
  Serial.begin(9600);
  pinMode(PROXIMITY_PIN, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  int proximityState = digitalRead(PROXIMITY_PIN);
a#define LED_PIN LED_BUILTIN
#define PROXIMITY_PIN 7

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  pinMode(PROXIMITY_PIN, INPUT);
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

  int proximityState = digitalRead(PROXIMITY_PIN);
  Serial.print("Proximity: ");
  if (proximityState == HIGH) {
    Serial.println("Detected");
  } else {
    Serial.println("Not Detected");
  }
  delay(1000); // Read every second
}

  if (proximityState == HIGH) {
    Serial.println("Proximity: Detected");
  } else {
    Serial.println("Proximity: Not Detected");
  }

  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(LED_BUILTIN, HIGH);
    } else if (command == '0') {
      digitalWrite(LED_BUILTIN, LOW);
    }
  }

  delay(1000); // Read every second
}
