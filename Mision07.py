#Cecilia Daniela Olivares Hernández
#Este programa despliega un menu en el cual el usuario puede utilizar cualquiera de las funciones de manera repetide hasta que de la opción salir

def dividir(dividendo, divisor):
    dividendoOriginal = dividendo #Guardo el valor original del dividendo en una nueva variable
    cociente = 0 #El contador comeinza en 0
    while dividendo >= divisor: #Parametro
        dividendo = dividendo - divisor #Se va a ir restando el dividendo para obtener el residuo
        cociente += 1 #Va sumando el número de restas
    print(dividendoOriginal, "/", divisor, "=", cociente, "sobra", dividendo)

def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor.")
    respuesta = 0
    numMayor = 0
    while respuesta != -1:
        respuesta = int(input("Teclea un número [-1 para salir]: "))
        if respuesta >= numMayor:
             numMayor =  respuesta
    print("El mayor es:",numMayor)


def main():
    respuesta = int(input("""Misión 07. Ciclos While
    Autor: Cecilia Daniela Olivares Hernández
    Matrícula: A01745727
    1. Calcular divisiones
    2. Encontrar el mayor
    3. Salir
    Teclea tu opción: """))
    while respuesta != 3:
        if respuesta == 1:
            dividendo = int(input("Ingresa el dividendo:" ))
            divisor = int(input("Ingresa el divisor:" ))
            dividir(dividendo, divisor)

        elif respuesta == 2:
            encontrarMayor()

        elif respuesta>=4 or 0>=respuesta:
            print("ERROR, teclea 1, 2 o 3")
        respuesta = int(input("""Misión 07. Ciclos While
        Autor: Cecilia Daniela Olivares Hernández
        Matrícula: A01745727
        1. Calcular divisiones
        2. Encontrar el mayor
        3. Salir
        Teclea tu opción: """))
    if respuesta == 3:
        print("Gracias por usar este programa, regresa pronto")


main()