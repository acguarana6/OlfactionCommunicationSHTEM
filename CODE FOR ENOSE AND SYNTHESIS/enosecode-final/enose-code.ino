#include <SoftwareSerial.h>
int counter = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.flush();
}

void loop() {
  // put your main code here, to run repeatedly:

  //here you would take the readings from all of your sensors:
  while(counter < 5) //assuming you are taking readings for 5 seconds
  {
    Serial.print(43.1); //ammonia reading
    Serial.print(",");
    Serial.print(54.1); //alcohol reading
    Serial.print(",");
    Serial.print(25.1); //hydrogen sulfide reading
    Serial.print(",");
    Serial.println(94.1); //formaldehyde reading
    
    delay(1000); //change this interval to how often you want to take readings
    counter++;
  }
  Serial.end();
  while(counter == 5) //effectively stops program here
  {
  }
}
