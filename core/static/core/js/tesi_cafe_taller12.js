var swiper = new Swiper('.teca_tesis_taller12_swiper', {
  slidesPerView: 1,
  spaceBetween: 20,
  effect: 'fade',
  loop: true,
  speed: 300,
  mousewheel: {
    invert: false,
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
    dynamicBullets: true
  },
  // Navigation arrows
  navigation: {
    nextEl: '.teca_tesis_taller12_button-next',
    prevEl: '.teca_tesis_taller12_button-prev',
  }
});