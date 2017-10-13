#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print ("Media anual dos alunos.")
bim1 = float (raw_input ("Nota do primeiro bimestre: "))
bim2 = float (raw_input ("Nota do segundo bimestre: "))
bim3 = float (raw_input ("Nota do terceiro bimestre: "))
bim4 = float (raw_input ("Nota do quarto bimestre: "))
media = (bim1 + bim2 + bim3 + bim4) / 4
print ("A media final do aluno e: %.2f") % media

if media >= 7:
    print ("Parabens!! O aluno foi aprovado.")
else:
    print ("Que pena! O aluno foi reprovado.")
