import grpc
import time
import matplotlib.pyplot as plt
import wine_pb2
import wine_pb2_grpc

def read_ids_from_file(file_path):
    with open(file_path, 'r') as file:
        ids = file.read().split(', ')
    return ids

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = wine_pb2_grpc.WineTasterStub(channel)
        ids = read_ids_from_file('datos.txt')
        times = []
        colors = []

        num_requests = 20000
        len_ids = len(ids)

        for index in range(num_requests):
            # Tomar ID de manera cíclica para asegurar uniformidad
            taster_id = ids[index % len_ids]
            start_time = time.time()
            response = stub.GetTasterInfo(wine_pb2.TasterRequest(id=taster_id))
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            times.append(elapsed_time)

            # Determinar el color en base al origen de la respuesta
            if getattr(response, 'fromCache', False):
                colors.append('green')
            else:
                colors.append('blue')

        # Calcular el tiempo promedio de respuesta total
        average_time = sum(times) / len(times)
        # Contar las respuestas desde caché y desde la base de datos
        cache_count = colors.count('green')
        db_count = colors.count('blue')

        # Graficar los tiempos de respuesta
        plt.figure(figsize=(10, 5))
        scatter = plt.scatter(range(num_requests), times, c=colors, edgecolors='w', alpha=0.5)
        plt.title('Tiempo de Respuesta por Solicitud Caché Particionado Random')
        plt.xlabel('Número de Petición (ID)')
        plt.ylabel('Tiempo de Respuesta (milisegundos)')
        plt.axhline(y=average_time, color='r', linestyle='-', label=f'Tiempo promedio: {average_time:.2f} ms')
        
        # Crear una leyenda personalizada con conteos
        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=f'Respuesta base de datos (n={db_count})',
                                      markerfacecolor='blue', markersize=10),
                           plt.Line2D([0], [0], marker='o', color='w', label=f'Respuesta caché (n={cache_count})',
                                      markerfacecolor='green', markersize=10),
                           plt.Line2D([0], [0], color='red', lw=2, label=f'Tiempo promedio: {average_time:.2f} ms')]
        plt.legend(handles=legend_elements, loc='best')

        plt.grid(True)
        plt.tight_layout()  # Ajustar automáticamente los parámetros del subplot
        plt.show()

if __name__ == '__main__':
    run()
