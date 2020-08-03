int counter = 0;

void setup() {
  Serial.begin(9600);
  Serial.flush();
  
}

void loop() {
 while(counter < 60)
 {
    const float AOUTpin0 = 0;
    float value0 = analogRead(AOUTpin0);
    const float AOUTpin1 = 1;
    float value1 = analogRead(AOUTpin1);
    const float AOUTpin2 = 2;
    float value2 = analogRead(AOUTpin2);
    const float AOUTpin3 = 3;
    float value3 = analogRead(AOUTpin3);
    const float AOUTpin4 = 4;
    float value4 = analogRead(AOUTpin4);
    const float AOUTpin5 = 5;
    float value5 = analogRead(AOUTpin5);
    
    Serial.print(value0); //MQ3B 
    Serial.print(",");
    Serial.print(value1); //MQ5
    Serial.print(",");
    Serial.print(value2); //MQ137
    Serial.print(",");
    Serial.print(value3); //MQ136
    Serial.print(",");
    Serial.print(value4); 
    Serial.print(",");
    Serial.println(value5); 
    
    delay(1000);
    counter++;
 }
 Serial.end();
 while(counter == 60)
 {
 }
}
