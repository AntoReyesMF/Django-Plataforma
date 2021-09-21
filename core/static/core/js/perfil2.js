'use strict'
/*----------------------------  Editar nickname ---------------------------- */ 
function edit_nickname() {

    // alert("perfil2");
    var nickname = document.querySelector("#perfil2_presentacion_username_2");
    // console.log(" Presionaste el boton de editar nick name. :) ");
    nickname.style.display = "block";

}
function close_edit_nickname(){

    // alert("Cerrar edit nickname");
    var nickname1 = document.querySelector("#perfil2_presentacion_username_2");
    // console.log("Cerraste el editor de presentacion.");
    nickname1.style.display = "none";
}
/*----------------------------  Editar nickname ---------------------------- */ 

/*----------------------------  Editar descripcion ---------------------------- */ 

function edit_descripcion() {

    // alert("editar descripcion");
    var nickname = document.querySelector("#perfil2_presentacion_descripcion_edit");
    // console.log(" Presionaste el boton de editar descripcion :) ");
    nickname.style.display = "block";
    
}
function close_edit_descripcion(){
    // alert("cerrar edit descripcion");
    var descripcion = document.querySelector("#perfil2_presentacion_descripcion_edit");
    descripcion.style.display = "none";
}
/*----------------------------  Editar descripcion ---------------------------- */ 

/*----------------------------  Editar Foto de fondo ---------------------------- */ 
var fotos_fondo = document.querySelector("#perfil2_imagenesFondo")

function editar_fotoFondo() {
    fotos_fondo.style.display = "block";
}

function cerrar_editarFotoFondo() {
    fotos_fondo.style.display = "none";
}
/*----------------------------  Editar Foto de fondo ---------------------------- */ 

/*----------------------------  Editar Foto de Perfil ---------------------------- */ 
var fotos_perfil = document.querySelector("#imagenesPerfil")

function editar_fotoPerfil() {
    fotos_perfil.style.display = "block";
}

function cerrar_editarFotoPeril() {
    fotos_perfil.style.display = "none";
}
/*----------------------------  Editar Foto de Perfil ---------------------------- */ 
