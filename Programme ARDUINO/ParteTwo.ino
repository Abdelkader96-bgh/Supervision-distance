#include <LiquidCrystal.h>;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup()
{
Serial.begin(9600);
lcd.begin(16, 2); 
lcd.clear();
pinMode(13,OUTPUT);
digitalWrite(13,LOW);
pinMode(10,OUTPUT);
digitalWrite(10,LOW);

}
void loop() {
          delay(1000);
          lcd.clear();
   double sensorValue1 = analogRead(A0);
   
   double sensorValue2 =  map(sensorValue1, 0, 1023, 0,5000);
   if(sensorValue2<1000) 
      { digitalWrite(13,HIGH);
        digitalWrite(10,LOW);
        lcd.setCursor(0,0);
        lcd.print("Erreur  ");
        //Serial.println("Erreur  ");
        lcd.setCursor(0,1);
        lcd.print("Coupure ligne");
        Serial.print("Erreur Coupure de ligne\n");
      }
   else
   {     digitalWrite(13,LOW);
         digitalWrite(10,HIGH);
   float  sensorValue3 = map(sensorValue2, 1000,5000, 0,100);
        lcd.setCursor(0,0);
        lcd.print("Level is (%) : ");
        lcd.setCursor(0,1);
        lcd.print(sensorValue3);
        Serial.print("Level is (%) :  ");
        Serial.println(sensorValue3);
   }
  
   delay(200);
 
   
  }

