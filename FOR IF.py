# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:58:23 2021

@author: ADMIN
"""

lista=['R1','R2','R3',"S1","S2"]
lista1=[]
lista2=[]
for j in lista:
    if  'S' in j:
        print (j)
        lista1.append(j)
    else:
        lista2.append(j)
print("ultimo valor de j:",j)
print ("Valores lista1 :",lista1)
print ("Valores lista1 :",lista2)
for i in range(0,10,1):
    print (i, end=" ")