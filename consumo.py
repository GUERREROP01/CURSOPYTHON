# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:26:17 2021

@author: ADMIN
"""

def Europa(litros):
    distancia= float ((litros * 100)/3.785411784)
    millas= float(distancia / 1.609344)
    return millas
    


def EEUU(rmillas):
    
    distkm=float((rmillas * 1.609344))
    litros= float( distkm * 3.785411784 / 100 )
    return litros


lit=input("Ingrese valor en litros consumidos:")
lit=float(lit)
total=Europa(lit)
print ("Con: ", lit, "Ha rrecorrido:",total, "millas")


millas=input("Ingrese valor en millas reccoridas:")
millas=float(millas)
total=float(EEUU(millas))
print ("Ha rrecorrido:", millas, "Millas", "el consumo es",float(total),"Galones" )
