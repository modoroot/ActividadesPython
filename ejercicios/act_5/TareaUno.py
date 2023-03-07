# Definición de las coordenadas del laberinto y los muros que lo componen (fila, columna)
muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# Crea el laberinto a partir de las coordenadas de los muros y los espacios vacíos
laberinto = []
for fila in range(5):
    # Crea una lista vacía para la fila actual del laberinto y la añade a la lista
    lista_fila = []
    for columna in range(5):
        # Comprueba si la casilla actual está en la lista de muros
        if (fila, columna) in muro:
            # Si hay muro, se añade una X a la lista
            lista_fila.append('X')
        # Comprueba si la casilla actual es la de salida del laberinto
        elif (fila, columna) == (4, 4):
            # Si es la casilla de salida, se añade una S a la lista
            lista_fila.append('S')
        else:
            # Si no hay muro, se añade un espacio en blanco
            lista_fila.append(' ')
    # Añadir la lista de la fila actual al laberinto
    laberinto.append(lista_fila)

# Mostrar el laberinto por pantalla con los espacios entre cada casilla
for fila in laberinto:
    print(' '.join(fila))