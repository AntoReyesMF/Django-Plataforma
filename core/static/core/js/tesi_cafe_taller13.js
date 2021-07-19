$(document).ready(function () {

  $('.teca_tesis_taller13_card').on('click', function () {

    if ($(this).hasClass('open')) {
      $(this).removeClass('open');
    } else {
      $('.teca_tesis_taller13_card').removeClass('open');
      $(this).addClass('open');
    }

  });

});