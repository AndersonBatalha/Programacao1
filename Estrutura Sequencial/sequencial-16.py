#!/usr/bin/env python
# coding: utf-8
# 16. Fa�a um programa para uma loja de tintas. O programa dever� pedir o tamanho em metros quadrados da �rea a ser pintada. Considere que a cobertura da tinta � de 1 litro para cada 3 metros quadrados e que a tinta � vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usu�rio a quantidades de latas de tinta a serem compradas e o pre�o total.
# 1 l cobre 3 m2
# 18 l cobrem x m2
# x = 54 m2 por lata de tinta.
print ("Programa para uma loja de tintas.")
area = float (raw_input ("Area (m2): "))
quantidade_latas = area / 54
preco_total = quantidade_latas * 80
print ("Latas de tinta: %.0f") % quantidade_latas
print ("Preco total: R$ %.0f") % preco_total
