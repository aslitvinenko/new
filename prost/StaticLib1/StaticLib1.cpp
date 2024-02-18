// StaticLib1.cpp : Определяет функции для статической библиотеки.
//

#include "pch.h"
#include "framework.h"
#include <cmath>
int prost(int n)
{
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            // вывести, что n  не простое, так как делится на i
            return false;
        }
    }
    //вывести что n простое. 
    return true;
}
// TODO: Это пример библиотечной функции.
void fnStaticLib1()
{
}
