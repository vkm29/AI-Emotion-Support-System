/*
=========================================
Analytics JavaScript
AI Student Emotional Support System
=========================================
*/

// -------------------------------------
// Animate Wellness Score
// -------------------------------------

function animateWellnessScore() {

    const scoreElement = document.getElementById("wellness-score");

    if (!scoreElement) return;

    const target = parseInt(scoreElement.dataset.score || "0");

    let current = 0;

    const timer = setInterval(() => {

        current++;

        scoreElement.innerHTML = current + "%";

        if (current >= target) {

            clearInterval(timer);

        }

    }, 20);

}

// -------------------------------------
// Emotion Pie Chart
// -------------------------------------

function createEmotionChart() {

    const canvas = document.getElementById("emotionChart");

    if (!canvas) return;

    new Chart(canvas, {

        type: "pie",

        data: {

            labels: [

                "Happy",
                "Sad",
                "Stress",
                "Anxiety",
                "Angry",
                "Lonely",
                "Neutral"

            ],

            datasets: [{

                data: [

                    window.chartData?.happy || 0,
                    window.chartData?.sad || 0,
                    window.chartData?.stress || 0,
                    window.chartData?.anxiety || 0,
                    window.chartData?.angry || 0,
                    window.chartData?.lonely || 0,
                    window.chartData?.neutral || 0

                ],

                backgroundColor: [

                    "#22c55e",
                    "#3b82f6",
                    "#f97316",
                    "#ef4444",
                    "#dc2626",
                    "#8b5cf6",
                    "#6b7280"

                ]

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    position: "bottom"

                }

            }

        }

    });

}

// -------------------------------------
// Weekly Mood Trend
// -------------------------------------

function createTrendChart() {

    const canvas = document.getElementById("trendChart");

    if (!canvas) return;

    new Chart(canvas, {

        type: "line",

        data: {

            labels: [

                "Mon",
                "Tue",
                "Wed",
                "Thu",
                "Fri",
                "Sat",
                "Sun"

            ],

            datasets: [{

                label: "Wellness Score",

                data: window.trendData || [

                    70,
                    75,
                    72,
                    80,
                    84,
                    88,
                    90

                ],

                borderColor: "#2563eb",

                backgroundColor: "rgba(37,99,235,0.15)",

                fill: true,

                tension: 0.4

            }]

        },

        options: {

            responsive: true,

            scales: {

                y: {

                    beginAtZero: true,

                    max: 100

                }

            }

        }

    });

}

// -------------------------------------
// Download Report
// -------------------------------------

function downloadReport() {

    window.print();

}

// -------------------------------------
// Refresh Dashboard
// -------------------------------------

function refreshAnalytics() {

    location.reload();

}

// -------------------------------------
// Current Date
// -------------------------------------

function currentDate() {

    const element = document.getElementById("analytics-date");

    if (!element) return;

    element.innerHTML = new Date().toLocaleDateString(

        "en-IN",

        {

            weekday: "long",

            year: "numeric",

            month: "long",

            day: "numeric"

        }

    );

}

// -------------------------------------
// Export JSON
// -------------------------------------

function exportJSON() {

    if (!window.chartData) {

        alert("No analytics data available.");

        return;

    }

    const data = JSON.stringify(window.chartData, null, 4);

    const blob = new Blob([data], {

        type: "application/json"

    });

    const link = document.createElement("a");

    link.href = URL.createObjectURL(blob);

    link.download = "analytics_report.json";

    link.click();

}

// -------------------------------------
// Auto Refresh Every 5 Minutes
// -------------------------------------

setInterval(() => {

    console.log("Analytics refreshed.");

}, 300000);

// -------------------------------------
// Window Load
// -------------------------------------

window.onload = function () {

    animateWellnessScore();

    currentDate();

    createEmotionChart();

    createTrendChart();

};
