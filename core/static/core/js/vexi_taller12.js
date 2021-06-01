$(document).ready(function() { 
  
  $(".icon").click(function() {
    var icon = $(this).attr('class').replace("-icon icon","");
    $("."+icon +"-screen").animate({top: '4%'});
  });

  $(".vexi_taller12_home-button").click(function() {
    $(".app").animate({top: '110%'});
  });

});