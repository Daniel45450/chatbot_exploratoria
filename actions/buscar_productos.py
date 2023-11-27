from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from swiplserver import PrologMQI
from actions.consultarPL import consultarPL
from rasa_sdk.events import SlotSet
from actions.config import *

import random

class AccionBuscarProductos(Action):
    def name(self):
        return "action_buscar_productos"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        dispatcher.utter_message(f"Buscando productos... por favor espere")

        entities = tracker.latest_message.get("entities")

        # Inicializar variables para cada rol
        categoria = None
        color = None
        talle = None
        material = None
        peso = None
        gusto = None
        marca = None
        tipo = None

        categoria, color, talle, material, peso, gusto, marca, tipo = asignar_entidades_a_atributos_del_producto(entities)
        result = filtrar_productos(categoria, color, material, talle, peso, gusto, marca, tipo)
        print(result)
        lista_productos = []
        for resultado in result[0].get('Productos', []):  # itero los id de los productos
            producto =  buscar_producto(resultado)
            tienda = buscar_tienda_producto(producto.get('id'))
            producto.update({
                'tienda': tienda
            })
            if producto:
                lista_productos.append(producto)          

        if not lista_productos:
            dispatcher.utter_message('No hay productos que coincidan con lo solicitado')
        else:
            dispatcher.utter_message('Estos son algunos productos que coinciden')
            for producto in lista_productos:
                des = producto.get('descripciones')
                i = random.randint(0, len(des)-1)
                dispatcher.utter_message(f'ID: {producto.get("id")} Descripcion: {des[i]} Cantidad disponible: {producto.get("stock")} Precio: {producto.get("precio")} Tienda: {producto.get("tienda")}\n')
        return[SlotSet('productos', lista_productos)]

def asignar_entidades_a_atributos_del_producto(entities):
    # Inicializar un diccionario para almacenar los atributos del producto
    producto_atributos = {
        "categoria": None,
        "color": None,
        "talle": None,
        "material": None,
        "peso": None,
        "gusto": None,
        "marca": None,
        "tipo": None
    }

    # Mapeo de roles a claves en el diccionario
    mapeo_roles = {
        "categoria": "categoria",
        "color": "color",
        "talle": "talle",
        "material": "material",
        "peso": "peso",
        "gusto": "gusto",
        "marca": "marca",
        "tipo": "tipo"
    }

    # Asignar entidades al diccionario de atributos del producto
    for entity in entities:
        if entity.get("entity") == "producto" and entity.get("role") in mapeo_roles:
            clave = mapeo_roles[entity.get("role")]
            valor = entity.get("value")
            producto_atributos[clave] = valor

    # Desempaquetar los valores del diccionario para devolverlos individualmente
    return producto_atributos["categoria"], producto_atributos["color"], producto_atributos["talle"], producto_atributos["material"], producto_atributos["peso"], producto_atributos["gusto"], producto_atributos["marca"], producto_atributos["tipo"]


def buscar_tienda_producto(id):
    # dado un id de un producto busca que tienda vende ese producto
    consulta_query = f"buscar_tienda_producto('{id}', Tienda)"
    result = consultarPL(port, path_db, consulta_query)
    tienda = result[0].get('Tienda')
    return tienda

def filtrar_productos(categoria, color, material, talle, peso, gusto, marca, tipo):
    # Devuelve una lista con los id de los productos que coinciden con los criterios de busqueda
    variables_sin_comillas = [categoria, marca]
    parametros = [categoria, color, material, talle, peso, gusto, marca, tipo]
    consulta_query = "filtrarProductos("
    for parametro in parametros:
        if parametro is not None:
            if parametro in variables_sin_comillas:
                consulta_query += f'{parametro},'
            else:
                consulta_query += f'"{parametro}",'
        else:
            consulta_query += '[],'
    consulta_query += f'Productos).'
    result = consultarPL(port, path_db, consulta_query)
    return result
    
def buscar_producto(id):
    # dado un id busca un producto y sus caracteristicas y lo retorna en un diccionario
    consulta_query = f'buscar_producto({id}, Producto).'
    result_p = consultarPL(port, path_db, consulta_query)
    # declaro un diccionario para ir construyendo un producto 
    producto = {}
    if result_p:
        element = result_p[0].get('Producto').get('args')
        producto = {
            'id': element[0],
            'categorias': element[1],
            'descripciones': element[3],
            'marca': element[4],
            'precio': element[6],
            'stock': element[5]   
        }
        # se procesan atributos como el color, talle y tipo dependiendo el producto seran distintos
        for atributo in element[2]:
            clave = atributo.get('args')[0]
            valor = atributo.get('args')[1]
            producto.update({
                clave: valor
            })
    return producto

