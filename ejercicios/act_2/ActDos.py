# Inicializar el saldo a cero y la lista de operaciones vacía
saldo = 0
operaciones = []

# Pedir al usuario que realice una operación hasta que decida terminar
while True:
    # Mostrar las opciones de operación
    print("¿Qué operación desea realizar?")
    print("1. Ingreso")
    print("2. Reintegro")
    print("3. Salir")

    # Pedir al usuario que ingrese una opción
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    # Realizar operación de ingreso
    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad a ingresar: "))
        saldo += cantidad  # Actualizar el saldo
        operaciones.append(cantidad)  # Agregar la cantidad a la lista de operaciones
        print(f"El saldo actual es: {saldo}")

    # Realizar operación de reintegro
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a sacar: "))
        if saldo < cantidad:  # Comprobar si hay suficiente saldo
            print("No hay saldo suficiente para realizar el reintegro.")
        else:
            saldo -= cantidad  # Actualizar el saldo
            operaciones.append(-cantidad)  # Agregar la cantidad negativa a la lista de operaciones
            print(f"El saldo actual es: {saldo}")

    # Terminar el programa
    elif opcion == "3":
        break

    # Opción inválida
    else:
        print("Opción inválida.")

# Crear listas de ingresos y reintegros a partir de la lista de operaciones
ingresos = [cantidad for cantidad in operaciones if cantidad > 0]
reintegros = [-cantidad for cantidad in operaciones if cantidad < 0]

# Mostrar el saldo final, los ingresos y los reintegros
print(f"El saldo final es: {saldo}")
print(f"Los ingresos fueron: {ingresos}")
print(f"Los reintegros fueron: {reintegros}")
