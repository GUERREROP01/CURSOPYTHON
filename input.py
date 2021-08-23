# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:34:12 2021

@author: ADMIN
"""

Nombre=  input("Nombre:")
Apellido= input("Apellido:")
Ciudad= input("Ciudad:")
Edad= int(input ("edad:"))
space=" "
print (Nombre,Apellido,Ciudad,Edad)
print (Nombre+space*3+Apellido+space*3+Ciudad+space*3+str(Edad))

if Edad >= 15 and Edad <=17 :
    print ("Edad Adolecente")
elif  Edad >= 18 and Edad <= 60:
    print ("Edad Adulto")
elif  Edad >= 61 :
    print("Adulto mayor")
else:
    print ("Edad Menor a 15")