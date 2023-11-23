:- use_module(library(lists)).
:- dynamic usuario/6.


%producto(id, [categorias], [atributos], [descripciones], marca,
% cantidad_stock, precio)

%camisetas
producto(p1, [ropa, camiseta, camisetas],[talle="M", color="rojo", tipo="corta", material="algodon"], ["Camiseta roja de talla M manga corta"], zara, 5, 200).

%pantalones
producto(p2, [ropa, pantalon, pantalones], [talle="32", color="azul", tipo="largo", material="denim"], ["Pantalon azul de talla 32"], kill, 8, 300).
producto(p20, [ropa, pantalon, jean, pantalones, jeans], [talle="40", color="azul", tipo="largo", material="denim"], ["Jean de color azul talle 40"], kill, 2, 250).
producto(p19, [ropa, pantalon, pantalones], [talle="36", color="celeste", tipo="corto", material="seda"], ["Pantalon corto celeste talle 36"], kill, 2, 350).


%vestidos
producto(p3, [ropa, vestido, vestidos], [talle="S", color="negro", material="algodon", tipo="largo"], ["Vestido negro de talla S"], dafiti, 6, 150).
producto(p16, [ropa, vestido,vestidos], [talle="M", color="rojo", material="seda", tipo="corto"], ["Vestido rojo de talla M"], rinu, 6, 200).

%zapatillas
producto(p4, [zapatilla, calzado, zapatillas], [talle="38", color="rojo", tipo="comunes", material="Malla"], ["Zapatilla nike talle 38 rojas"], nike, 10, 600).
producto(p5, [zapatilla, calzado, zapatillas], [talle="30", color="blanco", tipo="deportivas", material="Malla"], ["Zapatilla deportivas nike talle 30 blancas"], adidas, 5, 620).
producto(p6, [calzado, zapatilla, zapatillas], [talle="36", color="negro", tipo="formal"], ["zapatos formales talle 36 de color negro"], gucci, 2, 750).
producto(p13, [zapatilla, calzado, zapatillas], [talle="40", color="rojo", tipo="comunes"], ["Zapatilla nike talle 40 rojas"], nike, 10, 700).
producto(p14, [calzado, zapato, zapatos], [talle="38", color="negro", tipo="comunes"], ["zapatos marca nike talle 38 negros"], nike, 10, 1000).

% comida[tamano[liquidos=L, solidos=[grande, mediano, chico]]
% capacidad=kilos o unidades

%alimentos_liquidos
producto(p7, [alimentos, lacteos, leche], [volumen="1", tipo="entera", vencimiento="26/10/2024"], ["Leche entera de 1 litro"], serenisima, 10, 80).
producto(p15, [alimentos, lacteos, leche], [volumen="1", tipo="light", vencimiento="30/08/2024"], ["Leche light de 1 litro"], don_atilo, 6, 32).
producto(p22, [alimentos, agua], [volumen="1", tipo="mineral"], ["agua mineral de 1 litro"], el_sifon, 6, 32).


%alimentos_frutas
producto(p8, [alimentos, frutas, manzana, manzanas], [peso="1"], ["Manzana", "Manzana fresca", "Manzana fresca de temporada"], gala, 5, 500).
producto(p23, [alimentos, frutas, banana, platano, platanos, banana, bananas], [peso="1"], ["Bananas", "Bananas fresca", "Bananas de temporada"], gala, 7, 150).

%%alimentos_snacks
producto(p9, [alimentos, snack, snacks, aperitivo, bocadillo], [peso="0.25", gusto="salado"], ["Chips de papas", "Chips de papas salados", "Bolsa de chips de papas salados"], lays, 9, 20).
producto(p17, [alimentos, dorito, aperitivo, bocadillo, doritos], [peso="0.25", gusto="salado"], ["Doritos salados 0.25 grs", "Bolsa de doritos salados"], doritos, 3, 15).
producto(p18, [alimentos, bizcochito, aperitivo, bocadillo], [peso="0.25", gusto="dulce"], ["Biscochitos dulces", "don satur dulces"], don_satur, 3, 15).

% joyer�a
producto(p10, [joyas, collar, collares], [material="plata"], ["Collar de plata", "Collar de plata con colgante de corazon", "Collar de plata con colgante de corazon", "Joyeria Fina"], boucheron, 3, 150).
producto(p11, [joyas, anillo, anillos], [material="diamante"], ["Anillo de compromiso", "Anillo de compromiso con diamante", "Anillo de compromiso con diamante de corte brillante"], avon, 2, 300).
producto(p12, [joyas, pulsera, pulseras], [material="oro"], ["Pulsera de oro", "Pulsera de oro con eslabones entrelazados", "Pulsera de oro con eslabones entrelazados"], cartier, 1, 400).

% local(nombre, [productos], horario)

local("Moda Elegante",[p1,p2,p3,p19,p20],"13:00","18:00").
local("Pisadas de Estilo",[p4,p5,p6,p13,p14],"08:00","17:00").
local("Sabores del Dia",[p7,p8,p9,p15,p17,p18],"12:00","23:00").
local("Frescura Natural",[p23],"12:00","23:00").
local("Brillos Exquisitos",[p10,p11,p12],"08:00","13:00").
local("Atuendos Encantadores",[p16],"08:00","13:00").
local("Agua Pura Oasis",[p22],"08:00","13:00").


%ofertas oferta(tienda, efectivo, 6 cuotas, 12cuotas)
oferta("Moda Elegante",  0.5).
oferta("Pisadas de Estilo", 0.4).

buscar_ofertas(Tiendas) :- findall((Tienda, Efectivo), oferta(Tienda, Efectivo), Tiendas).


buscar_tienda_producto(Id, Tienda):- local(Tienda, Productos, _, _), member(Id, Productos).


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

filtrarProductos(Categoria, Color, Material, Talle, Peso, Gusto, Marca, Tipo, Productos) :-
    findall(Producto, (
        producto(Producto, Categorias, Atributos, _, MarcaProducto, _, _),
        (Categoria = [] ; member(Categoria, Categorias)),
        (Color = [] ; member(color=Color, Atributos)),
        (Material = [] ; member(material=Material, Atributos)),
        (Talle = [] ; member(talle=Talle, Atributos)),
        (Peso = [] ; member(peso=Peso, Atributos)),
        (Gusto = [] ; member(gusto=Gusto, Atributos)),
        (Marca = [] ; Marca = MarcaProducto),
        (Tipo = []; member(tipo=Tipo, Atributos))
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

