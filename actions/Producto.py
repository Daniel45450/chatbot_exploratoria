class Producto:
    def __init__(self, id, marca, talle, categoria, color):
        self._id = id
        self._marca = marca
        self._talle = talle
        self._categoria = categoria
        self._color = color

    # Getter para el atributo id
    def get_id(self):
        return self._id

    # Setter para el atributo id
    def set_id(self, nuevo_id):
        self._id = nuevo_id

    # Getter para el atributo marca
    def get_marca(self):
        return self._marca

    # Setter para el atributo marca
    def set_marca(self, nueva_marca):
        self._marca = nueva_marca

    # Getter para el atributo talle
    def get_talle(self):
        return self._talle

    # Setter para el atributo talle
    def set_talle(self, nuevo_talle):
        self._talle = nuevo_talle

    # Getter para el atributo categoría
    def get_categoria(self):
        return self._categoria

    # Setter para el atributo categoría
    def set_categoria(self, nueva_categoria):
        self._categoria = nueva_categoria

    # Getter para el atributo color
    def get_color(self):
        return self._color

    # Setter para el atributo color
    def set_color(self, nuevo_color):
        self._color = nuevo_color

    def __str__(self):
        return f"ID: {self._id}, Marca: {self._marca}, Talle: {self._talle}, Categoría: {self._categoria}, Color: {self._color}"