
  (function ($) {
  
    "use strict";
  
      // NAVBAR
      $('.navbar-nav .nav-link').click(function(){
          $(".navbar-collapse").collapse('hide');
      });
  
      $(window).scroll(function() {    
          var scroll = $(window).scrollTop();
  
          if (scroll >= 50) {
              $(".navbar").addClass("sticky-nav");
          } else {
              $(".navbar").removeClass("sticky-nav");
          }
      });
  
      // BACKSTRETCH SLIDESHOW
      $('#section_1').backstretch([
        "/static/img/microsoft-edge-FAaz8lkinzs-unsplash.jpg", 
        "/static/img/surface-1x5jnhtlp3Y-unsplash.jpg",
        "/static/img/surface-71_s6RDJpGc-unsplash.jpg"
      ],  {duration: 2000, fade: 750});
      
    })(window.jQuery);
  
  
  