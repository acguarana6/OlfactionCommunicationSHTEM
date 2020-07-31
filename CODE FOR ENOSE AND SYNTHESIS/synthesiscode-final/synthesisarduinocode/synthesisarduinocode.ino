String incomingNumber = "";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) 
  {
    // read the incoming byte:
    incomingNumber = Serial.readBytes(2); //this may not work; need to figure out reading

    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingNumber); //you guys don't need to print this, just decode it in a way that makes sense for you guys to use in your algorithm
  }
}
