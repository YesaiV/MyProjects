#Librerias
#=========================================
import numpy as np
import matplotlib.pyplot as plt

#Mapeo del panadero
#===============================================

# Crear la matriz inicial con un gradiente (rojo y azul)
rows, cols = 124, 124
canal_rojo = np.linspace(0, 1, cols).reshape(1, -1).repeat(rows, axis=0)
canal_azul = np.linspace(0, 1, rows).reshape(-1, 1).repeat(cols, axis=1)
canal_verde = np.zeros((rows, cols))
imagen = np.stack((canal_rojo, canal_verde, canal_azul), axis=2)

def panadero(imagen, iteraciones=1):
    """
    Aplica la transformación del panadero múltiples veces.
    :param imagen: Matriz RGB de la imagen (alto x ancho x 3).
    :param iterations: Número de iteraciones de la transformación.
    :return: Imagen transformada tras las iteraciones.
    """
    plt.imshow(imagen)
    plt.axis('off')  # Quitar los ejes para visualizar mejor
    plt.title(f"({0} iteraciones)",fontsize=20)
    plt.show()

    transformada = imagen.copy()

    iter = 1

    for _ in range(iteraciones):
        rows, cols, canales = transformada.shape

        # Nueva matriz con el doble de columnas y la mitad de filas
        new_rows, new_cols = rows // 2, cols * 2
        nueva_imagen = np.zeros((new_rows, new_cols, canales))

        for i in range(new_rows):  # Filas de la nueva matriz
            for j in range(new_cols):  # Columnas de la nueva matriz
                if j % 2 == 0:  # Columnas pares
                    nueva_imagen[i, j] = transformada[2 * i, j // 2]
                else:  # Columnas impares
                    nueva_imagen[i, j] = transformada[2 * i + 1, (j - 1) // 2]

        # Dividir la nueva matriz en mitades
        left_half = nueva_imagen[:, :cols, :]
        right_half = nueva_imagen[:, cols:, :]

        # Crear una matriz con dimensiones originales
        transformada = np.zeros_like(imagen)
        transformada[:rows // 2, :, :] = right_half  # Mitad superior
        transformada[rows // 2:, :, :] = left_half  # Mitad inferior

        plt.imshow(transformada)
        plt.axis('off')  # Quitar los ejes para visualizar mejor
        plt.title(f"({iter} iteraciones)",fontsize=20)
        plt.show()

        iter += 1

    return transformada

# Aplicar la transformación del panadero con varias iteraciones
iteraciones = 32   #400
Transformacicion = panadero(imagen, iteraciones=iteraciones)
