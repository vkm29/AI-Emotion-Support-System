/*
=========================================
Admin Dashboard JavaScript
AI Student Emotional Support System
=========================================
*/

// =====================================
// Live Clock
// =====================================

function updateClock() {

    const now = new Date();

    const element = document.getElementById("admin-clock");

    if (element) {

        element.innerHTML = now.toLocaleString();

    }

}

setInterval(updateClock, 1000);

// =====================================
// Animated Counter
// =====================================

function animateCounter(id, target) {

    const element = document.getElementById(id);

    if (!element) return;

    let value = 0;

    const timer = setInterval(() => {

        value++;

        element.innerHTML = value;

        if (value >= target) {

            clearInterval(timer);

        }

    }, 20);

}

// =====================================
// Search Students
// =====================================

function searchStudents() {

    let input = document.getElementById("studentSearch");

    if (!input) return;

    let filter = input.value.toLowerCase();

    let table = document.getElementById("studentTable");

    if (!table) return;

    let rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {

        let row = rows[i];

        let text = row.innerText.toLowerCase();

        row.style.display = text.includes(filter)
            ? ""
            : "none";

    }

}

// =====================================
// Search Chats
// =====================================

function searchChats() {

    let input = document.getElementById("chatSearch");

    if (!input) return;

    let filter = input.value.toLowerCase();

    let cards = document.querySelectorAll(".chat-card");

    cards.forEach(card => {

        card.style.display =

            card.innerText.toLowerCase().includes(filter)

            ? "block"

            : "none";

    });

}

// =====================================
// Export Table CSV
// =====================================

function exportCSV(tableId, filename) {

    const table = document.getElementById(tableId);

    if (!table) {

        alert("Table not found.");

        return;

    }

    let csv = [];

    const rows = table.querySelectorAll("tr");

    rows.forEach(row => {

        const cols = row.querySelectorAll("td, th");

        let rowData = [];

        cols.forEach(col => {

            rowData.push('"' + col.innerText + '"');

        });

        csv.push(rowData.join(","));

    });

    const blob = new Blob(

        [csv.join("\n")],

        {

            type: "text/csv"

        }

    );

    const link = document.createElement("a");

    link.href = URL.createObjectURL(blob);

    link.download = filename;

    link.click();

}

// =====================================
// Delete Chat Confirmation
// =====================================

function deleteChat(chatId){

    if(confirm(

        "Delete this chat permanently?"

    )){

        window.location.href=

        "/delete_chat/"+chatId;

    }

}

// =====================================
// Delete User Confirmation
// =====================================

function deleteUser(userId){

    if(confirm(

        "Delete this student account?"

    )){

        window.location.href=

        "/delete_user/"+userId;

    }

}

// =====================================
// Risk Alert Popup
// =====================================

function showRiskAlert(message){

    const div=document.createElement("div");

    div.className=

    "alert alert-danger";

    div.style.position="fixed";

    div.style.top="20px";

    div.style.right="20px";

    div.style.zIndex="9999";

    div.style.minWidth="320px";

    div.innerHTML=

    "<strong>⚠ High Risk</strong><br>"+message;

    document.body.appendChild(div);

    setTimeout(()=>{

        div.remove();

    },5000);

}

// =====================================
// Dashboard Auto Refresh
// =====================================

function autoRefresh(){

    setInterval(()=>{

        console.log(

            "Refreshing Admin Dashboard..."

        );

    },300000);

}

// =====================================
// Theme Toggle
// =====================================

function toggleTheme(){

    document.body.classList.toggle("dark-mode");

    localStorage.setItem(

        "admin_theme",

        document.body.classList.contains("dark-mode")

    );

}

// =====================================
// Load Theme
// =====================================

function loadTheme(){

    if(

        localStorage.getItem(

            "admin_theme"

        )==="true"

    ){

        document.body.classList.add(

            "dark-mode"

        );

    }

}

// =====================================
// Notifications
// =====================================

function notify(message,type="success"){

    const alert=document.createElement("div");

    alert.className=

    "alert alert-"+type;

    alert.style.position="fixed";

    alert.style.bottom="20px";

    alert.style.right="20px";

    alert.style.zIndex="9999";

    alert.innerHTML=message;

    document.body.appendChild(alert);

    setTimeout(()=>{

        alert.remove();

    },3000);

}

// =====================================
// Logout
// =====================================

function logout(){

    if(confirm(

        "Are you sure you want to logout?"

    )){

        window.location="/logout";

    }

}

// =====================================
// Window Load
// =====================================

window.onload=function(){

    updateClock();

    loadTheme();

    autoRefresh();

    animateCounter("totalUsers",150);

    animateCounter("totalChats",1200);

    animateCounter("highRisk",4);

    animateCounter("activeToday",82);

}