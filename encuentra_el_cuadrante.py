def determinar_cuadrante(x, y):
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            print("El punto se encuentra en el primer cuadrante.")
        elif x < 0 and y > 0:
            print("El punto se encuentra en el segundo cuadrante.")
        elif x < 0 and y < 0:
            print("El punto se encuentra en el tercer cuadrante.")
        else:
            print("El punto se encuentra en el cuarto cuadrante.")
    else:
        print("Las coordenadas no pueden ser cero.")

# Solicitar al usuario que ingrese las coordenadas
x_coord = float(input("Ingresa la coordenada x: "))
y_coord = float(input("Ingresa la coordenada y: "))

# Determinar en cuál cuadrante se encuentra el punto
determinar_cuadrante(x_coord, y_coord)
