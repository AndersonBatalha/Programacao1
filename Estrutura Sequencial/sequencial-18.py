#!/usr/bin/env python
# coding: utf-8
# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
print ("Velocidade de um Download.")
tamanho_arquivo = float (raw_input ("Tamanho do arquivo (MB): "))
velocidade_internet = float (raw_input ("Velocidade da internet (Mbps): "))
tempo_download = tamanho_arquivo / velocidade_internet
print "Tempo aproximado: %.0f min" % tempo_download
