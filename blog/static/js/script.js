$(document).ready(function() {

    $('#welcomeImage').click(function(event) {
        $(this).css('top', '-100vh');
    });
    $('.menu-bar').click(function(event) {
        $('nav').css('min-width', '800px');
        $('nav ul li').css('visibility', 'visible');
        $('.menu-bar').css('display', 'none');
        $('header').mousedown(function(event) {
            $('nav').css('min-width', '400px');
            $('nav ul li').css('visibility', 'hidden');
            $('.menu-bar').css('display', 'block');
        });
    });

});
