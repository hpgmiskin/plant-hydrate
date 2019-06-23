#include "Arduino.h"
#include "printing_utilities.hpp"

#define WATER_SENSOR_PIN 14

void setup()
{
    initSerial();
    pinMode(WATER_SENSOR_PIN, INPUT);
}

void loop()
{
    const int sensor_value = analogRead(WATER_SENSOR_PIN);
    print("sensor_value: ", sensor_value);
    delay(1000);
}