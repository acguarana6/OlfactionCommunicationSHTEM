#include <ESP8266WiFi.h> 
#include <FirebaseArduino.h>

#define FIREBASE_HOST "testerdatabase-dd943.firebaseio.com"
#define FIREBASE_AUTH "P2HeSuA0wvHC9cqBMBNdQEwFi3vd92kFRGHSGmhT"

#define WIFI_SSID "insertwifissid"
#define WIFI_PASSWORD "insertwifipassword"

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(500);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  
  Serial.print("Connecting to "); Serial.print(WIFI_SSID);
  while (WiFi.status() != WL_CONNECTED) 
  {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("Connected to "); Serial.println(WIFI_SSID);
  Serial.print("IP Address is : "); Serial.println(WiFi.localIP());

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
}

void loop() {
  // put your main code here, to run repeatedly:

  //need to replace below line with getting JsonVariant type here.
  int x = Firebase.getInt("/toUser");

  //alternatively:
  FirebaseObject y = Firebase.get("/toUser");
  JsonVariant z = y.getJsonVariant("/toUser");

  if (isnan(x)) //could also use success() method
  {
    Serial.println("Failed to get final smell int.");
    return;
  }
  else
  {
    Serial.print("The final smell is smell "); Serial.println(x);
  }

  delay(100);
}
