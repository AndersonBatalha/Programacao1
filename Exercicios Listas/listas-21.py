#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 21. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
# a. O modelo do carro mais econômico; b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
# Comparativo de Consumo de Combustível
# Veículo 1   Nome: Fusca     Km por litro: 7
# Veículo 2   Nome: Gol       Km por litro: 10
# Veículo 3   Nome: Uno       Km por litro: 12.5
# Veículo 4   Nome: Vectra    Km por litro: 9
# Veículo 5   Nome: Peugeot 207   Km por litro: 14.5
# Relatório Final
# 1 - Fusca       -  7.0 - 142.9 litros - R$ 321.43
# 2 - Gol         - 10.0 - 100.0 litros - R$ 225.00
# 3 - Uno         - 12.5 -  80.0 litros - R$ 180.00
# 4 - Vectra      -  9.0 - 111.1 litros - R$ 250.00
# 5 - Peugeot 207 - 14.5 -  69.0 litros - R$ 155.17
# O menor consumo é do Peugeot 207.
# 1 l - 7 km -->> x l - 1000 km -> 7x = 1000 -> x = 1000 / 7
carros = []
consumos = []
d = []
p = []
for i in range(1, 4):
	modelo = raw_input("Modelo do carro %d -> " % i)
	consumo = float(raw_input("Consumo do carro %d -> " % i))
	carros.append(modelo)
	consumos.append(consumo)
print "Comparativo de Consumo de Combustível"
for i in range(len(carros)):
	print "Veículo %d\tNome: %s\tKm por litro: %.1f" % (i + 1, carros[i], consumos[i])
print "\nRelatório Final"
for i in range(len(consumos)):
	x = 1000 / consumos[i]
	d.append(x)
	gasolina = d[i] * 2.25
	p.append(gasolina)
	print "%d\t%8s\t%3.1f km/l\t%3.1f litros\tR$ %3.2f" % (i + 1, carros[i], consumos[i], d[i], p[i])
print "\nO %s é o carro mais econômico.\nO %s é o menos econômico." % (carros[d.index(min(d))], carros[d.index(max(d))])
