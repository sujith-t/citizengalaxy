/**
 * @author Sujith T
 * Deus et Scientia Erit Pactum Meum 2024
 **/
$(document).ready(function(){
    const ecliptic = ["Ec", "Ei", "Er"];
    const spirals = ["Sa", "Sb", "Sc", "Sd", "Se"];
    const barredSpirals = ["SBa", "SBb", "SBc", "SBd"];
    const featureSelectorName = ".feature-selection";
    const minusBtn = ".minus";
    let featureChart;

    //loading the static pie and the bar charts
    $.ajax("/api/v1/stats/class/counts", {
        async: true,
        success: function (data) {
            drawGroupSummaryPieChart(data, "groups");
            drawClassWiseBarChart(data, "clazz");
        }
    });


    $.ajax({
        type: "POST",
        url: "/api/v1/stats/class/values",
        data: {"class": "Er", "features": ["petror50_r"]},
        async: true,
        success: function (data) {
            let labels = [];
            for(let x=1; x < (data['total']) + 1; x++) {
                labels.push(x);
            }
            let dataArray = [{
                label: "petror50_r",
                data: data["petror50_r"],
                fill: false,
                tension: 0.1
            }];

            featureChart = drawDynamicLineChart("clazz-features", labels, dataArray);
        }
    });


    $(".class-data-points").click(function() {
        let payload = {};
        payload['class'] = $("#htf-class").val();
        payload['features'] = [];
        $(".feature-selection").each(function() {
            payload['features'].push($(this).val().toLowerCase());
        });

        let classData = $.ajax({
            type: "POST",
            url: "/api/v1/stats/class/values",
            data: payload,
            async: false
        }).responseJSON;

        let labels = [];
        for(let x=1; x < (classData['total']) + 1; x++) {
            labels.push(x);
        }

        let dataArray = [];
        for(let x in payload['features']) {
            let obj = {
                label: payload['features'][x],
                data: classData[payload['features'][x]],
                fill: false,
                tension: 0.1
            }
            dataArray.push(obj);
        }

        featureChart.data.labels = labels;
        featureChart.data.datasets = dataArray;
        featureChart.update();
    });

    $(".plus").click(handlePlusClick);

    $(minusBtn).click(handleMinusClick);

    function handleMinusClick() {
        let trNode = $(this).parent().parent();
        $(trNode).remove();
    }

    function handlePlusClick() {
        let numFeatures = $(featureSelectorName).length;
        if(numFeatures >= 5) {
            alert("Maximum 5 features can be analysed, can't add more");
            return;
        }

        let trNode = $(this).parent().parent();
        let newTr = $("<tr><td>&nbsp;</td></tr>");
        let newTd = $("<td></td>");
        let featureDropDown = $(featureSelectorName).get(0);
        $(newTd).append($(featureDropDown).clone());
        $(newTr).append(newTd);

        let minusImg = $(minusBtn).get(0);
        minusImg = $(minusImg).clone(true);
        newTd = $("<td></td>").append($(minusImg).show());
        $(newTr).append(newTd);
        $(trNode).parent().append($(newTr));
    }

    function drawDynamicLineChart(idValue, xAxis, dataArray) {
        return new Chart($('#' + idValue), {
            type: 'line',
            data: {
                labels: xAxis,
                datasets: dataArray
            },
            options: {
                plugins: {
                    title: {
                        display: true,
                        text: 'Data Distribution Per Galaxy Type'
                    }
                }
            }
        });
    }

    /**
     * @param counts
     * @param idValue
     * @returns {Chart}
     */
    function drawClassWiseBarChart(counts, idValue) {
        let labels = ecliptic;
        labels = labels.concat(spirals, barredSpirals, ["UN"]);
        let values = [];
        for(let x=0; x < labels.length; x++) {
            values.push(counts[labels[x]]);
        }
        labels[labels.length - 1] = "Unknown";

        return new Chart($('#' + idValue), {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: "",
                    data: values,
                    backgroundColor: [
                        'rgba(245,64,102, 0.2)',
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(198,109,127, 0.2)',
                        'rgba(234,128,24, 0.2)',
                        'rgba(255,154,56, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(211,162,114, 0.2)',
                        'rgba(163,138,115, 0.2)',
                        'rgba(4,87,87, 0.2)',
                        'rgba(8,172,172, 0.2)',
                        'rgba(8,143,234, 0.2)',
                        'rgba(3,85,140, 0.2)',
                        'rgba(147,196,228, 0.2)',
                        'rgba(174,10,174, 0.2)'
                    ],
                    borderColor: [
                        'rgb(245,64,102)',
                        'rgb(255, 99, 132)',
                        'rgb(198,109,127)',
                        'rgb(234,128,24)',
                        'rgb(255,154,56)',
                        'rgb(255, 205, 86)',
                        'rgb(211,162,114)',
                        'rgb(163,138,115)',
                        'rgb(4,87,87)',
                        'rgb(8,172,172)',
                        'rgb(8,143,234)',
                        'rgb(3,85,140)',
                        'rgb(147,196,228)',
                        'rgb(174,10,174)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                plugins: {
                    title: {
                        display: true,
                        text: 'Galaxy Types Distribution'
                    }
                }
            }
        });
    }

    /**
     * @param counts
     * @param idValue
     * @returns {Chart}
     */
    function drawGroupSummaryPieChart(counts, idValue) {
        let groupCounts = [0,0,0,0];
        for(g in ecliptic) {
            groupCounts[0] += counts[ecliptic[g]];
        }
        for(g in spirals) {
            groupCounts[1] += counts[spirals[g]];
        }
        for(g in barredSpirals) {
            groupCounts[2] += counts[barredSpirals[g]];
        }
        groupCounts[3] = counts["UN"];

        return new Chart($('#' + idValue), {
            type: 'pie',
            data: {
                labels: ['Ecliptic', 'Spiral','Barred Spiral', "Unknown"],
                datasets: [{
                    data: groupCounts,
                    //backgroundColor: ["Yellow", "Blue", "Green"]
                }]
            },
            options: {
                plugins: {
                    title: {
                        display: true,
                        text: 'Galaxy Types Distribution'
                    }
                }
            }
        });
    }
});
