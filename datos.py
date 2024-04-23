import random

def seleccionar_ids_aleatorios(archivo_entrada, archivo_salida, n_seleccion):
    # Leer el archivo de entrada
    with open(archivo_entrada, 'r') as file:
        ids = file.read().strip().split(', ')

    # Seleccionar aleatoriamente los IDs (con repetición)
    ids_seleccionados = random.choices(ids, k=n_seleccion)

    # Guardar los IDs seleccionados en el archivo de salida
    with open(archivo_salida, 'w') as file:
        file.write(', '.join(ids_seleccionados))

# Usar la función para seleccionar 50000 IDs aleatorios
seleccionar_ids_aleatorios('valid_ids.txt', 'datos.txt', 50000)
