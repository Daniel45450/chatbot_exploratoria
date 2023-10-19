from swiplserver import PrologMQI

def consultarPL(port, path_db, query):
    with PrologMQI(port) as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query(path_db)
            response = prolog_thread.query(query)
            print(str(response), type(response))
        
    return response