/*
=========================================
Dashboard JavaScript
AI Student Emotional Support System
=========================================
*/

// -------------------------------
// Live Clock
// -------------------------------

function updateClock() {

    const now = new Date();

    const options = {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric"
    };

    const date = now.toLocaleDateString("en-IN", options);

    const time = now.toLocaleTimeString();

    const dateElement = document.getElementById("current-date");
    const timeElement = document.getElementById("current-time");

    if(dateElement)
        dateElement.innerHTML = date;

    if(timeElement)
        timeElement.innerHTML = time;

}

setInterval(updateClock,1000);

// -------------------------------
// Animated Counter
// -------------------------------

function animateCounter(id,target){

    let count=0;

    let speed=Math.ceil(target/100);

    const counter=document.getElementById(id);

    if(!counter)
        return;

    const timer=setInterval(()=>{

        count+=speed;

        if(count>=target){

            count=target;

            clearInterval(timer);

        }

        counter.innerHTML=count;

    },20);

}

// -------------------------------
// Progress Animation
// -------------------------------

function animateProgress(){

    document.querySelectorAll(".progress-bar").forEach(bar=>{

        const value=bar.getAttribute("data-value");

        bar.style.width="0%";

        setTimeout(()=>{

            bar.style.width=value+"%";

            bar.innerHTML=value+"%";

        },300);

    });

}

// -------------------------------
// Welcome Greeting
// -------------------------------

function greeting(){

    const hour=new Date().getHours();

    let text="";

    if(hour<12){

        text="🌞 Good Morning";

    }

    else if(hour<17){

        text="☀ Good Afternoon";

    }

    else{

        text="🌙 Good Evening";

    }

    const greeting=document.getElementById("greeting");

    if(greeting){

        greeting.innerHTML=text;

    }

}

// -------------------------------
// Notification Popup
// -------------------------------

function showNotification(message,type="success"){

    const notification=document.createElement("div");

    notification.className=`alert alert-${type}`;

    notification.style.position="fixed";

    notification.style.right="20px";

    notification.style.top="20px";

    notification.style.zIndex="9999";

    notification.style.minWidth="300px";

    notification.innerHTML=message;

    document.body.appendChild(notification);

    setTimeout(()=>{

        notification.remove();

    },4000);

}

// -------------------------------
// Mood Card Hover
// -------------------------------

document.querySelectorAll(".stats-card").forEach(card=>{

    card.addEventListener("mouseenter",()=>{

        card.style.transform="translateY(-8px)";

    });

    card.addEventListener("mouseleave",()=>{

        card.style.transform="translateY(0px)";

    });

});

// -------------------------------
// Dark Mode
// -------------------------------

function toggleDarkMode(){

    document.body.classList.toggle("dark-mode");

    localStorage.setItem(

        "darkMode",

        document.body.classList.contains("dark-mode")

    );

}

window.onload=function(){

    updateClock();

    greeting();

    animateProgress();

    animateCounter("chat-count",120);

    animateCounter("journal-count",40);

    animateCounter("emotion-count",65);

    animateCounter("wellness-score",92);

    if(localStorage.getItem("darkMode")=="true"){

        document.body.classList.add("dark-mode");

    }

}

// -------------------------------
// Refresh Dashboard
// -------------------------------

function refreshDashboard(){

    showNotification(

        "Dashboard Updated Successfully"

    );

}

// -------------------------------
// Logout Confirmation
// -------------------------------

function confirmLogout(){

    return confirm(

        "Are you sure you want to logout?"

    );

}