from swiplserver import PrologMQI

def consultarPL(port, path_db, query):
    # Se establece una conexión con PrologMQI utilizando un puerto especificado
    with PrologMQI(port) as mqi:
        
        # Se crea un hilo de PrologMQI para realizar consultas
        with mqi.create_thread() as prolog_thread:
            
            # Se carga la base de datos Prolog desde la ruta proporcionada
            prolog_thread.query(path_db)
            
            # Se realiza la consulta especificada en Prolog
            response = prolog_thread.query(query)

    # Se devuelve la respuesta obtenida de la consulta
    return response
