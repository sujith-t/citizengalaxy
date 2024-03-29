/**
 * @author Sujith T
 * Deus et Scientia Erit Pactum Meum 2024
 **/
$(document).ready(function(){

    $(".ra-set").change(rightAscensionToDegrees);

    $(".dec-set").change(declinationToDegrees);


    function rightAscensionToDegrees() {
        let num = parseFloat($(this).val());
        if(isNaN(num)) {
            alert("You have entered incorrect value " + $(this).val());
            $(this).val("");
            return;
        }

        if($(this).attr("id") === "hour" && (num < 0 || num >= 24)) {
            alert("Hour should be between 0-23, you have entered " + num);
            return;
        }

        if($(this).attr("id") === "minutes" && (num < 0 || num >= 60)) {
            alert("Minutes should be between 0-59, you have entered " + num);
            return;
        }

        if($(this).attr("id") === "seconds" && (num < 0 || num >= 60)) {
            alert("Seconds should be between 0-59, you have entered " + num);
            return;
        }

        let flag = calculateDegrees('right-ascension', "hour", "minutes", "seconds", "ra");
        if(!flag)
            alert("The right ascension exceeded 24hrs");
    }
    function declinationToDegrees() {
        let num = parseFloat($(this).val());
        if(isNaN(num)) {
            alert("You have entered incorrect value " + $(this).val());
            $(this).val("");
            return;
        }

        if($(this).attr("id") === "deg" && (num > 90 || num < -90)) {
            alert("Degree should be between -90 and +90, you have entered " + num);
            return;
        }

        if($(this).attr("id") === "arc_min" && num >= 60) {
            alert("Arc-minutes should be between 0-59, you have entered " + num);
            return;
        }

        if($(this).attr("id") === "arc_sec" && num >= 60) {
            alert("Arc-seconds should be between 0-59, you have entered " + num);
            return;
        }

        let flag = calculateDegrees('declination', "deg", "arc_min", "arc_sec", "dec");
        if(!flag)
            alert("The declination is either less than -90 or more than +90 degrees");
    }
    function calculateDegrees(option, num1Id, num2Id, num3Id, destId) {

        let hourOrDeg = parseFloat($("#" + num1Id).val());
        if (isNaN(hourOrDeg))
            hourOrDeg = 0;
        let minutes = parseFloat($("#" + num2Id).val());
        if (isNaN(minutes))
            minutes = 0;
        let seconds = parseFloat($("#" + num3Id).val());
        if (isNaN(seconds))
            seconds = 0;

        if (option === "declination" && hourOrDeg < 0) {
            minutes *= -1;
            seconds *= -1;
        }

        let calculatedValue = hourOrDeg + (minutes / 60) + (seconds / 3600);
        $("#" + destId).val("");

        if (option === "right-ascension")
            calculatedValue *= 15;

        if (option === "declination" && (calculatedValue > 90 || calculatedValue < -90))
            return false;

        if (option === "right-ascension" && (calculatedValue > 360 || calculatedValue < 0))
            return false;

        $("#" + destId).val(calculatedValue);

        return true;
    }
});