
def balanceador_expresion(expresion):
    contenedor = []  # contenedorr de aperturas
    aper_cerra = {'(': ')', '[': ']', '{': '}'}  #aperturas a cierres
    secuencia = []  # Lista de secuencia de los signos

    for i, char in enumerate(expresion):
        # Símbolos de apertura
        if char in aper_cerra:
            contenedor.append(char)
            secuencia.append(f"Paso {i+1}: '{char}' -> push → pila: {contenedor}")

        # Símbolos de cierre
        elif char in aper_cerra.values():
            if not contenedor:
                secuencia.append(f"Paso {i+1}: '{char}' -> error: pila vacía")
                return False, secuencia
            tope = contenedor.pop()
            if aper_cerra[tope] != char:
                secuencia.append(f"Paso {i+1}: '{char}' -> error: '{tope}' no se cierra con '{char}'")
                return False, secuencia
            secuencia.append(f"Paso {i+1}: '{char}' -> pop '{tope}' → pila: {contenedor}")

        # caracteres distintos no son tomados en cuenta :(
        else:
            secuencia.append(f"Paso {i+1}: '{char}' -> Rechazado")

    # ver si la pila quedó vacía
    if contenedor:
        secuencia.append(f"Fin: pila no vacía → {contenedor}")
        return False, secuencia

    secuencia.append("Fin: pila vacía → balanceado")
    return True, secuencia
