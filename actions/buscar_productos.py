from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.Producto import *
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
        categoria = tracker.get_slot("categoria")
        color = tracker.get_slot("color")
        talle = tracker.get_slot("talle")
        material = tracker.get_slot("material")
        tamano = tracker.get_slot("tamano")
        gusto = tracker.get_slot("gusto")
        marca = tracker.get_slot("marca")

        variables_sin_comillas = [categoria, marca]
        parametros = [categoria, color, material, talle, tamano, gusto, marca]
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
        lista_productos = []

        ultimo_intent = tracker.get_intent_of_latest_message()
        for resultado in result[0].get('Productos', []):  # Accede a la lista de productos en el resultado
            consulta_query = f'buscar_producto({resultado}, Producto).'
            result_p = consultarPL(port, path_db, consulta_query)
            if result_p:
                producto = result_p[0].get('Producto').get('args')
                id = producto[0]
                categorias = producto[1]
                atributos = {}
                for atributo in producto[2]:
                    clave = atributo.get('args')[0]
                    valor= atributo.get('args')[1]
                    atributos[clave] = valor

                descripciones = producto[3]
                marca = producto[4]
                precio = producto[6]
                stock = producto[5]     

                intents_to_Producto = {
                     'comprar_zapatos': 'zapatos',
                     'comprar_camiseta': 'camiseta',
                     'comprar_pantalones': 'pantalon',
                     'comprar_vestido': 'vestido',
                     'comprar_fruta': 'fruta',
                     'comprar_snack': 'snack',
                     'comprar_joyeria': 'joyeria'

                }

                tipo_p = intents_to_Producto.get(ultimo_intent)

                if tipo_p:
                     producto = crear_producto(tipo_p, id, marca, atributos, categorias, descripciones, precio, stock)
                     lista_productos.append(producto)          

        if not lista_productos:
            dispatcher.utter_message('No hay productos que coincidan con lo solicitado')
        else:
            dispatcher.utter_message('Estos son algunos productos que coinciden')
            for producto in lista_productos:
                print(type(producto), producto)
                des = producto.get_descripciones()
                print(type(des), des)
                i = random.randint(0, len(des)-1)
                tienda = buscar_tienda_producto(producto.get_id())
                dispatcher.utter_message(f'ID: {producto.get_id()} Descripcion: {des[i]} Cantidad disponible: {producto.get_stock()} Precio: {producto.get_precio()} Tienda: {tienda}\n')

        listado_resetear = ['categoria','color', 'material', 'talle', 'tamano', 'gusto', 'marca']
        listado_setear = []
        for parametro in listado_resetear:
            if parametro is not None:
                listado_setear.append(SlotSet(parametro, None))
        return listado_setear

def crear_producto(tipo_producto, id, marca, atributos, categorias, descripciones, precio, stock):

    tipo_prenda = ['zapatos', 'camiseta, pantalon, vestido']
    tipo_alimentos = ['alimento_liquido', 'fruta', 'snack']

    if tipo_producto in tipo_prenda:
        color = atributos.get('color')
        talle = atributos.get('talle')
        tipo = atributos.get('tipo')
        material = atributos.get('material')

        if tipo_producto == "zapatos": # zapatos
            suela = atributos.get('suela')
            return Zapatos(id, marca, talle, color, categorias, tipo, descripciones, material, suela, precio, stock)
        elif tipo_producto == "camiseta": # camisetas
            return Camiseta(id, marca, talle, color, categorias, material, tipo, descripciones, precio, stock)
        elif tipo_producto == "pantalon": # pantalones
            return Pantalon(id, marca, talle, color, categorias, tipo, descripciones, material, precio, stock)
        elif tipo_producto == "vestido":
            return Vestido(id, marca, talle, color, categorias, tipo, descripciones, material, precio, stock)

    elif tipo_producto in tipo_alimentos:
        if(tipo_producto == 'fruta'):
         peso = atributos.get('peso')
         return Fruta(id, marca, categorias, descripciones, peso, precio, stock)       
        elif tipo_producto == 'snack':
            peso = atributos.get('peso')
            gusto = atributos.get('gusto')
            return Snack(id, marca, categorias, descripciones, peso, precio, stock, gusto)
        elif tipo_producto == "alimento_liquido":
            volumen = atributos.get('volumen')
            vencimiento = atributos.get('vencimiento')
            tipo = atributos.get('tipo')
            return AlimentoLiquido(id, marca, categorias, descripciones, tipo, vencimiento, volumen, precio, stock)
        elif tipo_producto == 'joyeria':
            return Joyeria(id, marca, categorias, descripciones, material, precio, stock)
    else:
        return None
    
def buscar_tienda_producto(id):
    consulta_query = f"buscar_tienda_producto('{id}', Tienda)"
    result = consultarPL(port, path_db, consulta_query)
    tienda = result[0].get('Tienda')
    return tienda

