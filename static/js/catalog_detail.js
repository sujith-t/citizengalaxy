/**
 * @author Sujith T
 * Deus et Scientia Erit Pactum Meum 2024
 **/
$(document).ready(function(){
    let rightAscension = parseFloat($("#ra").val());
    let declination = parseFloat($("#dec").val());

    //var corsAttr = new EnableCorsAttribute("*", "*", "*");
    //config.EnableCors(corsAttr);
    let aladin;
    A.init.then(() => {
        aladin = A.aladin('#aladin-lite-div', {survey: "P/DSS2/color", fov:1.5});
        aladin.gotoRaDec(rightAscension, declination)

        let descMsg = "RA: " + rightAscension + "<br />Dec: " + declination + "<br />Class: " + $("#clz-minor").val();
        let marker1 = A.marker(rightAscension, declination, {popupTitle: $("#iauname").val(), popupDesc: descMsg});
        let markerLayer = A.catalog();
        aladin.addCatalog(markerLayer);
        markerLayer.addSources([marker1]);
    });

    $(".detail-download").click(handleFileExport);

    function handleFileExport() {
        let outString = "field,value\r\n";
        $.ajax({
            type: "GET",
            url: "/api/v1/catalog/id/" + $("#obj_id").val() + "/detail",
            async: false,
            success: function (data) {
                for (k in data) {
                    outString += k + "," + data[k] + "\r\n";
                }
            }
        });

        $(this).attr("href", 'data:text/plain;charset=utf-8,' + encodeURIComponent(outString));
        $(this).attr("download", $("#obj_id").val() + ".csv");
    }
});
