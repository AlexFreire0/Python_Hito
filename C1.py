#creamos una función para cada vez que accedemos al menú principal con las victorias
def pantalla_inicial():
    print("1 - Cuadrado")
    print("2 - Rectangulo")
    print("3 - Salir")
    while True:
        numero = int(input("Dime una opción: "))
        match numero:
            case 1:
                cuadrado()
                break
            case 2:
                rectangulo()
                break
            case 3:
                break
            case _:
                print("Opcion incorrecta")
#Creamos una función para si se elige la opción cuadrado
def cuadrado():
    lado = int(input("Dime el lado del cuadrado: "))
    for i in range(lado):
        print("*  " * lado)
    area = lado * lado
    perimetro = lado * 4
    print("Su área es", area)
    print("Su perímetro es", perimetro)
    pantalla_inicial()
#Creamos una función para si se elige la opción rectángulo
def  rectangulo():
    base = int(input("Dime la base del rectangulo: "))
    altura = int(input("Dime la altura del rectángulo: "))
    for i in range(altura):
        print("*  " * base)
    area = base * altura
    perimetro = (base * 2) + (altura * 2)
    print("Su área es", area)
    print("Su perímetro es", perimetro)
    pantalla_inicial()
#Llamamos a la pantalla inicial
pantalla_inicial()

    