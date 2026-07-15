/*
==========================================
AI Student Emotional Support System
Chat JavaScript
==========================================
*/

const chatBox = document.getElementById("chat-box");
const messageInput = document.getElementById("message");

// --------------------------------------
// Add Message
// --------------------------------------

function addMessage(sender, message, type = "bot") {

    const wrapper = document.createElement("div");

    wrapper.className = "message " + type;

    const bubble = document.createElement("div");

    bubble.className = "bubble";

    let avatar = "";

    if (type === "user") {

        avatar = `
        <img
        src="/static/images/student.png"
        class="avatar">
        `;

    } else {

        avatar = `
        <img
        src="/static/images/bot.png"
        class="avatar">
        `;
    }

    bubble.innerHTML = `

        <strong>${sender}</strong>

        <br><br>

        ${message.replace(/\n/g,"<br>")}

        <div class="time">

            ${new Date().toLocaleTimeString()}

        </div>

    `;

    if(type==="user"){

        wrapper.innerHTML=`

        <div>

            ${bubble.outerHTML}

        </div>

        ${avatar}

        `;

    }

    else{

        wrapper.innerHTML=`

        ${avatar}

        <div>

            ${bubble.outerHTML}

        </div>

        `;

    }

    chatBox.appendChild(wrapper);

    chatBox.scrollTop = chatBox.scrollHeight;

}

// --------------------------------------
// Typing Indicator
// --------------------------------------

function showTyping(){

    let typing=document.createElement("div");

    typing.className="message bot";

    typing.id="typing";

    typing.innerHTML=`

    <img
    src="/static/images/bot.png"
    class="avatar">

    <div class="typing">

        <span></span>

        <span></span>

        <span></span>

    </div>

    `;

    chatBox.appendChild(typing);

    chatBox.scrollTop=chatBox.scrollHeight;

}

function hideTyping(){

    let typing=document.getElementById("typing");

    if(typing){

        typing.remove();

    }

}

// --------------------------------------
// Send Message
// --------------------------------------

async function sendMessage(){

    const message=messageInput.value.trim();

    if(message===""){

        return;

    }

    addMessage(

        "You",

        message,

        "user"

    );

    messageInput.value="";

    showTyping();

    try{

        const response=await fetch("/send_message",{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify({

                message:message

            })

        });

        const data=await response.json();

        hideTyping();

        if(data.success){

            addMessage(

                "AI Assistant",

                data.response,

                "bot"

            );

        }

        else{

            addMessage(

                "System",

                "Something went wrong.",

                "bot"

            );

        }

    }

    catch(error){

        hideTyping();

        addMessage(

            "System",

            "Network Error.",

            "bot"

        );

    }

}

// --------------------------------------
// Press Enter
// --------------------------------------

messageInput.addEventListener(

    "keypress",

    function(event){

        if(event.key==="Enter"){

            event.preventDefault();

            sendMessage();

        }

    }

);

// --------------------------------------
// Auto Welcome
// --------------------------------------

window.onload=function(){

    addMessage(

        "AI Assistant",

        "👋 Hello! Welcome to the AI Student Emotional Support System.\n\nI'm here to listen and support you.\n\nHow are you feeling today?",

        "bot"

    );

}

// --------------------------------------
// Dark Mode
// --------------------------------------

function toggleDarkMode(){

    document.body.classList.toggle(

        "dark-mode"

    );

}

// --------------------------------------
// Voice Input (Chrome)
// --------------------------------------

function startVoiceInput(){

    if(!('webkitSpeechRecognition' in window)){

        alert("Voice Recognition Not Supported");

        return;

    }

    const recognition=new webkitSpeechRecognition();

    recognition.lang="en-IN";

    recognition.start();

    recognition.onresult=function(event){

        messageInput.value=

        event.results[0][0].transcript;

    }

}

// --------------------------------------
// Clear Chat
// --------------------------------------

function clearChat(){

    chatBox.innerHTML="";

}