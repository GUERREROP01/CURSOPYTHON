# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:27:40 2021

@author: ADMIN
"""

acl=int(input("Valor ACL:"))
if acl >= 1 and acl <=99 :
    print ("ACL ESTANDAR")
elif  acl >= 100 and acl <=199:
    print ("ACL EEXTENDIDA")
else:
    print("NO ES ACL")