#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print ("Salario do trabalhador")
salario_hora = float (raw_input ("Quanto voce ganha por hora: R$ "))
horas_trabalhadas = float (raw_input ("Horas trabalhadas no mes: R$ "))
salario_mes = salario_hora * horas_trabalhadas
print ("O valor da area do quadrado e: %.2f") % salario_mes
