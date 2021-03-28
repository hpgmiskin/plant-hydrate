#include "Arduino.h"

void initSerial(int baud = 9600)
{
    while (!Serial)
    {
        delay(10);
    }
    Serial.begin(baud);
}

template <class Type>
void print(Type arg)
{
    Serial.println(arg);
}

template <class T1, class T2, class... Ts>
void print(T1 arg1, T2 arg2, Ts... args)
{
    Serial.print(arg1);
    print(arg2, args...);
}
