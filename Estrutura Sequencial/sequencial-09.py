#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 9. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. 
# Fórmula ----> C = (5 * (F-32) / 9).
print ("Converte fahrenheit para celsius")
fahrenheit = float (raw_input ("Temperatura em graus fahrenheit: "))
celsius = (5 * (fahrenheit - 32) / 1.8)
print ("O valor em graus fahrenheit e: %.2f") % fahrenheit
print ("O valor em graus celsius e: %.2f") % celsius
