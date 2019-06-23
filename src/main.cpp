#include "Arduino.h"
#include "printing_utilities.hpp"

#define PUMP_PIN 15
#define WATER_SENSOR_PIN 14
#define NEEDS_WATER_THRESHOLD 120

void setup()
{
    initSerial();
    pinMode(PUMP_PIN, OUTPUT);
    pinMode(WATER_SENSOR_PIN, INPUT);
}

void loop()
{
    const int water_level = analogRead(WATER_SENSOR_PIN);
    print("water_level: ", water_level);
    if (water_level < NEEDS_WATER_THRESHOLD){
        print("enable pump");
        digitalWrite(PUMP_PIN, HIGH);
    } else {
        print("disable pump");
        digitalWrite(PUMP_PIN, LOW);
    }
    delay(5000);
}