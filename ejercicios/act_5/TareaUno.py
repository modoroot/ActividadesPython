muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

laberinto = []
for fila in range(5):
    lista_fila = []
    for columna in range(5):
        if (fila, columna) in muro:
            lista_fila.append('X')
        elif (fila, columna) == (4, 4):
            lista_fila.append('S')
        else:
            lista_fila.append(' ')
    laberinto.append(lista_fila)


def resolver_laberinto(fila_actual, columna_actual, camino, visitados):
    if (fila_actual, columna_actual) == (4, 4):
        return camino

    if fila_actual < 4 and (fila_actual + 1, columna_actual) not in muro and (
            fila_actual + 1, columna_actual) not in visitados:
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

    return None


pila = [(0, 0, [])]
visitados = set()

while len(pila) > 0:
    fila_actual, columna_actual, camino = pila.pop()
    if (fila_actual, columna_actual) not in visitados:
        visitados.add((fila_actual, columna_actual))
        resultado = resolver_laberinto(fila_actual, columna_actual, camino, visitados)
        if resultado is not None:
            print(resultado)
            break

for fila in laberinto:
    print(' '.join(fila))
