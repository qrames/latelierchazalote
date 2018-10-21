$(document).ready(function() {

    setTimeout(function(){
        $('#welcomeImage').css('top', '-100vh');
    },15000);

    $('#welcomeImage').click(function(event) {
        $(this).css('top', '-100vh');
    });
    $('.menu-bar').on('click',function(event) {
        $('nav').addClass('deploy');
        setTimeout(function(){
            $('nav').removeClass('deploy');
        },10000);

    });
    $('header').on('mouseleave', function(event) {
        $('nav').removeClass('deploy');
    });

    $('#formset div').formset();
});
