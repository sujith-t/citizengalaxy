/**
 * @author Sujith T
 * Deus et Scientia Erit Pactum Meum 2024
 **/
$(document).ready(function(){

    let clzImgSelector = ".final-label img";
    let clzTextLabel = ".cls-label";
    let payload = {};

    //clicking of classify button
    $("#btn-clazz").click(handleClassification);

    //clicking of import CSV file button
    $("#file_import").change(handleCSVFileImport);

    //clicking of export link
    $("#export_csv").click(handleDataExportToCsv);

    /**
     * Export values to CSV file for easy reuse(import) again
     **/
    function handleDataExportToCsv() {
        let outString = "field,value\r\n";
        $(".numeric").each(function(inx, element) {
            outString += $(element).attr("id") + "," + $(element).val() + "\r\n";
        });

        $(this).attr("href", 'data:text/plain;charset=utf-8,' + encodeURIComponent(outString));
        $(this).attr("download", "galaxy_data_export.csv");
    }

    /**
     * Handler function for classify button click
     **/
    function handleClassification() {
        //build the post payload first, validate all having numeric values
        let errorFound = false;
        $(".tbl-classify .numeric").each(function (inx) {
            let userVal = parseFloat($(this).val());
            if (isNaN(userVal)) {
                alert("Enter a valid numeric value for " + $(this).attr("id"));
                errorFound = true;
                return false;
            }

            payload[$(this).attr("id")] = userVal;
        });

        if (errorFound === true)
            return false;

        //immediately show processing image
        $(clzTextLabel).hide();
        $('html, body').animate({scrollTop: 0}, 'slow');
        $(clzImgSelector).show();
        $(clzImgSelector).attr("src", "/static/images/loader.gif");

        //we make it sleep for 5 min to make user feel the data is processing
        setTimeout(callAPIToClassify, 5000);
    }

    /**
     * Imports data from the CSV file for quick filling of text boxes
     **/
    function handleCSVFileImport() {
        let fileReader = new FileReader();
        fileReader.onload = function () {
            let rows = fileReader.result.split("\n");
            for(let x = 0; x < rows.length; x++) {
                let rowVals = rows[x].split(",");
                let floatVal = parseFloat(rowVals[1]);
                if(isNaN(floatVal))
                    continue;

                $("#" + rowVals[0]).val(floatVal);
            }
        };

        fileReader.readAsText($('#file_import').prop('files')[0]);
    }

    /**
     * Handler function for setTimeout
     * Provides a visual effect of processing to the user and makes AJAX call to the REST web service
     **/
    function callAPIToClassify() {
        //class E type default style
        let clzGradient = "#bfe9f5, #74dbf7";
        let clzTextColor = "#059eeb";
        const HTTP_ERROR_CODE = 400;

        $(clzImgSelector).hide();

        //post it to API
        $.ajax({
            type: "POST",
            url: "/api/v1/galaxy/classify",
            data: payload,
            async: false,
            success: function (data) {
                //when error messages received from the server
                if (data.hasOwnProperty("status") && data.status === HTTP_ERROR_CODE) {
                    //we restore the visual look
                    $(".final-label").css("background-image", "linear-gradient(#bfe9f5, #74dbf7)");
                    $(clzTextLabel).hide();
                    $(clzImgSelector).attr("src", "/static/images/planet.png");
                    $(clzImgSelector).show();

                    let entries = Object.entries(data.errors)
                    let errorMsgs = "";
                    entries.map( ([key, val] = entry) => {
                        errorMsgs += (key + " - " + val[0] + "\n");
                    });

                    alert(errorMsgs);
                    return;
                }

                let clazz = data[0];

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
            },
            fail: function (response) {
                alert("Failed in processing for galaxy type identification");
                console.log("Failure....");
                console.log(response);
            }
        });

        payload = {};
    }
});