# Función para imprimir el tablero
def imprimir_tablero(tablero):
    # Imprimir cada fila del tablero, separada por líneas horizontales
    for fila in tablero:
        print(" | ".join(fila))
        print("---------")
    print()


# Función para verificar si se ha formado tres en raya
def verificar_tres_en_raya(tablero):
    # Comprobar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != " ":
            return fila[0]
    # Comprobar columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
            return tablero[0][i]
    # Comprobar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]
    # Si no hay ganador, retornar None
    return None


# Crear tablero vacío
tablero = [[" ", " ", " "] for i in range(3)]

# Definir los símbolos de los jugadores
jugador1 = "X"
jugador2 = "O"

# Comenzar el juego
turno = jugador1
ganador = None
while not ganador:
    # Imprimir el tablero
    imprimir_tablero(tablero)
    # Pedir al jugador que elija una fila y una columna
    fila = int(input(f"{turno}: Elige una fila (1-3): ")) - 1
    columna = int(input(f"{turno}: Elige una columna (1-3): ")) - 1
    # Comprobar que la casilla esté vacía
    if tablero[fila][columna] != " ":
        print("Casilla ocupada. Intenta de nuevo.")
        continue
    # Poner la ficha en el tablero
    tablero[fila][columna] = turno
    # Verificar si se ha formado tres en raya
    ganador = verificar_tres_en_raya(tablero)
    # Cambiar el turno
    turno = jugador2 if turno == jugador1 else jugador1

# Imprimir el tablero final
imprimir_tablero(tablero)

# Imprimir el resultado
if ganador:
    print(f"Ganó {ganador}!")
else:
    print("Empate.")
