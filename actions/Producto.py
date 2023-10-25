class Producto:
    def __init__(self, id, marca, categorias, descripciones):
        self._id = id
        self._marca = marca
        self._categorias = categorias  # Lista de categorías
        self._descripciones = descripciones

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

    def to_dict(self):
        return {
            "id": self._id,
            "marca": self._marca,
            "categorias": self._categorias,
            "descripciones": self._descripciones
        }

    
    def __str__(self):
        return f"ID: {self._id}, Marca: {self._marca}, Categorías: {', '.join(self._categorias)}"
    
class Zapato(Producto):
    def __init__(self, id, marca, talle, color, categorias, tipo, descripciones):
        super().__init__(id, marca, categorias, descripciones)
        self._talle = talle
        self._color = color
        self._tipo = tipo

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

    def __str__(self):
        return f"{super().__str__()}, Talle: {self._talle}, Color: {self._color}, Tipo: {self._tipo}"
    
    def to_dict(self):
        zapato_dict = super().to_dict()  # Hereda los valores del producto base
        zapato_dict.update({
            "talle": self._talle,
            "color": self._color,
            "tipo": self._tipo
        })
        return zapato_dict

class Camiseta(Producto):
    def __init__(self, id, marca, talle, color, categorias, material, tipo, descripciones):
        super().__init__(id, marca, categorias, descripciones)
        self._material = material
        self._talle = talle
        self._tipo = tipo
        self._color = color

    def get_tipo(self):
        return self._tipo
    
    def set_tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    def get_material(self):
        return self._material
    
    def set_material(self, nuevo_material):
        self._material = nuevo_material
    
    def get_talle(self):
        return self._talle

    def set_talle(self, nuevo_talle):
        self._talle = nuevo_talle

    def get_color(self):
        return self._color

    def set_color(self, nuevo_color):
        self._color = nuevo_color

    def to_dict(self):
        camiseta_dict = super().to_dict()  # Hereda los valores del producto base
        camiseta_dict.update({
            "talle": self._talle,
            "color": self._color,
            "material": self._material,
            "tipo": self._tipo
        })
        return camiseta_dict
    
    def __str__(self):
        return f"{super().__str__()}, Material: {self._material}"
