// masterTime
const clockDuration = 3.5; 
let time = clockDuration * 60; 

let clock = document.querySelector(".timer")
let exercise1 = document.querySelector(".exercise1")


const startRound = () => {
    const minutes = Math.floor(time/60);
    let seconds = (time % 60); 

    clock.innerHTML = `${minutes}:${seconds}`;
    time--;
}
const bodyExercises = (exercise, delay, nextExercise) => {

    setTimeout(()=>{
        exercise1.innerHTML = exercise;
        // exerciseTimer.innerHTML = `${minutes3}:${seconds3}`
        // CHECKS IF THERE IS A NEXT EXERCISE OTHERWISE IT WOULD PASS UNDEFINED 
        nextExercise && nextExercise();  
    }, delay)
}
// as progress adjust variables - pokesquare 
document.querySelector(".startTimer").addEventListener("click", ()=>{
    let id = setInterval(startRound,1000);
    setTimeout(() => {
        clearTimeout(id);
        clock.innerHTML = "WORKOUT DONE"
    }, 210000)
    bodyExercises('Dips', 1000, ()=>{
        bodyExercises('Pull-ups', 30000, () =>{
            bodyExercises('Push-ups', 30000, () =>{
                bodyExercises('Side Plank', 30000, () =>{
                    bodyExercises('Squat', 30000, () =>{
                        bodyExercises('Superman Plank', 30000, () =>{
                            bodyExercises('Walking Lunges', 30000) 
                        })
                    })
                })
            })
        })
    });
});