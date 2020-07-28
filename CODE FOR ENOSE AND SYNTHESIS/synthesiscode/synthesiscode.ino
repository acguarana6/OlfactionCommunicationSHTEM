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
  //the first part to this is sending the "ready" signal to Firebase in the Signal folder under the tag "key":
  Firebase.pushString(firebaseData, "/Signal", "enteryourreadysignalhere");

  //the next part fo synthesis is pulling the final int
  //uniquekey will be the key that the synthesis device pushes to Firebase as the ready signal

  //We will have to extract the full JSON file at the uniquekey location and cycle through it to find the final int
  Firebase.getJSON(firebaseData, "/enteryourreadysignalhere");
  FirebaseJson json = firebaseData.jsonObject(); 

  FirebaseJsonData jsonData;
  json.get(jsonData, "enteryourreadysignalhere/finalint");
  int finalInt = jsonData.intValue;
}
