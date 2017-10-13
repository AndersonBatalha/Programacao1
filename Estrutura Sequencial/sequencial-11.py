#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
print ("Somar numeros reais e inteiros.")
numero1 = int (raw_input ("Digite um numero inteiro: "))
numero2 = int (raw_input ("Digite um outro numero inteiro: "))
numero3 = float (raw_input ("Digite um numero real: "))
a = (2 * numero1) * (numero2 / 2)
b = (3 * numero1) + (numero3)
c = numero3 ** 3
print ("O produto do dobro do primeiro com metade do segundo: %.f") % a
print ("A soma do triplo do primeiro com o terceiro: %.f") % b
print ("O terceiro elevado ao cubo: %.f") % c
