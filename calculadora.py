# Función para realizar la suma
def suma(a, b):
    return a + b

# Función para realizar la resta
def resta(a, b):
    return a - b

# Función principal para la calculadora
def calculadora():
    print("Calculadora")

    # Solicitar al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Resultado:", suma(num1, num2))

# Ejecutar la calculadora
calculadora()
