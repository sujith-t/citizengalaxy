$(document).ready(function(){

    $(".btn-grad").click(function(){
        $('html, body').animate({scrollTop:0}, 'slow');
        $(".cls-label img").attr("src", "/static/images/loader.gif");
        setTimeout(function() {
            $(".cls-label img").setAttribute("src", "/static/images/loader.gif");

        }, 5000);
    });
});