#! /usr/bin/python3

cadena = '''ie ke tk

*

   

ACADEMIA DE SEGURIDAD

COLOMBOLATINA

CERTIFICA 
ROBINSON JULIAN TORO CAMACHO
C.C 1.112.618.160

ASISTIO Y APROBO EL CURSO DE
REENTRENAMIENTO VIGILANCIA.

  

VENSIDADHORAPIAGE 39 Lonas, SECCN RESOLUCION
No 4973 DE JULIO DE 2011

%e Eb ob ob ob ob ob ot bo

DE UA SUPERINTENDENCIA DE VIGILANCIA Y SECUR.DAD PRIVADA,
Realizaco=N BOGOTA. 24 DE JULIO DE 2020, SMeepineiEN 1 OeaTA
A os

Mee

SERINE CAL)
NRO ECSP1223-G652086'''

startWord = cadena.index('CERTIFICA') #Ingresamos el texto inicial de la búsqueda
endWord = cadena.index('VIGILANCIA') #Ingresamos el texto final de la búsqueda

subcadena = cadena[startWord:endWord]


newString = subcadena.lstrip("CERTIFICA QUE").lstrip("CERTIFICA").replace('\n', ' ').replace('.', '').strip().rstrip().replace(' ', '_')


print(newString)