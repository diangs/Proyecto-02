"""
Proyecto 2: Introducción al análisis de datos
"""
from os import system
import csv
import operator

# =============================================================================
# Creación del código principal menú
# Se definen las opciones validas y se espera una selección
# =============================================================================
option = 0
while option != "4":
  print("***  Sistema de control principal  ***\n\n" )
  print("[1] Rutas de importación y exportación \n")
  print("[2] Medio de transporte utilizado \n")
  print("[3] Valor total de importaciones y exportaciones \n")
  print("[4] Salir \n")
  option = input("Ingrese la opción: ")
  system("cls")
  
  #Se comprueba la selección del usuario
  try:
      if int(option) in range(1,5):
          
# =============================================================================
# Opción 1: Rutas de importación y exportación            
# =============================================================================
          if int(option) == 1:
              system("cls")
              #La variale global_value servira como diccionario que almacenara como indice la ruta-medio y apuntara a la cantidad de veces que se uso esa ruta 
              global_value = {}
              sumador = 0
              sumador2 = 0
              total = 0
              total2 = 0
              with open("synergy_logistics_database.csv", "r") as data:
                  reader = csv.DictReader(data)
                  #Se recorre el archivo buscando las rutas de transporte y contando las veces que se usaron, se agrega el valor de sus importaciones y sumador guarda el valor total
                  for line in reader:
                      if line["origin"]+" - "+line["destination"]+" - "+line["transport_mode"] not in global_value:
                          global_value[line["origin"]+" - "+line["destination"]+" - "+line["transport_mode"]] = [1, int(line["total_value"])]
                      else:
                          global_value[line["origin"]+" - "+line["destination"]+" - "+line["transport_mode"]][0] += 1
                          global_value[line["origin"]+" - "+line["destination"]+" - "+line["transport_mode"]][1] += int(line["total_value"])
                      sumador += int(line["total_value"])
                      sumador2 += 1
                  #Se acomodan los valores de mayor a menor tomando en cuenta las veces que se uso la ruta
                  countrys = sorted(global_value.items(), key=operator.itemgetter(1), reverse=True)
                  suma = 0
                  #Se imprimen los valores hasta que se obtengan a los 10 primeros sumando sus valores
                  print("Principales 10 rutas de transporte: (ruta, uso, valor obtenido)\n")
                  for country in countrys:
                      if suma < 10:
                          print(country[0]+" || "+str(round((country[1][0]/sumador2)*100,4))+"%"+" || "+str(round((country[1][1]/sumador)*100,4))+"%")
                          total += round((country[1][1]/sumador)*100,4)
                          total2 += round((country[1][0]/sumador2)*100,4)
                      else:
                          break
                      suma +=1
                  print("\nValor total: "+str(round(total,4))+"%")
                  print("\nUso total: "+str(round(total2,4))+"%")
                  input("\nContinuar... ")
                  system("cls")
                  
# =============================================================================
# Opción 2: Medio de transporte utilizado
# =============================================================================
          if int(option) == 2:
              system("cls")
              #La variale global_value servira como diccionario que almacenara el valor total de los medios de transporte, suma contendrá el valor total de todos
              global_value = {}
              suma = 0
              with open("synergy_logistics_database.csv", "r") as data:
                  reader = csv.DictReader(data)
                  #Se recorre el archivo buscando los medios de transporte contenidos mientras suma sus valores, suma incrementa con todos ya que es el valor total
                  for line in reader:
                      if line["transport_mode"] not in global_value:
                          global_value[line["transport_mode"]] = int(line["total_value"])
                      else:
                          global_value[line["transport_mode"]] += int(line["total_value"])
                      suma += int(line["total_value"])
              #Se genera el porcentaje de los valores
              for country in global_value:
                  global_value[country] = round((global_value[country]/suma)*100,4)
              #Se acomodan los valores de mayor a menor
              countrys = sorted(global_value.items(), key=operator.itemgetter(1), reverse=True)
              suma = 0
              #Se imprimen los valores hasta que se obtengan a los tres primeros
              print("Principales tres medios de transporte: \n")
              for country in countrys:
                  if suma < 3:
                      print(country[0]+" \t\t"+str(country[1])+"%")
                  else:
                      break
                  suma +=1
              input("\nContinuar... ")
              system("cls")
              
# =============================================================================
# Opción 3: Valor total de importaciones y exportaciones               
# =============================================================================
          if int(option) == 3:
              system("cls")
              #La variale global_value servira como diccionario que almacenara el valor total por pais, suma contendrá el valor total de todos
              global_value = {}
              suma = 0
              with open("synergy_logistics_database.csv", "r") as data:
                  reader = csv.DictReader(data)
                  #Se recorre el archivo buscando los paises contenidos mientras suma sus valores, suma incrementa con todos ya que es el valor total
                  for line in reader:
                      if line["origin"] not in global_value:
                          global_value[line["origin"]] = int(line["total_value"])
                      else:
                          global_value[line["origin"]] += int(line["total_value"])
                      suma += int(line["total_value"])
              #Se genera el porcentaje de los valores
              for country in global_value:
                  global_value[country] = round((global_value[country]/suma)*100,4)
              #Se acomodan los valores de mayor a menor
              countrys = sorted(global_value.items(), key=operator.itemgetter(1), reverse=True)
              suma = 0
              #Se imprimen los valores hasta que se obtengan los paises que conforman el 80% del valor total
              print("Paises generadores del 80% del valor de las exportaciones e importaciones: \n")
              for country in countrys:
                  if suma < 80:
                      print(country[0]+" "+str(country[1])+"%")
                      suma += country[1]
                  else:
                      break
              input("\nContinuar... ")
              system("cls")
      else:
          print("Ingrese una opción valida")
          input("Confirmar...")
  except ValueError:
      print("Ingrese una opción valida")
      input("Confirmar...")