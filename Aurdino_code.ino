const int ledPins[] = { 8, 9, 10,11,12};  // Replace with your LED pin numbers
const int numLeds = sizeof(ledPins) / sizeof(ledPins[0]);
void setup() {
  Serial.begin(9600);
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}
void loop() {
  if (Serial.available() > 0) {
    int fingers_up = Serial.parseInt();
    for (int i = 0; i < numLeds; i++) {
      if (i < fingers_up) {
        digitalWrite(ledPins[i], HIGH);
      } else {
        digitalWrite(ledPins[i], LOW);
      }
    }
  }
}
