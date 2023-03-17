# Se pregunta por pantalla la renta anual del usuario
renta = float(input('Introduce tu renta anual: '))

# Calcula el IRPF a pagar según la renta anual del usuario
if renta <= 12450:
    irpf = 0.19 * renta
elif renta <= 20200:
    irpf = 2365.5 + 0.24 * (renta - 12450)
elif renta <= 35200:
    irpf = 4543 + 0.3 * (renta - 20200)
else:
    # renta > 35200 (no es necesario comprobarlo porque ya se ha comprobado antes)
    irpf = 11777 + 0.37 * (renta - 35200)

# Muestra el IRPF que debe pagar el usuario por pantalla con dos decimales
print(f'IRPF a pagar: {irpf:.2f} euros')
