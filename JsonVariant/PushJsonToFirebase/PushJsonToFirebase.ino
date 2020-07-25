#include <ArduinoJson.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("working");
}

void loop() {

//creating a JSON variant (we will use this on the e-nose side to send to Firebase)
  
  // allocate the memory for the document
  DynamicJsonDocument doc(1024);
  Serial.println("allocated the memory for the document.");

  //creates a JsonVariant in that memory space
  JsonVariant variant = doc.to<JsonVariant>();
  Serial.println("variant created");

  //adds these floats under their respective keys to the JsonVariant
  variant["alcohol"] = 43.1;
  variant["ethanol"] = 57.3;

  //prints out a serialized version of the JsonVariant
  Serial.println(serializeJson(doc, Serial));

  //we can push the variant directly to Firebase.

  delay(10000);
}
