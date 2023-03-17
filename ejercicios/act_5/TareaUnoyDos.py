# Definición de los obstáculos del laberinto
muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# Crea la matriz del laberinto con las posiciones y los muros
laberinto = []
for fila in range(5):
    lista_fila = []
    for columna in range(5):
        # Se revisa si la ubicación está dentro de los muros del laberinto, si es así se agrega una 'X'
        if (fila, columna) in muro:
            lista_fila.append('X')
        # Si no es un muro, pero es la salida del laberinto, entonces se agrega una 'S'
        elif (fila, columna) == (4, 4):
            lista_fila.append('S')
        # Sino, se agrega un espacio vacío ' '
        else:
            lista_fila.append(' ')
    # Se agrega cada fila creada a la lista principal que contiene el laberinto completo
    laberinto.append(lista_fila)


# Definición de la función que resuelve el laberinto
def resolver_laberinto(fila_actual, columna_actual, camino, visitados):
    # Verifica si es posible moverse hacia abajo, derecha, arriba o izquierda.
    # En el caso de que sea posible, se añade a la pila
    if (fila_actual, columna_actual) == (4, 4):
        # Si llegamos al final del laberinto, se devuelve el camino hasta esa posición
        return camino
    if fila_actual < 4 and (fila_actual + 1, columna_actual) not in muro and (
            fila_actual + 1, columna_actual) not in visitados:
        # Se agrega en la pila la nueva posición, se actualiza el camino realizado hasta ese punto agregando el
        # movimiento, y se marca como visitado
        pila.append((fila_actual + 1, columna_actual, camino + ['Abajo']))

    if columna_actual < 4 and (fila_actual, columna_actual + 1) not in muro and (
            fila_actual, columna_actual + 1) not in visitados:
        pila.append((fila_actual, columna_actual + 1, camino + ['Derecha']))

    if fila_actual > 0 and (fila_actual - 1, columna_actual) not in muro and (
            fila_actual - 1, columna_actual) not in visitados:
        pila.append((fila_actual - 1, columna_actual, camino + ['Arriba']))

    if columna_actual > 0 and (fila_actual, columna_actual - 1) not in muro and (
            fila_actual, columna_actual - 1) not in visitados:
        pila.append((fila_actual, columna_actual - 1, camino + ['Izquierda']))

    # Si no hay más lugares para movernos, se retorna None

    return None


# Inicialización de la pila y el conjunto de visitados
pila = [(0, 0, [])]
visitados = set()

# Encuentra una solución posible para salir del laberinto
while len(pila) > 0:
    # Se saca la última posición agregada en la pila
    fila_actual, columna_actual, camino = pila.pop()
    if (fila_actual, columna_actual) not in visitados:
        # Se marca esta posición cómo visitada
        visitados.add((fila_actual, columna_actual))
        # Se llama a la función para verificar movimientos desde este punto
        resultado = resolver_laberinto(fila_actual, columna_actual, camino, visitados)
        # Si hay un resultado válido, se imprime el camino y se rompe el ciclo
        if resultado is not None:
            print(resultado)
            break

# Imprime la matriz del laberinto
for fila in laberinto:
    print(' '.join(fila))
