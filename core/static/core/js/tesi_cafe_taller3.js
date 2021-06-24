$( function() {
    $( ".teca_tesis_taller3_stick" ).draggable();
  } );

$(document).on('click','.teca_tesis_taller3_btn-del', function(){
	Swal.fire({
  title: '¿Quieres eliminar esta nota?',
  type: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Si, borar!'
}).then((result) => {
  if (result.value) {
		$(this).closest('.teca_tesis_taller3_stick').remove();
    Swal(
      'Deleted!',
      'Your note has been deleted.',
      'success'
    )
  }
});
})
var i = 0;
$('.teca_tesis_taller3_btn-add').click(function(){
	i++;
	$('body').prepend('<div class="teca_tesis_taller3_stick"><input type="checkbox"><div class="teca_tesis_taller3_nota nota-rounded"><textarea placeholder="Puedes escribir aquí"></textarea></div> <div class="teca_tesis_taller3_action"><button type="button" class="teca_tesis_taller3_btn teca_tesis_taller3_btn-del"><i class="fa fa-trash"></i></button></div></div>');
	$('.teca_tesis_taller3_stick:last').find('textarea').attr('id', 'teca_tesis_taller3_nota-'+i);
	$( ".teca_tesis_taller3_stick" ).draggable();
});
$(document).ready(function(){
	$('textarea').bind('input propertychange',function(){
		var notes= $(this).val();
		if (typeof(Storage) !== "undefined") {
			localStorage.value = notes;
			// alert(localStorage.value);
		}else {
    $('body').innerHTML = "Sorry, your browser does not support web storage...";
  }
	 });
});