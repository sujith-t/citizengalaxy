/**
 * @author Sujith T
 * Deus et Scientia Erit Pactum Meum 2024
 **/
$(document).ready(function(){
    const ecliptic = ["Ec", "Ei", "Er"];
    const spirals = ["Sa", "Sb", "Sc", "Sd", "Se"];
    const barredSpirals = ["SBa", "SBb", "SBc", "SBd"];

    let classWiseCounts = $.ajax("/api/v1/catalog/class/counts", {async: false}).responseJSON;

    drawGroupSummaryPieChart(classWiseCounts, "groups");
    let barClassWiseChart = drawClassWiseBarChart(classWiseCounts, "clazz");
    barClassWiseChart.resize(600,600);

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
