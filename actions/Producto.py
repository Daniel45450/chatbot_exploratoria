class Producto:
    def __init__(self, id, marca, categorias, descripciones, precio, stock):
        self._id = id
        self._marca = marca
        self._categorias = categorias  # Lista de categorías
        self._descripciones = descripciones
        self._precio = precio
        self._stock = stock

    def get_id(self):
        return self._id

    def get_marca(self):
        return self._marca

    def get_categorias(self):
        return self._categorias
    
    def get_descripciones(self):
        return self._descripciones
    
    def set_descripcion(self, nuevas_descripciones):
        self._descripciones = nuevas_descripciones

    def get_stock(self):
        return self._stock
    
    def get_precio(self):
        return self._precio

    def to_dict(self):
        return {
            "id": self._id,
            "marca": self._marca,
            "categorias": self._categorias,
            "descripciones": self._descripciones,
            "precio": self._precio,
            "stock": self._stock
        }

    
    def __str__(self):
        return f"ID: {self._id}, Marca: {self._marca}, Categorías: {', '.join(self._categorias)}"

class Prenda(Producto):
    def __init__(self, id, marca, talle, color, categorias, precio, tipo, descripciones, material, stock):
        super().__init__(id, marca, categorias, descripciones, precio, stock)
        self._talle = talle
        self._color = color
        self._tipo = tipo
        self._material = material
    
    def get_material(self):
        return self._material

    def get_talle(self):
        return self._talle

    def set_talle(self, nuevo_talle):
        self._talle = nuevo_talle

    def get_color(self):
        return self._color

    def set_color(self, nuevo_color):
        self._color = nuevo_color

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    def to_dict(self):
        prenda_dict = super().to_dict()  # Hereda los valores del producto base
        prenda_dict.update({
            "talle": self._talle,
            "color": self._color,
            "tipo": self._tipo,
            "material": self._material
        })
        return prenda_dict

    def __str__(self):
        return f"{super().__str__()}, Talle: {self._talle}, Color: {self._color}, Tipo: {self._tipo}, Material: {self._material}"
    
class Zapatos(Prenda):
    def __init__(self, id, marca, talle, color, categorias, tipo, descripciones, material, suela, precio, stock):
        super().__init__(id, marca, talle, color, categorias, precio, tipo, descripciones, material, stock)

        self._suela = suela

    def get_suela(self):
        return self._suela
    
    def to_dict(self):
        zapatos_dict = super().to_dict()
        zapatos_dict.update({
           'suela': self._suela 
        })
        return zapatos_dict

class Camiseta(Prenda):
    def __init__(self, id, marca, talle, color, categorias, material, tipo, descripciones, precio, stock):
        super().__init__(id, marca, talle, color, categorias, precio, tipo, descripciones, material, stock)
    
class Pantalon(Prenda):
    def __init__(self, id, marca, talle, color, categorias, tipo, descripciones, material, precio, stock):
        super().__init__(id, marca, talle, color, categorias, precio, tipo, descripciones, material, stock)

class Vestido(Prenda):
    def __init__(self, id, marca, talle, color, categorias, tipo, descripciones, material, precio, stock):
        super().__init__(id, marca, talle, color, categorias, tipo, descripciones, material, precio, stock)


class AlimentoLiquido(Producto):
    def __init__(self, id, marca, categorias, descripciones, tipo, vencimiento, volumen, precio, stock):
        super().__init__(id, marca, categorias, descripciones, precio, stock)
        self._tipo = tipo
        self._vencimiento = vencimiento
        self._volumen = volumen

    def get_tipo(self):
        return self._tipo
    
    def get_volumen(self):
        return self._volumen


    def to_dict(self):
        alimento_liquido_dict = super().to_dict()
        alimento_liquido_dict.update({
            "tipo": self._tipo,
            "vencimiento": self._vencimiento,
            "volumen": self._volumen,
        })
        return alimento_liquido_dict

class Snack(Producto):
    def __init__(self, id, marca, categorias, descripciones, peso, precio, stock, gusto):
        super().__init__(id, marca, categorias, descripciones, precio, stock)
        self._peso= peso   
        self._gusto = gusto

    def get_peso(self):
        return self._peso
    
    def get_gusto(self):
        return self._gusto
    
    def to_dict(self):
        snack_to_dict = super().to_dict()
        snack_to_dict.update({
            "gusto": self._gusto,
            "peso": self._peso
        })
        return snack_to_dict
    

class Fruta(Producto):
    def __init__(self, id, marca, categorias, descripciones, peso, precio, stock):
        super().__init__(id, marca, categorias, descripciones, peso*precio, stock)
        self._peso= peso

    def get_peso(self):
        return self._peso
    
    def to_dict(self):
        fruta_to_dict = super().to_dict()
        fruta_to_dict.update({
            'peso': self._peso
        })

        return fruta_to_dict

    def __str__(self):
        return super().__str__() + f", Peso: {self._peso}"
    

class Joyeria(Producto):
    def __init__(self, id, marca, categorias, descripciones, material, precio, stock):
        super().__init__(id, marca, categorias, descripciones, precio, stock)
        self._material = material

    def get_material(self):
        return self._material
    
    def to_dict(self):
        joyeria_to_dict = super().to_dict()
        joyeria_to_dict.update({
            "material": self._material
        })
        return joyeria_to_dict