import random
import string

def generar_contrasena(num_letras, num_numeros, num_simbolos, excluir_ambiguos = False):
    """
    Genera una contraseña aleatoria basada en la configuración especificada.

    Parámetros:
    - num_letras (int): Número de letras en la contraseña.
    - num_numeros (int): Número de números en la contraseña.
    - num_simbolos (int): Número de símbolos en la contraseña.
    - excluir_ambiguos (bool): Si es True, excluye caracteres ambiguos como '0', 'O', 'l', 'I'.

    Retorna:
    - str: La contraseña generada.
    
    Excepciones:
    - ValueError: Si la suma de num_letras, num_numeros y num_simbolos es menor a 4.
    """
    if excluir_ambiguos:
        # Excluir caracteres ambiguos como '0', 'O', 'l', 'I'
        letras = string.ascii_letters.replace('l', '').replace('I', '').replace('O', '').replace('o', '')
        numeros = string.digits.replace('0', '')
    else:
        letras = string.ascii_letters
        numeros = string.digits

    simbolos = string.punctuation

    # Verificar que la longitud total sea al menos 4
    if num_letras + num_numeros + num_simbolos < 4:
        raise ValueError("La contraseña debe tener al menos 4 caracteres en total.")

    # Generar las partes de la contraseña
    parte_letras = ''.join(random.choices(letras, k=num_letras))
    parte_numeros = ''.join(random.choices(numeros, k=num_numeros))
    parte_simbolos = ''.join(random.choices(simbolos, k=num_simbolos))

    # Combinar y mezclar los caracteres
    contrasena = parte_letras + parte_numeros + parte_simbolos
    contrasena = ''.join(random.sample(contrasena, len(contrasena)))  # Mezclar caracteres

    return contrasena

def evaluar_fortaleza(contrasena):
    """
    Evalúa la fortaleza de una contraseña en función de su longitud y diversidad de caracteres.

    Parámetros:
    - contrasena (str): La contraseña que se desea evaluar.

    Retorna:
    - str: Un mensaje que describe la fortaleza de la contraseña ('Muy fuerte', 'Fuerte', 'Moderada', 'Débil').
    """
    longitud = len(contrasena)
    tiene_mayus = any(c.isupper() for c in contrasena)
    tiene_minus = any(c.islower() for c in contrasena)
    tiene_numeros = any(c.isdigit() for c in contrasena)
    tiene_simbolos = any(c in string.punctuation for c in contrasena)

    # Calcular un puntaje basado en la longitud y diversidad de caracteres
    puntaje = longitud
    if tiene_mayus: puntaje += 2
    if tiene_minus: puntaje += 2
    if tiene_numeros: puntaje += 2
    if tiene_simbolos: puntaje += 2

    # Evaluar la fortaleza de la contraseña según el puntaje
    if puntaje >= 16:
        return "Muy fuerte"
    elif puntaje >= 12:
        return "Fuerte"
    elif puntaje >= 8:
        return "Moderada"
    else:
        return "Débil"

def main():
    """
    Función principal para interactuar con el usuario y generar la contraseña.
    
    Este método guía al usuario a través del proceso de especificación de la contraseña,
    genera la contraseña, evalúa su fortaleza, y ofrece la opción de guardar la contraseña
    generada en un archivo.
    """
    print("¡Bienvenido al generador de contraseñas mejorado!")
    try:
        # Solicitar al usuario el número de letras, números y símbolos
        num_letras = int(input("¿Cuántas letras deseas en tu contraseña? "))
        num_numeros = int(input("¿Cuántos números deseas en tu contraseña? "))
        num_simbolos = int(input("¿Cuántos símbolos deseas en tu contraseña? "))
        
        # Preguntar si se deben excluir caracteres ambiguos
        excluir_ambiguos = input("¿Quieres excluir caracteres ambiguos como '0', 'O', 'l', 'I'? (s/n): ").lower() == 's'

        # Generar la contraseña con la configuración especificada
        contrasena = generar_contrasena(num_letras, num_numeros, num_simbolos, excluir_ambiguos)

        # Evaluar la fortaleza de la contraseña
        fortaleza = evaluar_fortaleza(contrasena)

        # Mostrar la contraseña generada y su fortaleza
        print("\nTu contraseña generada es: %s" % contrasena)
        print("Nivel de fortaleza: %s" % fortaleza)

        # Ofrecer la opción de guardar la contraseña
        guardar = input("¿Quieres guardar esta contraseña en un archivo? (s/n): ").lower()
        if guardar == 's':
            # Guardar la contraseña y la fortaleza en un archivo
            with open("contrasena_generada.txt", "w") as archivo:
                archivo.write("Contraseña: %s\n" % contrasena)
                archivo.write("Fortaleza: %s\n" % fortaleza)
            print("¡Contraseña guardada en 'contrasena_generada.txt'!")

    except ValueError as e:
        # Manejo de errores en caso de que se introduzcan valores incorrectos
        print("Error: %s" % e)

# Ejecutar la función principal
if __name__ == "__main__":
    main()
