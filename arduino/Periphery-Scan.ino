#include <Keypad.h>
/* Example sketch to control a 28BYJ-48 stepper motor with ULN2003 driver board and Arduino UNO. More info: https://www.makerguides.com */
// Include the Arduino Stepper.h library:
#include <Stepper.h>
#include <Wire.h>
#include <MechaQMC5883.h>
#include <dht.h>
#include <QuickMedianLib.h>
#define BUZZER_PIN  3
#define DHT11_PIN 2
dht DHT;
MechaQMC5883 qmc;
// Define number of steps per rotation:
const int stepsPerRevolution = 2048;
const int pingPin = 7; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 6; // Echo Pin of Ultrasonic Sensor
const byte ROWS = 4; //four rows
const byte COLS = 4; //four columns
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','.','D'}
};
byte rowPins[ROWS] = {22, 24, 26, 28}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {30, 32, 34, 36}; //connect to the column pinouts of the keypad
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

// Wiring:
// Pin 8 to IN1 on the ULN2003 driver
// Pin 9 to IN2 on the ULN2003 driver
// Pin 10 to IN3 on the ULN2003 driver
// Pin 11 to IN4 on the ULN2003 driver
int startseq = 0 ;
int loops = 1 ;
int incomingByte = 0;
int incoming = 0;
int endloops = 0;
int progrun = 0;
int i = 1;
int locarray[20];
String x = "";
String y = "";
String z = "";
String distance = "";
String locdig1 = "";
String locdig2 = "";
String locality = "";
int input = 0;
// Create stepper object called 'myStepper', note the pin order:
Stepper myStepper = Stepper(stepsPerRevolution, 8, 10, 9, 11);

void setup() {
  pinMode(40, OUTPUT);
  pinMode(42, OUTPUT);
  pinMode(44, OUTPUT);
  pinMode(46, OUTPUT);
  pinMode(48, OUTPUT);
  pinMode(50, OUTPUT);
  pinMode(52, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  // Set the speed to 5 rpm:
  myStepper.setSpeed(5);
  // Begin Serial communication at a baud rate of 9600:
  Serial.begin(9600);
  Wire.begin();
  Serial.begin(9600);
  qmc.init();
  //qmc.setMode(Mode_Continuous,ODR_200Hz,RNG_2G,OSR_256);
}

long microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}

void loop() {
  char key = keypad.getKey();
  if (key){
  digitalWrite(BUZZER_PIN, HIGH);
  delay(60);
  digitalWrite(BUZZER_PIN, LOW);
  }
  if (key == 'A') {
    Serial.println("Data");
    if (startseq == 0); {
      digitalWrite(40, HIGH);
      digitalWrite(42, HIGH);
      digitalWrite(44, LOW);
      digitalWrite(46, HIGH);
      digitalWrite(48, LOW);
      digitalWrite(50, HIGH);
      digitalWrite(52, HIGH);
      delay(1000);
      digitalWrite(52, LOW);
      digitalWrite(48, HIGH);
      digitalWrite(40, HIGH);
      delay(1000);
      digitalWrite(40, LOW);
      digitalWrite(42, LOW);
      digitalWrite(44, HIGH);
      digitalWrite(46, LOW);
      digitalWrite(50, LOW);
      delay(1000);
      digitalWrite(48, LOW);
      digitalWrite(44, LOW);
      digitalWrite(48, HIGH);
      digitalWrite(46, HIGH);
      myStepper.step(512);
      delay(500);
      startseq = startseq + 1 ;
    }
    long duration, inches, cm;
    pinMode(pingPin, OUTPUT);
    if (progrun == 0) {
      while (loops <=16) {
        long duration, inches, cm;
        pinMode(pingPin, OUTPUT);
        digitalWrite(BUZZER_PIN, HIGH);
        delay(1);
        digitalWrite(BUZZER_PIN, LOW);
        digitalWrite(pingPin, LOW);
        delayMicroseconds(2);
        digitalWrite(pingPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(pingPin, LOW);
        pinMode(echoPin, INPUT);
        duration = pulseIn(echoPin, HIGH);
        inches = microsecondsToInches(duration);
        cm = microsecondsToCentimeters(duration);
        Serial.println(inches);
        myStepper.step(-64);
        delay(1);
        loops = loops + 1;
      }
      loops = 1 ;
      digitalWrite(BUZZER_PIN, HIGH);
      delay(20);
      digitalWrite(BUZZER_PIN, LOW);
      digitalWrite(pingPin, LOW);
      delayMicroseconds(2);
      digitalWrite(pingPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(pingPin, LOW);
      pinMode(echoPin, INPUT);
      duration = pulseIn(echoPin, HIGH);
      inches = microsecondsToInches(duration);
      cm = microsecondsToCentimeters(duration);
      Serial.println(inches);
      Serial.println("Restart");
      digitalWrite(BUZZER_PIN, HIGH);
      delay(20);
      digitalWrite(BUZZER_PIN, LOW);
      endloops = endloops + 1;
    }
    if (endloops >= 1 and progrun == 0) {
      myStepper.step(512);
      digitalWrite(BUZZER_PIN, HIGH);
      delay(150);
      int chk = DHT.read11(DHT11_PIN);
      if (DHT.temperature != -999.0) {
        Serial.println("Temp + Humid");
        Serial.println(DHT.temperature);
        Serial.println(DHT.humidity); 
        delay(1000);
      }
      digitalWrite(BUZZER_PIN, LOW);
      Serial.println("Done!");
      progrun = 0;
      digitalWrite(48, HIGH);
      digitalWrite(46, HIGH);
      digitalWrite(50, HIGH);
      digitalWrite(52, HIGH);
      digitalWrite(40, HIGH);
      delay(300);
      digitalWrite(48, LOW);
      digitalWrite(46, LOW);
      digitalWrite(50, LOW);
      digitalWrite(52, LOW);
      digitalWrite(40, LOW);
      startseq = 0;
      endloops = 0;
    }
  }
  if (key == 'B') {
    input = 0; 
    if (input == 0) {
      digitalWrite(44, HIGH);
      digitalWrite(48, HIGH);
      digitalWrite(50, HIGH);
      while (input == 0){
        char key = keypad.getKey();
        if (key){
          locdig1 = String(key);
          digitalWrite(BUZZER_PIN, HIGH);
          delay(60);
          digitalWrite(BUZZER_PIN, LOW);
          input = 1;
        }
      }
      input = 0;
      while (input == 0){
        char key = keypad.getKey();
        if (key){
          locdig2 = String(key);
          digitalWrite(BUZZER_PIN, HIGH);
          delay(60);
          digitalWrite(BUZZER_PIN, LOW);
          input = 1;
          Serial.println("StatName:");
          Serial.println(locdig1 + "-" + locdig2); 
        }
      }
      digitalWrite(44, LOW);
      digitalWrite(48, LOW);
      digitalWrite(50, LOW);
    }
    input = 0;
    digitalWrite(42, HIGH);
    digitalWrite(46, HIGH);
    digitalWrite(50, HIGH);
    Serial.println("Distance:");
    if (z == "") { 
      while (input != 1) {
        char key = keypad.getKey();
        if (key){
          z = String(key);
          digitalWrite(BUZZER_PIN, HIGH);
          delay(60);
          digitalWrite(BUZZER_PIN, LOW);
          input = 1;
        }
      }
      input = 0;
      while (input != 1) {
        char key = keypad.getKey();
        if (key){
          z = z + String(key);
          digitalWrite(BUZZER_PIN, HIGH);
          delay(60);
          digitalWrite(BUZZER_PIN, LOW);
          input = 1;
        }
      }
      input = 0;
      while (input != 1) {
        char key = keypad.getKey();
        if (key){
          z = z + String(key);
          digitalWrite(BUZZER_PIN, HIGH);
          delay(60);
          digitalWrite(BUZZER_PIN, LOW);
          input = 1;
        }
      }
      input = 0;
      digitalWrite(BUZZER_PIN, HIGH);
      delay(120);
      digitalWrite(BUZZER_PIN, LOW);
      distance = z;
      Serial.println(distance);
      z = "";
      delay(500);
      digitalWrite(40, LOW);
      digitalWrite(42, LOW);
      digitalWrite(44, LOW);
      digitalWrite(46, LOW);
      digitalWrite(48, LOW);
      digitalWrite(50, LOW);
    }
    //Get angles N stuff
    i = 1;
    int i1= 0;
    Serial.println("Angles:");
    while (i <= 150) {
      if (i1 == 0) {
        digitalWrite(44, HIGH);
      }
      else if (i1 == 1) {
        digitalWrite(46, HIGH);
      }
      else if (i1 == 2) {
        digitalWrite(48, HIGH);
      }
      else if (i1 == 3) {
        digitalWrite(50, HIGH);
      }
      else if (i1 == 4) {
        digitalWrite(52, HIGH);
      }
      else if (i1 == 5) {
        digitalWrite(40, HIGH);
      }
      else if (i1 == 6) {
        digitalWrite(42, HIGH);
      }
      int x, y, z;
      int azimuth;
      //float azimuth; //is supporting float too
      qmc.read(&x, &y, &z,&azimuth);
      //azimuth = qmc.azimuth(&y,&x);//you can get custom azimuth
      Serial.print("x: ");
      Serial.print(x);
      Serial.print(", y: ");
      Serial.print(y);
      Serial.print(", z: ");
      Serial.print(z);
      Serial.print(", a: ");
      Serial.print(azimuth);
      Serial.println();
      delay(100);
      if (i1 == 0) {
        digitalWrite(44, LOW);
        i1 = i1 + 1;
      }
      else if (i1 == 1) {
        digitalWrite(46, LOW);
        i1 = i1 + 1;
      }
      else if (i1 == 2) {
        digitalWrite(48, LOW);
        i1 = i1 + 1;
      }
      else if (i1 == 3) {
        digitalWrite(50, LOW);
        i1 = i1 + 1;
      }
      else if (i1 == 4) {
        digitalWrite(52, LOW);
        i1 = i1 + 1;
      }
      else if (i1 == 5) {
        digitalWrite(40, LOW);
        i1 = i1 + 1;
      }
      else if (i1 == 6) {
        digitalWrite(42, LOW);
        i1 = 0;
      }
      i = i + 1;
    }
  }
  if (key == 'C') {
    Serial.print("Rewrite");
  }
}
