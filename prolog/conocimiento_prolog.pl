:- use_module(library(lists)).

%producto(id, [categorias], [atributos], [descripciones], marca,
% cantidad_stock, precio)

producto(p1, [ropa, camiseta],[talle="M", color="rojo"], ["Camiseta roja de talla M"], zara, 5, 200).
producto(p2, [ropa, pantal�n], [talle="32", color="azul"], ["Pantal�n azul de talla 32"], kill, 8, 300).
producto(p3, [ropa, vestido], [talle="S", color="negro"], ["Vestido negro de talla S"], dafiti, 6, 150).

% calzado
producto(p4, [zapatilla, calzado], [talle="38", color="rojo"], ["Zapatilla nike talle 38 rojas"], nike, 10, 600).
producto(p5, [zapatilla, calzado, deportivo], [talle="30", color="blanco"], ["Zapatilla deportivas nike talle 30 blancas"], adidas, 5, 620).
producto(p6, [zapatillas, calzado, formal], [talle="36", color="negro"], ["zapatos formales talle 36 de color negro"], gucci, 2, 750).
producto(p13, [zapatilla, calzado], [talle="40", color="rojo"], ["Zapatilla nike talle 40 rojas"], nike, 10, 700).

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

filtrar_por_marca(Marca, Productos):- findall(Producto, (producto(Producto, _, _, _, MarcaProducto, _, _), MarcaProducto = Marca), Productos).

% usuarios (usuario(nombre, email, contrasena, [productoscomprados])).


