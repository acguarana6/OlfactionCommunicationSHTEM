#include <ArduinoJson.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("working");
}

void loop() {
  // put your main code here, to run repeatedly:

//unpacking a JSON variant (synthesis will use this to obtain final int

  //creating a sample variant just for this code:
  //in real life, the variant will just be pulled from firebase.
  
  // allocate the memory for the document
  DynamicJsonDocument doc(1024);
  Serial.println("allocated the memory for the document.");

  //creates a JsonVariant in that memory space
  JsonVariant variant = doc.to<JsonVariant>();
  Serial.println("variant created");

  //adds these floats under their respective keys to the JsonVariant
  variant["finalint"] = 2;

  //prints out a serialized version of the JsonVariant
  Serial.println(serializeJson(doc, Serial));


  //in real life, this is where we would start after pulling the JsonVariant file under "toUser":

  //extract the integer from this JsonVariant: 
  JsonObject object = variant.as<JsonObject>();
  int x = object.getMember("finalint");
  Serial.print("The final smell is smell "); Serial.println(x);
  
  delay(10000);
}
