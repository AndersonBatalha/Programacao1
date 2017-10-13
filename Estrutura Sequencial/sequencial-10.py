#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
print ("Converte celsius para fahrenheit.")
celsius = float (raw_input ("Temperatura em graus celsius: "))
fahrenheit = (celsius * 1.8) + 32
print ("O valor em graus celsius e: %.f C.") % celsius
print ("O valor em graus fahrenheit e: %.2f F.") % fahrenheit
