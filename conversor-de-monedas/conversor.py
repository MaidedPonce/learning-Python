
def conversor(valor):

    pesos = input("Ingresa cuántos pesos tienes ")
    pesos = float(pesos)

    dolares = pesos / valor
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print(f"tienes {dolares} dolares")


menu = """
Hola, selecciona tu moneda 🤑💵💰
1. Pesos mexicanos
2. Pesos chilenos
3. Pesos colombianos

"""
opcion = int(input(menu))
if opcion == 1:
    conversor(20.80)
elif opcion == 2:
    conversor(993.17)
elif opcion == 3:
    conversor(4578.88) 
else:
    print("Ingrese una opción valida o vayase al demonio:)")
