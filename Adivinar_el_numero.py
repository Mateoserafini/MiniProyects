import random 

try:
    print('Has entrado a el juego: Adivinar el numero')
    while True:
        print('1- Jugar \n2- Instrucciones del Juego \n3- Salir')
        opcion = int(input('Eliga una opcion: '))
        if opcion == 1:
            print('Empesaste a jugar. ')
            cifras = int(input('Ingrese la cantidad de cifras que quiera adivinar (4 es un punto intermedio/dificil): '))
            numero_a_adivinar = "".join(random.sample("0123456789", cifras)) # genera un número aleatorio de la cantidad de cifras ingresadas sin repetir ningún dígito
            print('Ya he pensado un número de {} cifras. Adivina cuál es.'.format(cifras))
            intentos = 0
            while True:
                intentos += 1
                numero_usuario = input('Intento {}: '.format(intentos))
                if numero_usuario.isdigit() and len(numero_usuario) == cifras: # valida que la entrada sea un número de la cantidad de cifras esperada
                    aciertos = 0
                    for i in range(cifras):
                        if numero_usuario[i] == numero_a_adivinar[i]:
                            aciertos += 1
                    if aciertos == cifras:
                        print('¡Felicidades! Adivinaste el número en {} intentos.'.format(intentos))
                        break
                    else:
                        print('Tienes {} aciertos.'.format(aciertos))
                else:
                    print('Por favor, ingrese un número de {} cifras.'.format(cifras))
        elif opcion == 2:
            print('Instrucciones del Juego: ')
            print('El objetivo del juego es adivinar un número aleatorio generado por la computadora.')
            print('El número a adivinar tiene una cantidad de cifras que el jugador puede seleccionar al comenzar el juego.')
            print('Cada vez que el jugador ingresa un número, el programa le indica cuántos aciertos tiene con respecto al número a adivinar.')
        elif opcion == 3:
            print('Gracias por jugar. Hasta la próxima.')
            break
        else:
            print('Por favor, ingrese una opción válida.')
except Exception as e:
    print('Ha ocurrido un error: {}'.format(str(e)))
