'''
El programa pedirá:
• un operador (+.- o *) o la palabra “Fin” que hará terminar el programa (validando
que se introduce uno de esos valores)
• cuantos números se quiere introducir
• solicitará dichos números (validando que sean números)
• Finalmente devolverá el resultado
Los resultados hasta la introducción de la palabra “Fin” serán independiente'''

programa_acabado = False

while not programa_acabado:
   
    # pedir el operador o la palabra "Fin".
    operador = input("Ingrese el operador (+, -, *, o 'Fin' para terminar): ")

    # Ver si se termina el programa.
    if operador.lower() == 'fin':
        print("Fin del programa.")
        programa_acabado = True
    else:
        # Si el operador esta entre mi eleccion entonces sehuir para delante
        if operador in ['+', '-', '*']:
            # Cantidad de números
            cantidad_numeros = input("Ingrese la cantidad de números: ")

            # Validar que la cantidad de números sea un entero positivo.
            if cantidad_numeros.isdigit() and int(cantidad_numeros) > 0:
                cantidad_numeros = int(cantidad_numeros)

                # Inicializar el resultado.
                resultado = 0

                i = 1
                error = False

                while i <= cantidad_numeros and not error:
                    # Solicitar al usuario el número.
                    numero = input(f"Ingrese el número {i}: ")

                    # Validar que el número ingresado sea un número válido.
                    if '.' in numero and numero.replace('.', '', 1).isdigit():
                        numero = float(numero)
                    elif numero.isdigit():
                        numero = int(numero)
                    else:
                        print("Error: Ingrese un número válido.")
                        error = True

                    # Realizar la operación si no hay error, este es una construccion que la uso para evakluar si la experion es falsa
                    if not error:
                        # Realizar la operación.
                        if operador == '+':
                            resultado += numero
                        elif operador == '-':
                            resultado = resultado - numero if i > 1 else numero
                        elif operador == '*':
                            resultado = resultado * numero if i > 1 else numero

                        i += 1

                if not error:
                    print("Resultado:", resultado)
            else:
                print("Error: Ingrese un número entero positivo válido.")
        else:
            print("Error: Ingrese un operador válido (+, -, *).")




