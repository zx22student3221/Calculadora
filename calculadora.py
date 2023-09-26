# Función para realizar la suma
def suma(a, b):
    return a + b

# Función para realizar la resta
def resta(a, b):
    return a - b

# Función para realizar la multiplicación
def multiplicacion(a, b):
    return a * b

# Función principal para la calculadora
def calculadora():
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")


    # Solicitar al usuario que seleccione una operación
    opcion = input("Seleccione una operación (1/2/3): ")

    # Solicitar al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("Resultado:", suma(num1, num2))
    elif opcion == '2':
        print("Resultado:", resta(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    else:
        print("Opción no válida")

# Ejecutar la calculadora
calculadora()
