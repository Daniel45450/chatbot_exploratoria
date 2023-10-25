:- use_module(library(lists)).
:- dynamic usuario/6.


%producto(id, [categorias], [atributos], [descripciones], marca,
% cantidad_stock, precio)

producto(p1, [ropa, camiseta],[talle="M", color="rojo", tipo="corta", material="algodon"], ["Camiseta roja de talla M manga corta"], zara, 5, 200).

producto(p2, [ropa, pantalon], [talle="32", color="azul"], ["Pantalon azul de talla 32"], kill, 8, 300).

producto(p3, [ropa, vestido], [talle="S", color="negro"], ["Vestido negro de talla S"], dafiti, 6, 150).

%zapatillas
producto(p4, [zapatilla, calzado, zapatillas], [talle="38", color="rojo", tipo="comunes"], ["Zapatilla nike talle 38 rojas"], nike, 10, 600).
producto(p5, [zapatilla, calzado, deportivo, zapatillas], [talle="30", color="blanco", tipo="deportivas"], ["Zapatilla deportivas nike talle 30 blancas"], adidas, 5, 620).
producto(p6, [zapatillas, calzado, zapatilla], [talle="36", color="negro", tipo="formal"], ["zapatos formales talle 36 de color negro"], gucci, 2, 750).
producto(p13, [zapatilla, calzado, zapatillas], [talle="40", color="rojo", tipo="comunes"], ["Zapatilla nike talle 40 rojas"], nike, 10, 700).
producto(p14, [calzado, zapatos, zapato], [talle="38", color="negro", tipo="comunes"], ["zapatos marca nike talle 38 negros"], nike, 10, 1000).

% comida[tamano[liquidos=L, solidos=[grande, mediano, chico]]
% capacidad=kilos o unidades

producto(p7, [alimentos, lacteos], [tamano="1"], ["Leche entera de 1 litro"], serenisima, 10, 80).
producto(p8, [alimentos, frutas], [tamano="mediano"], ["Manzana", "Manzana fresca", "Manzana fresca de temporada"], gala, 5, 500).
producto(p9, [alimentos, snacks], [tamano="0.25", gusto=salado], ["Chips de papas", "Chips de papas salados", "Bolsa de chips de papas salados"], lays, 9, 20).

% joyer�a
producto(p10, [joyas, collares], [material="plata"], ["Collar de plata", "Collar de plata con colgante de coraz�n", "Collar de plata con colgante de coraz�n", "Joyer�a Fina"], boucheron, 3, 150).
producto(p11, [joyas, anillos], [material="diamante"], ["Anillo de compromiso", "Anillo de compromiso con diamante", "Anillo de compromiso con diamante de corte brillante"], avon, 2, 300).
producto(p12, [joyas, pulseras], [material="oro"], ["Pulsera de oro", "Pulsera de oro con eslabones entrelazados", "Pulsera de oro con eslabones entrelazados"], cartier, 1, 400).

% local(nombre, [productos], horario)

local("Tienda de Ropa",[p1,p2,p3],"13:00-18:00").
local("Tienda de Calzado",[p4,p5,p6,p13],"08:00-17:00").
local("Tienda de Comida",[p7,p8,p9],"12:00-23:00").
local("Tienda de joyeria",[p10,p11,p12],"08:00-13:00").

esta_en_stock(Producto, Tienda, CantidadNecesaria) :-
    local(Tienda, Productos, _), member(Producto, Productos), producto(Producto, _, _, _, _, Cantidad_Stock,_), Cantidad_Stock >= CantidadNecesaria.

filtrar_por_color(Color, Productos) :- findall(Producto, (
    producto(Producto, _, Atributos, _, _, _, _),
    member(color=Color, Atributos)
), Productos).

filtrar_por_talle(Talle, Productos) :- findall(Producto, (
    producto(Producto, _, Atributos, _, _, _, _),
    member(talle=Talle, Atributos)
), Productos).

filtrar_por_categoria(Categoria, Productos) :- findall(Producto, (
    producto(Producto, Categorias, _, _, _, _, _),
    member(Categoria, Categorias)
), Productos).

filtrar_precio_min(Precio, Productos):- findall(Producto, (
    producto(Producto, _, _, _, _, _, PrecioProducto), PrecioProducto >= Precio
), Productos).

filtrar_precio_max(Precio, Productos):- findall(Producto, (
    producto(Producto, _, _, _, _, _, PrecioProducto), PrecioProducto =< Precio
), Productos).

obtener_usuario(Nombre, Email, Telefono, Contrasena, Productoscomprados, Direccion) :- usuario(Nombre, Email, Telefono, Contrasena, Productoscomprados, Direccion).

filtrar_por_marca(Marca, Productos):- findall(Producto, (producto(Producto, _, _, _, MarcaProducto, _, _), MarcaProducto = Marca), Productos).

filtrarProductos(Categoria, Color, Material, Talle, Tamano, Gusto, Marca, Productos) :-
    findall(Producto, (
        producto(Producto, Categorias, Atributos, _, MarcaProducto, _, _),
        (Categoria = [] ; member(Categoria, Categorias)),
        (Color = [] ; member(color=Color, Atributos)),
        (Material = [] ; member(material=Material, Atributos)),
        (Talle = [] ; member(talle=Talle, Atributos)),
        (Tamano = [] ; member(tamano=Tamano, Atributos)),
        (Gusto = [] ; member(gusto=Gusto, Atributos)),
        (Marca = [] ; Marca = MarcaProducto)
    ), Productos).

buscar_producto(Id, Producto):- producto(Id, Categoria, Atributos, Desc, Marca, Stock, Precio), Producto =  producto(Id, Categoria, Atributos, Desc, Marca, Stock, Precio).


% usuarios (usuario(nombre, email, contrasena,telefono
% [productoscomprados], direccion)).

usuario("Daniel", "daniel@hotmail.com", "2281682520", "1234", [], "MARTIN M").
usuario("Juan", "juan@gmail.com", "5555555555", "5678", [], "GONZALEZ J").
usuario("Ana", "ana@yahoo.com", "9999999999", "9876", [], "RODRIGUEZ A").
usuario("Luis", "luis@hotmail.com", "3333333333", "4321", [], "PEREZ L").
usuario("María", "maria@gmail.com", "7777777777", "2468", [], "LOPEZ M").
usuario("Carlos", "carlos@yahoo.com", "1111111111", "1357", [], "SANCHEZ C").
usuario("Laura", "laura@hotmail.com", "6666666666", "8765", [], "GARCIA L").
usuario("Sofía", "sofia@gmail.com", "2222222222", "9876", [], "MARTINEZ S").
usuario("Pedro", "pedro@yahoo.com", "4444444444", "5432", [], "FERNANDEZ P").
usuario("Elena", "elena@hotmail.com", "8888888888", "6789", [], "DIAZ E").

existe_usuario(Email):- usuario(_,Email,_,_,_,_).

agregar_usuario(Nombre, Email, Telefono, Contrasena, Direccion) :-
    not(existe_usuario(Email)), assert(usuario(Nombre, Email, Telefono, Contrasena, [], Direccion)).

