$(document).ready(function(){
		var quoteSource=[
		{
			quote: "Puede ser importante para tu aréa o campo en el cual tu investigación se basa, puede ser la primera vez que alguien hable sobre el tema",
			name:"Importancia a nivel académico"
	    },
	    {
	    	quote:"Aquí se determina la utilidad de tu investigación, es decir para quíenes les puede ayudar o afectar",
	    	name:"Importancia a nivel social"
	    },
	    {
	    	quote:"Qué tecnicas o herramientas estas aportando que resulten de utilidad en otros estudios",
	    	name:"Importancia a nivel metodológico"
	    },
	    {
	    	quote:"La solución es suficiente para el problema, es nuevo enfoque o manera de abordar una solución",
	    	name:"Importancia de la solución"
	    },

	];
		

		$('#teca_tesis_taller9_just_quote').click(function(evt){
			//define the containers of the info we target
			var quote = $('#teca_tesis_taller9_just p').text();
			var quoteGenius = $('#teca_tesis_taller9_just_p').text();
			//prevent browser's default action
			evt.preventDefault();
			//getting a new random number to attach to a quote and setting a limit
			var sourceLength = quoteSource.length;
			var randomNumber= Math.floor(Math.random()*sourceLength);
			//set a new quote
			for(i=0;i<=sourceLength;i+=1){
			var newQuoteText = quoteSource[randomNumber].quote;
			var newQuoteGenius = quoteSource[randomNumber].name;
			//console.log(newQuoteText,newQuoteGenius);
      var timeAnimation = 500;
      var teca_tesis_taller9_just = $('#teca_tesis_taller9_just');
      //fade out animation with callback
      teca_tesis_taller9_just.fadeOut(timeAnimation, function(){
        teca_tesis_taller9_just.html('');
		teca_tesis_taller9_just.append('<p>'+newQuoteText+'</p>'+'<p id="teca_tesis_taller9_just_p">'+'-								'+newQuoteGenius+'</p>');
        //fadein animation.
        teca_tesis_taller9_just.fadeIn(timeAnimation);
      });  
			
			break;
		};//end for loop
	
	});//end quoteButton function
		
		
});//end document ready