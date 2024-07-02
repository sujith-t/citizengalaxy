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

    new Chart($('#clazz'), {
        type: 'bar',
        data: {
            labels: [1,2,3,4,5,6,7],
            datasets: [{
                label: "hello",
                data: [65, 59, 80, 81, 56, 55, 40],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(201, 203, 207, 0.2)'
                ],
                borderColor: [
                    'rgb(255, 99, 132)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 205, 86)',
                    'rgb(75, 192, 192)',
                    'rgb(54, 162, 235)',
                    'rgb(153, 102, 255)',
                    'rgb(201, 203, 207)'
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

        console.log(groupCounts);
        chart = new Chart($('#' + idValue), {
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

        return chart;
    }
});
