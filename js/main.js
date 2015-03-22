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
    document.getElementById(cur_tab + "H").style.color = "#b69e40";
    $("#discGolfContent").show();

    // Change visibility to clicked link.
    $(".apiCat").click(function () {
        document.getElementById(cur_tab + "H").style.color = 'white';
        $("#" + cur_tab + "Content").fadeOut(300);
        cur_tab = event.target.id.toString().substr(0, event.target.id.toString().length - 1);
        document.getElementById(cur_tab + "H").style.color = "#b69e40";
        $("#" + cur_tab + "Content").delay(300).fadeIn(300);
    });


});