#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); 

String inputString = ""; 
bool messageReady = false;

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Waiting...");
}

void loop() {
  if (messageReady) {
    lcd.clear();
    if (inputString.length() > 16) {
      lcd.setCursor(0, 0);
      lcd.print(inputString.substring(0, 16));
      lcd.setCursor(0, 1);
      lcd.print(inputString.substring(16));
    } else {
      lcd.setCursor(0, 0);
      lcd.print(inputString);
    }

    Serial.print("LCD Updated: ");
    Serial.println(inputString);

    inputString = "";
    messageReady = false;
  }
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n' || c == '\r') {
      if (inputString.length() > 0) {
        messageReady = true;
      }
    } else {
      inputString += c;
    }
  }
}