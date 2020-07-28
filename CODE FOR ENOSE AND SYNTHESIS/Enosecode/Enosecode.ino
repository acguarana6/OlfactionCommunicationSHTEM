//documentation for FirebaseESP8266 library: https://github.com/mobizt/Firebase-ESP8266

#include <FirebaseESP8266.h> //you will have to install Firebase ESP8266 Client library
#include <FirebaseESP8266HTTPClient.h>
#include <FirebaseFS.h>
#include <FirebaseJson.h>

#include <ESP8266WiFi.h> //you will have to run this code on the ESP8266 board and not the Arduino Uno.

FirebaseData firebaseData;

#define WIFI_SSID "insertwifissid"
#define WIFI_PASSWORD "insertwifipassword"

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(500);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Firebase.begin("testerdatabase-dd943.firebaseio.com", "P2HeSuA0wvHC9cqBMBNdQEwFi3vd92kFRGHSGmhT");
}

void loop() {
  // every time the sensors collect a new round of data:
  
  FirebaseJson json;
  json.set("sensor1", 42.1);
  json.set("sensor2", 34.1);
  json.set("sensor3", 34.1);
  json.set("sensor4", 34.1);

  Firebase.pushJSON(firebaseData, "/smells", json);

  //delay however long you guys want
  delay(10000);
  
}
