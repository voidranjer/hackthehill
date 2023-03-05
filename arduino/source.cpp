
const int ledPin1 = 10;
const int ledPin2 = 11;
const int ledPin3 = 12;
const int ledPin4 = 13;
const int wait = 1000;
int incomingByte;      

void setup() {
  Serial.begin(9600);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == '1') {
      digitalWrite(ledPin1, HIGH);
    }else if (incomingByte == '2') {
      digitalWrite(ledPin2, HIGH);
    }else if (incomingByte == '3') {
      digitalWrite(ledPin3, HIGH);
    }else if (incomingByte == '4') {
      digitalWrite(ledPin4, HIGH);
    }else if (incomingByte == '5') {
      digitalWrite(ledPin1, LOW);
      digitalWrite(ledPin2, LOW);
      digitalWrite(ledPin3, LOW);
      digitalWrite(ledPin4, LOW);
    }
  }
}
