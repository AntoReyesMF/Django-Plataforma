$(".teca_tesis_taller4_sujeto").click(function() {
  $(".teca_tesis_taller4_sujeto").addClass("active");
  $(".teca_tesis_taller4_problema").removeClass("active");
  $(".teca_tesis_taller4_tiempo").removeClass("active");
  $(".teca_tesis_taller4_espacio").removeClass("active");
  $("#line").addClass("one");
  $("#line").removeClass("two");
  $("#line").removeClass("three");
  $("#line").removeClass("four");
})

$(".teca_tesis_taller4_problema").click(function() {
  $(".teca_tesis_taller4_problema").addClass("active");
  $(".teca_tesis_taller4_sujeto").removeClass("active");
  $(".teca_tesis_taller4_tiempo").removeClass("active");
  $(".teca_tesis_taller4_espacio").removeClass("active");
  $("#line").addClass("two");
  $("#line").removeClass("one");
  $("#line").removeClass("three");
  $("#line").removeClass("four");
})

$(".teca_tesis_taller4_tiempo").click(function() {
  $(".teca_tesis_taller4_tiempo").addClass("active");
  $(".teca_tesis_taller4_problema").removeClass("active");
  $(".teca_tesis_taller4_sujeto").removeClass("active");
  $(".teca_tesis_taller4_espacio").removeClass("active");
  $("#line").addClass("three");
  $("#line").removeClass("two");
  $("#line").removeClass("one");
  $("#line").removeClass("four");
})

$(".teca_tesis_taller4_espacio").click(function() {
  $(".teca_tesis_taller4_espacio").addClass("active");
  $(".teca_tesis_taller4_problema").removeClass("active");
  $(".teca_tesis_taller4_tiempo").removeClass("active");
  $(".teca_tesis_taller4_sujeto").removeClass("active");
  $("#line").addClass("four");
  $("#line").removeClass("two");
  $("#line").removeClass("three");
  $("#line").removeClass("one");
})

$(".teca_tesis_taller4_sujeto").click(function() {
  $("#teca_tesis_taller4_first").addClass("active");
  $("#teca_tesis_taller4_second").removeClass("active");
  $("#teca_tesis_taller4_third").removeClass("active");
  $("#teca_tesis_taller4_fourth").removeClass("active");
})

$(".teca_tesis_taller4_problema").click(function() {
  $("#teca_tesis_taller4_first").removeClass("active");
  $("#teca_tesis_taller4_second").addClass("active");
  $("#teca_tesis_taller4_third").removeClass("active");
  $("#teca_tesis_taller4_fourth").removeClass("active");
})

$(".teca_tesis_taller4_tiempo").click(function() {
  $("#teca_tesis_taller4_first").removeClass("active");
  $("#teca_tesis_taller4_second").removeClass("active");
  $("#teca_tesis_taller4_third").addClass("active");
  $("#teca_tesis_taller4_fourth").removeClass("active");
})

$(".teca_tesis_taller4_espacio").click(function() {
  $("#fteca_tesis_taller4_first").removeClass("active");
  $("#teca_tesis_taller4_second").removeClass("active");
  $("#teca_tesis_taller4_third").removeClass("active");
  $("#teca_tesis_taller4_fourth").addClass("active");
})