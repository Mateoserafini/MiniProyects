import tkinter, sqlite3

def Farenheit_a_Celcios():
    farenheit = float(input('ingrese la temperatura en grados farenheit : '))
    celcios =  (farenheit-32) * (5/9)
    print(f'La temperatura es de :{round(celcios,2)} grados celcios')
    
def Celcios_a_Farenheit():
    celcios = float(input('ingrese la temperatura en grados celcios : '))
    farenheit =  celcios * 1.8 + 32
    print(f'La temperatura es de :{round(farenheit,2)} grados farenheit')

def suma():
    num_1 = float(input('ingrese el primer numero: '))
    num_2 = float(input('ingrese el numero que desee sumar: '))
    print(f'La resultado de la suma es de: {num_1 + num_2}')

def resta():
    num_1 = float(input('ingrese el primer numero: '))
    num_2 = float(input('ingrese el numero que desee restar: '))
    print(f'La resultado de la resta es de: {num_1 - num_2}')
    
def multiplicacion():
    num_1 = float(input('ingrese el primer numero: '))
    num_2 = float(input('ingrese el numero por el que desee multiplicarlo: '))
    print(f'La resultado de la resta es de: {num_1 * num_2}')

def multiplicacion():
    num_1 = float(input('ingrese el primer numero: '))
    num_2 = float(input('ingrese el numero por el que desee multiplicarlo: '))
    print(f'La resultado de la multiplicacion es de: {num_1 * num_2}')

def division():
    num_1 = float(input('ingrese el primer numero: '))
    num_2 = float(input('ingrese el numero por el que desee dividirlo: '))
    print(f'La resultado de la division es de: {num_1 // num_2}')

def potencia():
    num_1 = float(input('ingrese el primer numero: '))
    num_2 = float(input('ingrese el exponente por el que desea elevarlo: '))
    print(f'La resultado de la potencia es de: {num_1 ** num_2}')
    
def raiz():
    num_1 = float(input('Ingrese el radical: '))
    num_2 = float(input('Ingrese el índice: '))
    resultado = num_1 ** (1/num_2)
    print(f'El resultado de la raíz es: {round(resultado, 2)}')

def Par_o_Impar():
    num_1 = int(input('Ingrese un numero y le dire si es par o impar: '))
    if num_1 == 0:
        print('El numero ingresado es 0, y este no se concidera par o impar')
    elif num_1 % 2 == 0:
        print("El numero es par.")
    else:
        print("El numero es impar.")

def Factorial():
    num = int(input('Ingrese un numero: '))
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i
    print(f"El factorial de {num} es: {factorial}")
        
def Es_Primo():
    num = int(input('Ingrese un numero: '))
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print('El numero es primo')
    else:
        print('El numero no es primo')
