$(document).ready(function() {

    $('#welcomeImage').click(function(event) {
        $(this).css('top', '-100vh');
    });
    $('.menu-bar').click(function(event) {
        $('nav').addClass('deploy');
    });
    $('header').hover(function(event) {
        $('nav').removeClass('deploy');
    });

});
