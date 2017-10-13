#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
print ("Peso ideal de uma pessoa.")
altura = float (raw_input ("Altura: "))
peso_ideal = (72.7 * altura) - 58
print ("Peso ideal: %.2f") % peso_ideal
