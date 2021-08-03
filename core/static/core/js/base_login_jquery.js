$(document).ready(function () {
    alert("Menu Login");

    var mostrar = $("#mostrar");
    var ocultar = $("#ocultar");

    var menu2 = $("#menu2");

    mostrar.click(function(){
        menu2.show("slow");
        mostrar.hide("slow");
    });

    ocultar.click(function(){
        menu2.hide("slow");
        mostrar.show("slow");
    });


});