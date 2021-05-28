(function($) {

	var tabs =  $(".tabs li a");
  
	tabs.click(function() {
		var terms = this.hash.replace('/','');
		tabs.removeClass("active");
		$(this).addClass("active");
    $("#vexi_taller6_terms").find('p').hide();
    $(terms).fadeIn(200);
	});

})(jQuery);