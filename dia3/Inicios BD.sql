-- ESTO ES UN COMENTARIO
-- SQL ES UN LENGUAJE DE SENTENCIA ESTRUCTURADO EN EL CUAL, MEDIANTE
-- UNAS SENTENCIA PODEMOS EXTRAER, AGREGAR,ELIMINAR, ACTUALIZAR, INFO DE UNA BASE DE DATOS
# ESTO ES OTRO COMENTARIO
create database pruebas;
use pruebas

create table alumnos(
	#ACA AHORA VENDRA TODAS LAS COLUMNAS DE ESA TABLA DE ALUMNOS
    nombre varchar(40),
    apellido varchar(25),
    sexo varchar(9),
    numero_emergencia int,
    religion varchar(10),
    fecha_nacimiento date,
    );