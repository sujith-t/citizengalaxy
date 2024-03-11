$(document).ready(function(){

    let clzImgSelector = ".final-label img";
    let clzTextLabel = ".cls-label";

    $(".btn-grad").click(function(){
        //build the post payload first, validate all having numeric values
        var payload = {};
        $(".tbl-classify .numeric").each(function(inx) {
            let userVal = parseFloat($(this).val());
            if(isNaN(userVal)) {
                alert("Enter a valid numeric value for " + $(this).attr("id"));
                return;
            }
        });

        //immediately show processing image
        $(clzTextLabel).hide();
        $('html, body').animate({scrollTop:0}, 'slow');
        $(clzImgSelector).show();
        $(clzImgSelector).attr("src", "/static/images/loader.gif");

        //we make it sleep for 5 min to make user feel the data is processing
        setTimeout(callAPIToClassify, 5000);

        //post it to API
        /*$.ajax({
            type: "POST",
            url: "/api/v1/galaxy/classify",
            data: payload,
            async: false,
            success: function (response) {
                alert(response)
            }
        })*/

    });

    function callAPIToClassify() {
        //these are class E styles
        var clzGradient = "#bfe9f5, #74dbf7";
        var clzTextColor = "#059eeb";

        // SB class types
        clzGradient = "#f7dae4, #d46c7d, #f7dae4";
        clzTextColor = "#f00c58";

        //S Types
        clzGradient = "#b7ffb0, #96f78d";
        clzTextColor = "#16e002";

        $(clzImgSelector).hide();

        $(".final-label").css("background-image", 'linear-gradient(#bfe9f5, #74dbf7)');
        //post it to API
        $.ajax({
            type: "POST",
            url: "/api/v1/galaxy/classify",
            data: payload,
            async: false,
            success: function (response) {

                console.log(response);
            }
        });

        $(clzTextLabel).text("Sba");
        $(clzTextLabel).css("color", "#059eeb");
        $(clzTextLabel).show();
    }
});