const dropItem = document.getElementById("teca_tesis_taller7_drop-items");

new Sortable(dropItem, {
  animation: 350,
  ChosenClass: "sortable-chosen",
  dragClass: "sortable-drag"
});