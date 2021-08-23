# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:24:04 2021

@author: ADMIN
"""




valor=int(input("Ingrese valor:"))

res=True
for j in range (2,valor,1):
    resultado = int(valor / j)
    print ("Division:",resultado, "J:",j)
    if resultado == 0 :
        res=False
        break
    

print ("Resultado:", res)

