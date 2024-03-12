/**
 * @author Sujith T
 * Deus et Scientia Erit Pactum Meum 2024
 **/
$(document).ready(function(){

    let clzImgSelector = ".final-label img";
    let clzTextLabel = ".cls-label";
    let payload = {};

    $(".btn-grad").click(function(){
        //build the post payload first, validate all having numeric values
        $(".tbl-classify .numeric").each(function(inx) {
            let userVal = parseFloat($(this).val());
            if(isNaN(userVal)) {
                alert("Enter a valid numeric value for " + $(this).attr("id"));
                return false;
            }

            payload[$(this).attr("id")] = userVal;
        });

        //immediately show processing image
        $(clzTextLabel).hide();
        $('html, body').animate({scrollTop:0}, 'slow');
        $(clzImgSelector).show();
        $(clzImgSelector).attr("src", "/static/images/loader.gif");

        //we make it sleep for 5 min to make user feel the data is processing
        setTimeout(callAPIToClassify, 5000);
    });

    function callAPIToClassify() {
        //class E type default style
        let clzGradient = "#bfe9f5, #74dbf7";
        let clzTextColor = "#059eeb";

        $(clzImgSelector).hide();

        //post it to API
        $.ajax({
            type: "POST",
            url: "/api/v1/galaxy/classify",
            data: payload,
            async: false,
            success: function (data, status, jqXHR) {
                //when successful response received
                if (jqXHR.status === 200) {
                    let clazz = data[0][0];

                    //if SB types
                    if(clazz.search(/SB[a-d]/) > -1) {
                        clzGradient = "#f7dae4, #d46c7d, #f7dae4";
                        clzTextColor = "#f00c58";
                    }

                    //if S types
                    if(clazz.search(/S[a-e]/) > -1) {
                        clzGradient = "#b7ffb0, #96f78d, #b7ffb0";
                        clzTextColor = "#16e002";
                    }

                    $(".final-label").css("background-image", "linear-gradient(" + clzGradient + ")");
                    $(clzTextLabel).text(clazz);
                    $(clzTextLabel).css("color", clzTextColor);
                    $(clzTextLabel).show();
                }
            },
            fail: function (response) {
                console.log("Failure....");
                console.log(response);
            }
        });

        payload = {};
    }

});