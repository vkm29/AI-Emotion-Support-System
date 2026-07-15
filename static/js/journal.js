/*
=========================================
Journal JavaScript
AI Student Emotional Support System
=========================================
*/

const journalBox = document.querySelector("textarea[name='journal']");
const emotionSelect = document.querySelector("select[name='emotion']");

// ------------------------------------
// Character Counter
// ------------------------------------

function updateCharacterCount(){

    const counter=document.getElementById("character-count");

    if(!counter || !journalBox) return;

    counter.innerHTML=journalBox.value.length;

}

// ------------------------------------
// Word Counter
// ------------------------------------

function updateWordCount(){

    const counter=document.getElementById("word-count");

    if(!counter || !journalBox) return;

    const words=journalBox.value.trim();

    if(words===""){

        counter.innerHTML=0;

        return;

    }

    counter.innerHTML=words.split(/\s+/).length;

}

// ------------------------------------
// Writing Progress
// ------------------------------------

function updateProgress(){

    const progress=document.getElementById("writing-progress");

    if(!progress || !journalBox) return;

    let percent=(journalBox.value.length/500)*100;

    if(percent>100){

        percent=100;

    }

    progress.style.width=percent+"%";

    progress.innerHTML=Math.floor(percent)+"%";

}

// ------------------------------------
// Auto Save Draft
// ------------------------------------

function saveDraft(){

    if(!journalBox) return;

    localStorage.setItem(

        "journalDraft",

        journalBox.value

    );

}

// ------------------------------------
// Load Draft
// ------------------------------------

function loadDraft(){

    if(!journalBox) return;

    const draft=localStorage.getItem(

        "journalDraft"

    );

    if(draft){

        journalBox.value=draft;

    }

}

// ------------------------------------
// Clear Draft
// ------------------------------------

function clearDraft(){

    localStorage.removeItem(

        "journalDraft"

    );

}

// ------------------------------------
// Current Date
// ------------------------------------

function currentDate(){

    const today=document.getElementById("today");

    if(!today) return;

    today.innerHTML=new Date().toLocaleDateString(

        "en-IN",

        {

            weekday:"long",

            day:"numeric",

            month:"long",

            year:"numeric"

        }

    );

}

// ------------------------------------
// Emotion Changed
// ------------------------------------

function emotionChanged(){

    if(!emotionSelect) return;

    const value=emotionSelect.value;

    const label=document.getElementById("selected-emotion");

    if(label){

        label.innerHTML=value.toUpperCase();

    }

}

// ------------------------------------
// Validation
// ------------------------------------

function validateJournal(){

    if(!journalBox) return false;

    if(journalBox.value.trim()===""){

        alert("Please write your journal.");

        return false;

    }

    if(journalBox.value.length<30){

        alert(

            "Please write at least 30 characters."

        );

        return false;

    }

    clearDraft();

    return true;

}

// ------------------------------------
// Writing Statistics
// ------------------------------------

function statistics(){

    updateCharacterCount();

    updateWordCount();

    updateProgress();

    saveDraft();

}

// ------------------------------------
// Event
// ------------------------------------

if(journalBox){

journalBox.addEventListener(

    "keyup",

    statistics

);

}

// ------------------------------------
// Window Load
// ------------------------------------

window.onload=function(){

    loadDraft();

    statistics();

    currentDate();

    emotionChanged();

}

// ------------------------------------
// Emotion Event
// ------------------------------------

if(emotionSelect){

emotionSelect.addEventListener(

    "change",

    emotionChanged

);

}