#include "Arduino.h"
#include "printing_utilities.hpp"

#define PUMP_PIN 15
#define WATER_SENSOR_PIN 14

void setup()
{
    // initSerial();
    pinMode(PUMP_PIN, OUTPUT);
    pinMode(WATER_SENSOR_PIN, INPUT);
}

void loop()
{
    // const int sensor_value = analogRead(WATER_SENSOR_PIN);
    // print("sensor_value: ", sensor_value);
    // delay(1000);
    digitalWrite(PUMP_PIN, HIGH);   // turn the relay on (HIGH is the voltage level)
    delay(2000);              // wait for a second
    digitalWrite(PUMP_PIN, LOW);    // turn the relay off by making the voltage LOW
    delay(2000);              // wait for a second
}