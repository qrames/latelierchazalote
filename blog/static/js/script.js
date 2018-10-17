$(document).ready(function() {

    $('#welcomeImage').click(function(event) {
        $(this).css('top', '-100vh');
    });
    $('.menu-bar').on('click',function(event) {
        $('nav').addClass('deploy');
    });
    $('header').on('mouseleave', function(event) {
        $('nav').removeClass('deploy');
    });

    $('#formset div').formset();
});
