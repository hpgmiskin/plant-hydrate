#include "Arduino.h"
#include "printing_utilities.hpp"

#define WATER_SENSOR_PIN 23

void setup()
{
    initSerial();
    pinMode(WATER_SENSOR_PIN, INPUT);
}

void loop()
{
    const int water_sensor = analogRead(WATER_SENSOR_PIN);
    print("water_sensor:", water_sensor);
    delay(10 * 1000);
}