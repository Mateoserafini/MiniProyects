import random, string

contraseña_numerica = string.digits
contraseña_alfabetica = string.ascii_letters
contraseña_alfanumerica = string.ascii_letters + string.digits
contraseña_sim_num_alf = string.digits + string.punctuation + string.ascii_letters

print('Hola has entrado al Generador de contraseñas.')
try:
    while True:
        print('1- Contraseña de tipo numerica \n2- Contraseña de tipo alfabetica \n3- Contraseña de tipo alfa-numerica\n4- Contraseña con numeros, letras y simbolos\n5- Salir ')
        opcion = int(input('Eliga una opcion: '))
        if (opcion == 1):
            longitud = int(input('Ingrese la cantidad de caracters que desee para si contraseña: '))
            contraseña = ''.join(random.choice(contraseña_numerica) for i in range(longitud))
            print(f'La contraseña es : {contraseña}')
        elif (opcion == 2):
            longitud = int(input('Ingrese la cantidad de caracters que desee para si contraseña: '))
            contraseña = ''.join(random.choice(contraseña_alfabetica) for i in range(longitud))
            print(f'La contraseña es : {contraseña}')
        elif (opcion == 3):
            longitud = int(input('Ingrese la cantidad de caracters que desee para si contraseña: '))
            contraseña = ''.join(random.choice(contraseña_alfanumerica) for i in range(longitud))
            print(f'La contraseña es : {contraseña}')
        elif (opcion == 4):
            longitud = int(input('Ingrese la cantidad de caracters que desee para si contraseña: '))
            contraseña = ''.join(random.choice(contraseña_sim_num_alf) for i in range(longitud))
            print(f'La contraseña es : {contraseña}')
        elif (opcion == 5):
            print('Gracias por probar este programa.')
            
        else:
            print('Ingresaste un numero invalido, ahora ingrese un numero valido del (1 al 5): ')
            continue
except ValueError:

    print('Ingrese una opcion valida (Letras, Nada(Null) o Simbolos)')