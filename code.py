from ast import If
from dis import dis
from hashlib import new
from math import dist, radians
from operator import ne
from re import I, M
from tkinter import N
import pandas as pd
df=pd.read_csv('calcutate.csv')
mass=df['mass'].tolist()
radi=df['radious'].tolist()
grav=df['gravity'].tolist()
dista=df['distance'].tolist()
nm=[]
nr=[]
ng=[]
nd=[]
for i in range(0,len(dista)):
    m=float(mass[i])
    g=float(grav[i])
    r=float(radi[i])
    d=float(dista[i])
    if(d<=100 and g>=150 and g<=350):
        nm.append(m)
        nr.append(r)
        ng.append(g)
        nd.append(d)
newdf=pd.DataFrame({'Distance':nd,'Mass':nm,'Gravity':ng,'Radious':nr})
newdf.to_csv('filtared.csv')