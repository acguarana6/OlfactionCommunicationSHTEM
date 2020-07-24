#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>
 
// Set these to run example. 

#define FIREBASE_HOST "testerdatabase-dd943.firebaseio.com"
#define FIREBASE_AUTH "P2HeSuA0wvHC9cqBMBNdQEwFi3vd92kFRGHSGmhT"

#define WIFI_SSID "insertwifissid"
#define WIFI_PASSWORD "insertpassword"

void setup() { 
  Serial.begin(115200); 
 
  // connect to wifi. 
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD); 
  Serial.print("connecting"); 
  while (WiFi.status() != WL_CONNECTED) { 
    Serial.print("."); 
    delay(500); 
  } 
  Serial.println(); 
  Serial.print("connected: "); 
  Serial.println(WiFi.localIP()); 
   
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH); 
} 
 
void loop() { 
  Firebase.pushFloat("/smells", 42.1);
  delay(10000);
}
