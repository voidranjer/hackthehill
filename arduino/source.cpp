const int ledPin1 = 11;
const int ledPin2 = 12;
const int ledPin3 = 13;
const int wait = 2000;
int incomingByte;      

void setup() {
  Serial.begin(9600);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == '1') {
      digitalWrite(ledPin1, HIGH);
      delay(wait);
      digitalWrite(ledPin1, LOW);
    }else if (incomingByte == '2') {
      digitalWrite(ledPin2, HIGH);
      delay(wait);
      digitalWrite(ledPin2, LOW);
    }else if (incomingByte == '3') {
      digitalWrite(ledPin3, HIGH);
      delay(wait);
      digitalWrite(ledPin3, LOW);
    }
  }
}