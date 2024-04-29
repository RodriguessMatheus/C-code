// C++ code
//
int vermelhoPin = 10;
int laranjaPin = 9;
int azulPin = 8;
int verdePin = 7;

void setup()// função chamada setup
{
  pinMode(vermelhoPin, OUTPUT);
  pinMode(laranjaPin, OUTPUT);
  pinMode(azulPin, OUTPUT);
  pinMode(verdePin, OUTPUT);
}

void loop()
{
  digitalWrite(verdePin, HIGH);
  digitalWrite(azulPin, LOW);
  digitalWrite(laranjaPin, LOW);
  digitalWrite(vermelhoPin, LOW);
  delay(2000); 
   digitalWrite(verdePin, LOW);
  digitalWrite(azulPin, HIGH);
  digitalWrite(laranjaPin, LOW);
  digitalWrite(vermelhoPin, LOW);
  delay(2000);
  digitalWrite(verdePin, LOW);
  digitalWrite(azulPin, LOW);
  digitalWrite(laranjaPin, HIGH);
  digitalWrite(vermelhoPin, LOW);
  delay(2000); 
   digitalWrite(verdePin, LOW);
  digitalWrite(azulPin, LOW);
  digitalWrite(laranjaPin, LOW);
  digitalWrite(vermelhoPin, HIGH);
  delay(2000);  
  digitalWrite(verdePin, HIGH);
  digitalWrite(azulPin, HIGH);
  digitalWrite(laranjaPin, LOW);
  digitalWrite(vermelhoPin, LOW);
  delay(2000);  
   digitalWrite(verdePin, LOW);
  digitalWrite(azulPin, LOW);
  digitalWrite(laranjaPin, HIGH);
  digitalWrite(vermelhoPin, LOW);
  delay(2000);
   digitalWrite(verdePin, LOW);
  digitalWrite(azulPin, HIGH);
  digitalWrite(laranjaPin, HIGH);
  digitalWrite(vermelhoPin, LOW);
  delay(2000);
  digitalWrite(verdePin, HIGH);
  digitalWrite(azulPin, HIGH);
  digitalWrite(laranjaPin, HIGH);
  digitalWrite(vermelhoPin, LOW);
  delay(2000);
  digitalWrite(verdePin, LOW);
  digitalWrite(azulPin, LOW);
  digitalWrite(laranjaPin, LOW);
  digitalWrite(vermelhoPin, HIGH);
  delay(2000);
  digitalWrite(verdePin, HIGH);
  digitalWrite(azulPin, LOW);
  digitalWrite(laranjaPin, LOW);
  digitalWrite(vermelhoPin, HIGH);
  delay(2000);
  digitalWrite(verdePin, HIGH);
  digitalWrite(azulPin, LOW);
  digitalWrite(laranjaPin, LOW);
  digitalWrite(vermelhoPin, HIGH);
  delay(2000);
  digitalWrite(verdePin, LOW);
  digitalWrite(azulPin, HIGH);
  digitalWrite(laranjaPin, LOW);
  digitalWrite(vermelhoPin, HIGH);
  delay(2000);
  digitalWrite(verdePin, HIGH);
  digitalWrite(azulPin, HIGH);
  digitalWrite(laranjaPin, LOW);
  digitalWrite(vermelhoPin, HIGH);
  delay(2000);
  digitalWrite(verdePin, LOW);
  digitalWrite(azulPin, LOW);
  digitalWrite(laranjaPin, HIGH);
  digitalWrite(vermelhoPin, HIGH);
  delay(2000);
  digitalWrite(verdePin, HIGH);
  digitalWrite(azulPin, LOW);
  digitalWrite(laranjaPin, HIGH);
  digitalWrite(vermelhoPin, HIGH);
  delay(2000);
  digitalWrite(verdePin, LOW);
  digitalWrite(azulPin, HIGH);
  digitalWrite(laranjaPin, HIGH);
  digitalWrite(vermelhoPin, HIGH);
  delay(2000);
  digitalWrite(verdePin, HIGH);
  digitalWrite(azulPin, HIGH);
  digitalWrite(laranjaPin, HIGH);
  digitalWrite(vermelhoPin, HIGH);
  delay(2000);
               
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
}
