#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 48. Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# a. Exemplo: 12376489 => 98467321
numero = int(raw_input("Número: "))
n = str(numero)
print "\n%d --> %s" % (numero, n[::-1])
