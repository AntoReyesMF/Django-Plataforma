$(document).ready(function () {
    // alert("Menu Login");

    var mostrar = $("#mostrar");
    var ocultar = $("#ocultar");

    var menu2 = $("#menu2");

    mostrar.click(function(){
        menu2.toggle("slide");
        mostrar.hide();
    });

    ocultar.click(function(){
        menu2.toggle("slide");
        mostrar.show();
    });


});