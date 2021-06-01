$(document).ready(function() {
  
  var stack1 = $('#vexi_taller_10_stack1');
  
  stack1.removeClass('vexi_taller_10_start');
  
  stack1.hammer().on('tap', function(event) {
    stack1.addClass('hover');
    event.stopPropagation();
  });
  
  
  $(document).hammer().on('tap', function(event) {
    stack1.removeClass('hover');
    $('.vexi_taller_10_card').removeClass('hover');
  });
  
  $('.vexi_taller_10_card').hammer().on('tap', function(event) {
      $('.vexi_taller_10_card').removeClass('hover');
      $(this).addClass('hover');
  });
});