
import csv
file = open("ArchivoNaive.csv")
csvreader = csv.reader(file)
header = next(csvreader)

#Variables
trabajos=[]
categorias=[]
Finanza=[]
Tecnologia=[]
Venta=[]
palabras=[]
ocurrencias=[]
pxckFin=[]
pxckTec=[]
pxckVentas=[]
tempL=[]
modeloProbalisticoFina=[]
modeloProbalisticoTec=[]
modeloProbalisticoVenta=[]
totalTecno=0
totalFin=0
totalVenta=0
totalTrabajos=0
probabilidadFin=1
probabilidadTec=1
probabilidadVenta=1
px=0
pTecX=0
pVenX=0
pFinX=0
trabajoN='gerente analista de datos'.upper()

#Hacemos uso de for each para la deteccion de palabras dentro de cada lista#
for row in csvreader:
  trabajos.append(row[0].upper())  
  categorias.append(row[1].upper())
  if row[1]=="Tecnologia":
      Tecnologia.append(row[0].upper())
  elif row[1]=="Finanza":  
      Finanza.append(row[0].upper())
  elif row[1]=="Ventas":  
      Venta.append(row[0].upper())
    
file.close()

#Cargamos los valores totales del tamaño de cada lista generada
totalTecno=len(Tecnologia)
totalFin=len(Finanza)
totalVenta=len(Venta)
totalTrabajos=len(trabajos)

#Obtenemos el p(Ck)/porcentaje y lo almacenamos en valores pck
pckTec=totalTecno/totalTrabajos
pckFin=totalFin/totalTrabajos
pckVenta=totalVenta/totalTrabajos
print("probablidad de aparecer: ")
print(pckTec)
print(pckFin)
print(pckVenta)

#Se realiza un variable encargada de almacenar y alistar las palabras obtenidas.
palabras=' '.join(trabajos)
palabras=palabras.split(' ')
palabras=set(palabras)
palabras=list(palabras)

#Las palabras obtenidas son alistadas dentro de su respectiva lista
for palabra in palabras:
  pxckFin.append(0)
  pxckTec.append(0)
  pxckVentas.append(0)


# Nos encargamos de generar el modelo de finanza obteniendo las 
# palabras utilizadas dentro de las listas, obtenemos el valor y
# realizamos, finalmente haciendo comparacion y obteniendo su 
# modelo probabilistico final.
print("Modelo finanza:","\n")
for trabajo in Finanza:
  for palabra in palabras:
    if palabra in trabajo.split(' '):
      tempL.append(1)
    else:
      tempL.append(0)
  modeloProbalisticoFina.append(tempL.copy())
  tempL.clear()

print(modeloProbalisticoFina)  

# Nos encargamos de generar el modelo de tecnologia obteniendo las 
# palabras utilizadas dentro de las listas, obtenemos el valor y
# realizamos, finalmente haciendo comparacion y obteniendo su 
# modelo probabilistico final.
print("Modelo tecnologia:","\n")
for trabajo in Tecnologia:
  for palabra in palabras:
    if palabra in trabajo.split(' '):
      tempL.append(1)
    else:
      tempL.append(0)
  modeloProbalisticoTec.append(tempL.copy())
  tempL.clear()

print(modeloProbalisticoTec) 

# Nos encargamos de generar el modelo de venta obteniendo las 
# palabras utilizadas dentro de las listas, obtenemos el valor y
# realizamos, finalmente haciendo comparacion y obteniendo su 
# modelo probabilistico final.
print("Modelo venta:","\n")
for trabajo in Venta:
  for palabra in palabras:
    if palabra in trabajo.split(' '):
      tempL.append(1)
    else:
      tempL.append(0)
  modeloProbalisticoVenta.append(tempL.copy())
  tempL.clear()

print(modeloProbalisticoVenta)

#Realizamos un split para obtener la lista de los trabajos aun no asignados
trabajoN=trabajoN.split(' ')

# Hacemos uso de ciclos for para la asigancion de valores y renumeramos las 
# las palabras dentro de aquellos sin asignacion para realizar su posicionamiento
# y otorgarle su calculo.
for finanza in modeloProbalisticoFina:
  for i,palabra in enumerate(palabras):     
    if finanza[i]==1:
      pxckFin[i]=pxckFin[i]+1
print("Calcular p(xi|ck) Finanzas: ", "\n")
print(pxckFin)

for i,palabra in enumerate(palabras):     
  if palabra in trabajoN:
    pxckFin[i]=pxckFin[i]/totalFin
  else:
    pxckFin[i]=(totalFin-pxckFin[i])/totalFin

print(pxckFin)

for pxckfin in pxckFin:
  probabilidadFin=probabilidadFin*pxckfin
  
print(probabilidadFin)


# Hacemos uso de ciclos for para la asigancion de valores y renumeramos las 
# las palabras dentro de aquellos sin asignacion para realizar su posicionamiento
# y otorgarle su calculo.
for tecnologia in modeloProbalisticoTec:
  for i,palabra in enumerate(palabras):     
    if tecnologia[i]==1:
      pxckTec[i]=pxckTec[i]+1
print("Calcular p(xi|ck) Tecnologia: ", "\n")
print(pxckTec)

for i,palabra in enumerate(palabras):     
  if palabra in trabajoN:
    pxckTec[i]=pxckTec[i]/totalTecno
  else:
    pxckTec[i]=(totalTecno-pxckTec[i])/totalTecno


print(pxckTec)

for pxcktec in pxckTec:
  probabilidadTec=probabilidadTec*pxcktec

print(probabilidadTec)

# Hacemos uso de ciclos for para la asigancion de valores y renumeramos las 
# las palabras dentro de aquellos sin asignacion para realizar su posicionamiento
# y otorgarle su calculo.
for ventas in modeloProbalisticoVenta:
  for i,palabra in enumerate(palabras):     
    if ventas[i]==1:
      pxckVentas[i]=pxckVentas[i]+1
print("Calcular p(xi|ck) Ventas: ", "\n")
print(pxckVentas)

for i,palabra in enumerate(palabras):     
  if palabra in trabajoN:
    pxckVentas[i]=pxckVentas[i]/totalVenta
  else:
    pxckVentas[i]=(totalVenta-pxckVentas[i])/totalVenta


print(pxckVentas)

# Dentro de un ciclo for each realizamos calculos sobre las probabilidades
# y lo almacena dentro de la variable de probabilidadVenta otorgando asi un nuevo
# valor dado al ser multiplicado por el pxck de las ventas.
for pxckventas in pxckVentas:
  probabilidadVenta=probabilidadVenta*pxckventas


print(probabilidadVenta)

px=(pckTec*probabilidadTec)+(pckVenta*probabilidadVenta)+(pckFin*probabilidadFin)

print("calcular p(xi): ")
print(px)

# Calculamos la probabilidad dada para cada una de las categorias
print("calcular p(ck|xi) de tecnologia: ")
pTecX=(pckTec)*(probabilidadTec)/px
print(pTecX)

print("calcular p(ck|xi) de ventas: ")
pVenX=(pckVenta)*(probabilidadVenta)/px
print(pVenX)

print("calcular p(ck|xi) de Finanzas: ")
pFinX=(pckFin)*(probabilidadFin)/px
print(pFinX)



