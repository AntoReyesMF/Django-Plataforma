$('document').ready(function() {
  var quotes = [{
  }, {
    quote: 'NO gastes más de lo que puedes pagar mensualmente: lo ideal es que tu TDC tenga una deuda de un 30% de tu sueldo',
 
  }, {
    quote: 'NO uses el efectivo: Si se te antojaron unos taquitos en la calle o comprar en el mercadito, lo mejor será que no uses tu tarjeta para evitar las comisiones.',

  }, {
    quote: 'Trata de evitar comprar a plazos: Si vas a comprar algo trata de que puedas pagarlo en su totalidad al siguiente corte de tu tarjeta, así evitarás intereses. La única manera en la que te recomendamos comprar algo a plazos es en caso de que tu compra tenga una vida superior a lo que durará tu deuda.',

  }];
  
  $('#vexi_taller11_generate').click(function() {
    var q = quotes[Math.floor((Math.random() * quotes.length) + 1)];
    $('.quote').text(q.quote);
 
  });
  
});