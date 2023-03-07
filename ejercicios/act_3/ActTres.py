# Crear matriz de butacas
butacas = [['L' for j in range(4)] for i in range(5)]


# Función para imprimir la matriz de butacas
def mostrar_butacas():
    for fila in butacas:
        print(' '.join(fila))


# Función para reservar una butaca
def reservar_butaca():
    while True:
        # Preguntar por la fila y columna de la butaca a reservar
        fila = int(input('Introduce la fila (1-5): '))
        columna = int(input('Introduce la columna (1-4): '))

        # Verificar si la fila y columna son válidas
        if fila < 1 or fila > 5 or columna < 1 or columna > 4:
            print('Fila o columna no válida. Introduce otra vez.')
            continue

        # Verificar si la butaca está libre
        if butacas[fila - 1][columna - 1] == 'O':
            print('Butaca ocupada. Introduce otra vez.')
            continue

        # Reservar la butaca
        butacas[fila - 1][columna - 1] = 'O'
        print('Butaca reservada.')
        break


# Mostrar la matriz de butacas y preguntar por reservas hasta que el usuario no quiera hacer más
while True:
    mostrar_butacas()
    respuesta = input('¿Quieres hacer una reserva? (S/N): ')
    if respuesta == 's':
        reservar_butaca()
    else:
        print('Hasta luego.')
        break
