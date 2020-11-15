#include <Servo.h>

#define OnTekerCm 18
#define OnArkaCm 32

#define SOL 430
#define SAG -430

Servo solTeker, sagTeker; 
Servo solMotor, sagMotor;

//Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);

String gelenMesaj, subStringOne, subStringTwo, gidenMesaj;
int hiz, aci;
//sensors_event_t event;

int TekerDon(int Degree) {
    //Serial.print("Fonksiyona Su sayı geldi: "); Serial.println(Degree);
  if (Degree < 25 && Degree > -25) return Degree;
  
  int isaret = 0;
  if (Degree < 0) {isaret = 1; Degree = -Degree;}
  
  double Derece = Degree / 10.0;
  Derece = Derece * 3.141592 / 180;
  
  double DigerTekerDerece = atan(1/((OnArkaCm * tan(3.141592/2 - Derece) + OnTekerCm) / OnArkaCm));
  DigerTekerDerece = DigerTekerDerece * 180 / 3.141592;
  
  int DigerTekerDegree = DigerTekerDerece * 10;
  if (isaret) DigerTekerDegree = -DigerTekerDegree;
  
  return DigerTekerDegree;
}

void acilariTekereYazdir(int aci1, int aci2) {
  //delay(600);
  if (aci1 < 0) {
    //Serial.print(aci1); Serial.print(" "); Serial.println(aci2);
    //Serial.print("sağa dönüyor sağ tekerin açısı: "); Serial.println(aci1);
    //Serial.print("sol tekerin açısı: "); Serial.println(aci2);
    aci1 = map(aci1, -430, 310, 25, 90);
    aci2 = map(aci2, -310, 430, 47, 115);
    aci1 = constrain(aci1, 25, 90);
    aci2 = constrain(aci2, 47, 115);
    sagTeker.write(aci1);
    solTeker.write(aci2);   
    ///solTeker.write(47);//sol=115, orta=70, sag=47
    ///sagTeker.write(25);//sol=90, orta=62, sag=25
  }
  else {
    //Serial.print(aci2); Serial.print(" "); Serial.println(aci1);
    //Serial.print("sola dönüyor sol tekerin açısı: "); Serial.println(aci1);
    //Serial.print("sağ tekerin açısı: "); Serial.println(aci2);
    aci1 = map(aci1, -310, 430, 47, 115);
    aci2 = map(aci2, -430, 310, 25, 90);
    aci1 = constrain(aci1, 47, 115);
    aci2 = constrain(aci2, 25, 90);
    solTeker.write(aci1);
    sagTeker.write(aci2);  
  }
}

void setup() {
  solMotor.attach(7);
  sagMotor.attach(6);
  //bno.begin();
  //delay(1000);
  Serial.begin(230400);
  Serial.setTimeout(10);
  solMotor.writeMicroseconds(1000);
  sagMotor.writeMicroseconds(1000);
  delay(6000);
  //bno.setExtCrystalUse(true);
solTeker.attach(4);
sagTeker.attach(5);

sagTeker.write(70);
solTeker.write(70);

}

void loop() {
  if (Serial.available()) {
    gelenMesaj = Serial.readString();
    subStringOne = gelenMesaj.substring(0, 3);
    subStringTwo = gelenMesaj.substring(4, 7);
    hiz = subStringOne.toInt();
    aci = subStringTwo.toInt();
    aci = constrain(aci, 100, 960);
    aci = aci - 530;
    hiz = constrain(hiz, 100, 200);
    hiz = hiz * 10;
    hiz = constrain(hiz, 1000, 1250);
    sagMotor.writeMicroseconds(hiz);
    solMotor.writeMicroseconds(hiz);
    acilariTekereYazdir(aci, TekerDon(aci));
    //bno.getEvent(&event);
    //gidenMesaj = String(event.orientation.x)+ String(" ") + String(event.orientation.y) + String(" ") + String(event.orientation.z);
    Serial.print(hiz); Serial.print("  "); Serial.println(aci);
  }

}
