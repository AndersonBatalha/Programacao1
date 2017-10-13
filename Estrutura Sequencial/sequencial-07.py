#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print ("Area do quadrado")
import math
area = float (raw_input ("Digite o valor da area do quadrado: "))
dobro_area = area * area
print ("O valor da area do quadrado e: %.2f") % dobro_area
