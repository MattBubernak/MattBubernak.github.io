$(document).ready(function () {
	// Activates wow.js
	new WOW().init();

	//Allows for smooth scrolling
	$('a[href^="#"]').on('click',function (e) {
		    e.preventDefault();
		    var target = this.hash;
		    var $target = $(target);

		    $('html, body').stop().animate({
		        'scrollTop': $target.offset().top
		    }, 900, 'swing', function () {
		        window.location.hash = target;
		    });
	});


	// Hide all project tabs except for default
    var cur_tab = "discGolf";
    $(".apiTex").hide();
    document.getElementById(cur_tab + "H").style.opacity=1;
    $("#discGolfContent").show();

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
        } else {
            jQuery('.back-to-top').fadeOut(duration);
        }
    });


});