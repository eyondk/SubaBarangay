document.addEventListener("DOMContentLoaded", function () {
    // Sanitary Chart
    const sanitaryCanvas = document.getElementById('sanitaryChart');
    if (sanitaryCanvas) {
        const sanitaryCtx = sanitaryCanvas.getContext('2d');
        new Chart(sanitaryCtx, {
            type: 'pie',
            data: {
                labels: [
                    'Pour/Flush type with septic tank', 
                    'Pour/Flush toilet connected to septic tank AND to sewerage system', 
                    'Ventilated Pit (VIP) Latrine'
                ],
                datasets: [{
                    data: [40, 35, 25], // Example Data
                    backgroundColor: [
                        'rgba(2, 2, 87, 0.8)', 
                        'rgba(54, 162, 235, 0.8)', 
                        'rgba(75, 192, 192, 0.8)'
                    ]
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'left',
                        labels: {
                            usePointStyle: true,
                            padding: 10,
                            maxWidth: 150  // Adjust legend width
                        }
                    },
                    datalabels: {
                        formatter: function (value, ctx) {
                            let total = ctx.dataset.data.reduce((acc, val) => acc + val, 0);
                            let percentage = ((value / total) * 100).toFixed(2);
                            return percentage + '%';  // Show percentage
                        },
                        color: 'white',  // Text color of the percentage
                        font: {
                            weight: 'bold',
                            size: 14
                        }
                    }
                }
            }
        });
    } else {
        console.error("Sanitary Chart canvas element not found!");
    }

    // Unsanitary Chart
    const unsanitaryCanvas = document.getElementById('unsanitaryChart');
    if (unsanitaryCanvas) {
        const unsanitaryCtx = unsanitaryCanvas.getContext('2d');
        new Chart(unsanitaryCtx, {
            type: 'pie',
            data: {
                labels: [
                    'Water-sealed toilet without septic tank', 
                    'Overhung latrine', 
                    'Open Pit latrine', 
                    'Without Toilet'
                ],
                datasets: [{
                    data: [30, 20, 25, 25], // Example Data
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.8)', 
                        'rgba(255, 159, 64, 0.8)', 
                        'rgba(255, 205, 86, 0.8)', 
                        'rgba(153, 102, 255, 0.8)'
                    ]
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'left',
                        labels: {
                            usePointStyle: true,
                            padding: 10,
                            maxWidth: 150  // Adjust legend width
                        }
                    },
                    datalabels: {
                        formatter: function (value, ctx) {
                            let total = ctx.dataset.data.reduce((acc, val) => acc + val, 0);
                            let percentage = ((value / total) * 100).toFixed(2);
                            return percentage + '%';  // Show percentage
                        },
                        color: 'white',  // Text color of the percentage
                        font: {
                            weight: 'bold',
                            size: 14
                        }
                    }
                }
            }
        });
    } else {
        console.error("Unsanitary Chart canvas element not found!");
    }
});
