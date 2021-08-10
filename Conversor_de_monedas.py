#Funcion para convertir monedas
def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos" + " " + tipo_pesos + " " + "tienes: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + " " + dolares + " " + "Dolares")

#Menu para escoger pais
menu = """"
¡Bienvenido al conversor de monedas! 🤑
1 - Pesos Colombianos
2 - Pesos Argentinos 
3 - Pesos Mexicanos
Elige una opcion: """
opcion = input(menu)
if opcion == '1':
    conversor("Colombiano",3996.75)
elif opcion == '2':
    conversor("Argentino",97.04 )
elif opcion == '3':
    conversor("Mexicano",20.16 )
else:
    print ("Ingresa una opcion correcta")