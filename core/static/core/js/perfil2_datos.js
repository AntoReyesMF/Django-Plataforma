$(document).ready(function(){
	
	// Variables
	var clickedTab = $(".perfil2_tabs > .perfil2_tab_active");
	var tabWrapper = $(".perfil2_tab_content");
	var activeTab = tabWrapper.find(".perfil2_tab_active");
	var activeTabHeight = activeTab.outerHeight();
	
	// Show tab on page load
	activeTab.show();
	
	// Set height of wrapper on page load
	tabWrapper.height(activeTabHeight);
	
	$(".perfil2_tabs > li").on("click", function() {
		
		// Remove class from active tab
		$(".perfil2_tabs > li").removeClass("perfil2_tab_active");
		
		// Add class active to clicked tab
		$(this).addClass("perfil2_tab_active");
		
		// Update clickedTab variable
		clickedTab = $(".perfil2_tabs .perfil2_tab_active");
		
		// fade out active tab
		activeTab.fadeOut( function() {
			
			// Remove active class all tabs
			$(".perfil2_tab_content> li").removeClass("perfil2_tab_active");
			
			// Get index of clicked tab
			var clickedTabIndex = clickedTab.index();

			// Add class active to corresponding tab
			$(".perfil2_tab_content > li").eq(clickedTabIndex).addClass("perfil2_tab_active");
			
			// update new active tab
			activeTab = $(".perfil2_tab_content > .perfil2_tab_active");
			
			// Update variable
			activeTabHeight = activeTab.outerHeight();
			
			// Animate height of wrapper to new tab height
			tabWrapper.stop().animate({
				height: activeTabHeight
			}, function() {
				
				// Fade in active tab
				activeTab.delay(50).fadeIn(250);
				
			});
		});
	});
	

});