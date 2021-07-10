const roundDuration = 3; 
let time = roundDuration * 60; 

let clock = document.querySelector(".timer")

let punchOne = document.querySelector(".punch1")
let punchTwo = document.querySelector(".punch2")
let punchThree = document.querySelector(".punch3")
let punchFour = document.querySelector(".punch4")
let punches = ['Jab', 'Cross', 'Lead hook', 'Rear hook', 'Lead uppercut', 'Rear uppercut']


let startButton = document.querySelector(".startTimer")

function punchRandomizer(){
  return Math.floor(Math.random()*punches.length)
} 

function startTimer(){
  const minutes = Math.floor(time/60);
  let seconds = time % 60; 
  clock.innerHTML = `${minutes}:${seconds}`;
  time--; 
}

function startRound(){
  punchOne.innerHTML = punches[punchRandomizer()]; 
  punchTwo.innerHTML = punches[punchRandomizer()]; 
  punchThree.innerHTML = punches[punchRandomizer()]; 
  punchFour.innerHTML = punches[punchRandomizer()];
}

document.querySelector(".startTimer").addEventListener("click", ()=>{
  let timerId = setInterval(startTimer,1000);
    setTimeout(()=>{
      clearTimeout(timerId);
      clock.innerHTML = "ROUND COMPLETE"
    }, 180000)  
  
  let id = setInterval(startRound,6000);
    setTimeout(() => {
        clearTimeout(id);
    }, 180000)
})

