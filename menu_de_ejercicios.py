try:
    while True:
        print('1- Calculadora \n2- Conversor de grados \n3- ¿Par o Impar? \n4- Factorial de un numero \n5- ¿Es primo? ')
        opcion = int(input('Eliga una opcion: '))
        if (opcion == 1 ):
            from funciones import suma,resta,multiplicacion,division,potencia,raiz
            print('Accediste a la calculadora ingrese un numero segun que operacion quieres realizar.')
            print(' 1- Suma \n2- Resta \n3- Multiplicacion \n4- Divicion \n5- Potencia \n6- Raiz ')
            while True:
                opcion1 = int(input('Eliga una opcion: '))
                if opcion1 == 1:
                    suma()
                    break
                elif opcion1 == 2:
                    resta()
                    break
                elif opcion1 == 3:
                    multiplicacion()
                    break
                elif opcion1 == 4:
                    division()
                    break
                elif opcion1 == 5:
                    potencia()
                    break
                elif opcion1 == 6:
                    raiz()
                    break
                else:
                    print('Ingrese un numero valido para realizar una operacion.')
                    continue  # Continua con la siguiente iteración del bucle
        elif(opcion==2):
            from funciones import Farenheit_a_Celcios as Fac,Celcios_a_Farenheit as Caf
            print('accediste al conversor de grados elija lo que necesite.')
            print('1-Farenheit a celcios \n2- Celcios a farenheit ')
            while True:
                opcion2 = int(input('Eliga una opcion: '))
                if opcion2 == 1:
                    Fac()
                    break
                elif opcion2 == 2:
                    Caf()
                    break
                else:
                    print('Ingrese un numero valido para realizar una operacion.')
                break  # Sale del bucle después de completar una operación
        elif(opcion==3):
            from funciones import Par_o_Impar as PoI
            PoI()
            break
        elif(opcion==4):
            from funciones import Factorial
            Factorial()
            break
        elif(opcion==5):
            from funciones import Es_Primo
            Es_Primo()
            break
    
        else: 
            print("Ingresaste una opcion invalida, ingrese un numero del 1 al 6")
            continue
except ValueError:
    print('Ingrese una opcion valida (Letras, Nada(Null) o Simbolos)')  # Manejo de excepciones para opciones inválidas. 
               