# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 15:01:47 2023

@author: YASEMİN
"""

import random
Liste=["Ankara","İzmir","Mersin","Adana","Eskişehir"]
kelime=random.choice(Liste)
adam=['''
    
      +--------+
      O        |
    / | \      |
      |        |
    /  \       |
           -----  ''' , 
'''
      +--------+
      O        |
    / | \      |
      |        |
    /          |
           -----  ''' ,           
'''
      +--------+
      O        |
    / | \      |
      |        |
               |
           -----  ''' , 
'''
      +--------+
      O        |
    / | \      |
               |
               |
           -----  ''' , 
'''
      +--------+
      O        |
    / |        |
               |
               |
           -----  ''' , 
'''
      +--------+
      O        |
      |        |
               |
               |
           -----  ''' , 
'''
      +--------+
      O        |
               |
               |
               |
           -----  ''' , 
'''
      +--------+
               |
               |
               |
               |
           -----  '''  ]
           
DoğruHarf=[]
YanlışHarf=[]
Hak=len(adam)

while Hak>0:
    out=""
    for h in kelime:
        if h in DoğruHarf:
            out+=h
        else:
            out+="_"
    if out == kelime:
         break
    print ("kelime:",out)
    print ( adam[Hak-1])
    HarfGir=input()
    if HarfGir in kelime:
        print("Doğru Harf")
        DoğruHarf.append(HarfGir)
    if HarfGir not in kelime:
        print("Yanlış Harf")
        YanlışHarf.append(HarfGir)
        Hak-=1
    elif HarfGir in DoğruHarf or HarfGir in YanlışHarf:
        print("Harf girildi")
if Hak !=0:
    print ("Kazandın..Kelime: ",kelime)
else:
    print ("Kaybettin..Kelime: ",kelime)
    
    
    
    
    
    
     