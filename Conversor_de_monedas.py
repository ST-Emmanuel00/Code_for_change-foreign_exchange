#Menu para escoger pais
menu = """"
¡Bienvenido al conversor de monedas! 🤑
1 - Pesos Colombianos
2 - Pesos Argentinos 
3 - Pesos Mexicanos

Elige una opcion: """
opcion = input(menu)

if opcion == '1':
    pesos = input("¿cuantos pesos colombianos tienes: ")
    pesos = float(pesos)
    valor_dolar = 3972.11
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + " " + dolares + " " + "Dolares")

elif opcion == '2':
    pesos = input("¿cuantos pesos Argentinos tienes: ")
    pesos = float(pesos)
    valor_dolar = 97.01
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + " " + dolares + " " + "Dolares")
elif opcion == '3':
    pesos = input("¿cuantos pesos Mexicanos tienes: ")
    pesos = float(pesos)
    valor_dolar = 20.07
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + " " + dolares + " " + "Dolares")
else:
    print ("Ingresa una opcion correcta")

