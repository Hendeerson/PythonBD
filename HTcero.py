
#Titulo
print("------------Calculo de IMC----------------")
#Datos a obtener
peso = float(input("¿Cual es su peso en Kg?"))
Estatura = float(input("¿Cual es su estatura en metros?"))
#Uso de los datos obtenidos para el IMC
Indice = round(peso/(Estatura*Estatura),2)


print("Su masa corporal es:  " + str(Indice))
print("-----------Final de Calculo--------------")
