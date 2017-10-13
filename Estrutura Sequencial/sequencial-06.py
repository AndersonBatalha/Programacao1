#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
print ("Area do circulo")
import math
raio = float (raw_input ("Digite o valor do raio do circulo: "))
area = math.pi * raio * 2
print ("O valor da area do circulo e: %.2f") % area
