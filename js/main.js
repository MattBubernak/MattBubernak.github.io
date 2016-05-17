$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip()
    
	// Activates wow.js
	new WOW().init();

	//Allows for smooth scrolling
	$('a[href^="#"]').on('click',function (e) {
		    e.preventDefault();
		    var target = this.hash;
		    var $target = $(target);

		    $('html, body').stop().animate({
		        'scrollTop': $target.offset().top-50
		    }, 900, 'swing', function () {
		        window.location.hash = target;
		    });
	});


	// Hide all project tabs except for default
    var cur_tab = "cityTrendz";
    $(".apiTex").hide();
    document.getElementById(cur_tab + "H").style.opacity=1;
    $("#cityTrendzContent").show();

    // Change visibility to clicked link.
    $(".apiCat").click(function () {
        document.getElementById(cur_tab + "H").style.opacity = .6;
        $("#" + cur_tab + "Content").fadeOut(300);
        cur_tab = event.target.id.toString().substr(0, event.target.id.toString().length - 1);
        document.getElementById(cur_tab + "H").style.opacity = 1;
        $("#" + cur_tab + "Content").delay(300).fadeIn(300);
    });

    // Handle the back to top arrow. 
    var offset = 250;
    var duration = 300;
    jQuery('.back-to-top').fadeOut(0);
    jQuery(window).scroll(function() {
        if (jQuery(this).scrollTop() > offset) {
            jQuery('.back-to-top').fadeIn(duration);
            jQuery('#menubar').fadeIn(duration);
        } else {
            jQuery('.back-to-top').fadeOut(duration);
            jQuery('#menubar').fadeOut(duration);
        }
    });


    var waypointAbout = new Waypoint({
      element: document.getElementById('About'),
      handler: function() {
        jQuery('#navbar-about').addClass("active").show();
        jQuery('#navbar-resume').removeClass("active").show();
        jQuery('#navbar-portfolio').removeClass("active").show();
        jQuery('#navbar-contact').removeClass("active").show();
      },
      offset:100
    })
    var waypointAbout = new Waypoint({
      element: document.getElementById('About'),
      handler: function() {
        jQuery('#navbar-about').addClass("active").show();
        jQuery('#navbar-resume').removeClass("active").show();
        jQuery('#navbar-portfolio').removeClass("active").show();
        jQuery('#navbar-contact').removeClass("active").show();
      },
      offset:-100
    })
    var waypointAbout = new Waypoint({
      element: document.getElementById('Resume'),
      handler: function() {
        jQuery('#navbar-about').removeClass("active").show();
        jQuery('#navbar-resume').addClass("active").show();
        jQuery('#navbar-portfolio').removeClass("active").show();
        jQuery('#navbar-contact').removeClass("active").show();
      },
      offset:100
    })
    var waypointAbout = new Waypoint({
      element: document.getElementById('Resume'),
      handler: function() {
        jQuery('#navbar-about').removeClass("active").show();
        jQuery('#navbar-resume').addClass("active").show();
        jQuery('#navbar-portfolio').removeClass("active").show();
        jQuery('#navbar-contact').removeClass("active").show();
      },
      offset:-100
    })
    var waypointAbout = new Waypoint({
      element: document.getElementById('Portfolio'),
      handler: function() {
        jQuery('#navbar-about').removeClass("active").show();
        jQuery('#navbar-resume').removeClass("active").show();
        jQuery('#navbar-portfolio').addClass("active").show();
        jQuery('#navbar-contact').removeClass("active").show();
      },
      offset:100
    })
    var waypointAbout = new Waypoint({
      element: document.getElementById('Portfolio'),
      handler: function() {
        jQuery('#navbar-about').removeClass("active").show();
        jQuery('#navbar-resume').removeClass("active").show();
        jQuery('#navbar-portfolio').addClass("active").show();
        jQuery('#navbar-contact').removeClass("active").show();
      },
      offset:-100
    })
    var waypointAbout = new Waypoint({
      element: document.getElementById('Contact'),
      handler: function() {
        jQuery('#navbar-about').removeClass("active").show();
        jQuery('#navbar-resume').removeClass("active").show();
        jQuery('#navbar-portfolio').removeClass("active").show();
        jQuery('#navbar-contact').addClass("active").show();
      },
      offset:100
    })
    var waypointAbout = new Waypoint({
      element: document.getElementById('Contact'),
      handler: function() {
        jQuery('#navbar-about').removeClass("active").show();
        jQuery('#navbar-resume').removeClass("active").show();
        jQuery('#navbar-portfolio').removeClass("active").show();
        jQuery('#navbar-contact').addClass("active").show();
      },
      offset:-100
    })

});