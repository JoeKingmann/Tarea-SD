import grpc
import random
import wine_pb2
import wine_pb2_grpc

def run():
    # Establecer conexión con el servidor gRPC
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = wine_pb2_grpc.WineTasterStub(channel)
        valid_ids = []  # Usar una lista para permitir IDs repetidos
        total_ids = 130000  # Número máximo de IDs
        target_count = 100000  # Objetivo de IDs válidos a recolectar
        
        while len(valid_ids) < target_count:  # Continuar hasta recolectar 50,000 IDs válidos
            random_id = random.randint(1, total_ids)  # Generar un ID aleatorio entre 1 y 130,000
            response = stub.GetTasterInfo(wine_pb2.TasterRequest(id=str(random_id)))
            taster_name = response.tasterName
            
            # Verificar que la respuesta no sea 'ID no existe' ni 'Taster no identificado'
            if taster_name not in ["ID no existe", "Taster no identificado"]:
                valid_ids.append(str(random_id))  # Añadir el ID a la lista si es válido

        # Guardar los IDs válidos en un archivo txt
        with open('valid_ids.txt', 'w') as file:
            file.write(', '.join(valid_ids))  # Escribir todos los IDs válidos en formato '1', '2', '3', etc.

if __name__ == '__main__':
    run()