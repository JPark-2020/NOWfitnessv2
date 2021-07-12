// masterTime
const clockDuration = 5; 
let time = clockDuration * 60; 


let clock = document.querySelector(".timer")
let exercise1 = document.querySelector(".exercise1")

const startRound = () => {
    const minutes = Math.floor(time/60);
    let seconds = time % 60; 

    clock.innerHTML = `${minutes}:${seconds}`;
    time--;
}
const yogaExercises = (exercise, delay, nextExercise) => {

    setTimeout(()=>{
        exercise1.innerHTML = exercise;
        // exerciseTimer.innerHTML = `${minutes3}:${seconds3}`
        // CHECKS IF THERE IS A NEXT EXERCISE OTHERWISE IT WOULD PASS UNDEFINED 
        nextExercise && nextExercise();  
    }, delay)
}

document.querySelector(".startTimer").addEventListener("click", ()=>{
    let id = setInterval(startRound,1000);
    setTimeout(() => {
        clearTimeout(id);
        clock.innerHTML = "ROUND DONE"
    }, 300000)
    yogaExercises('Bridge Pose', 1000, ()=>{
        yogaExercises('Childs Pose', 30000, () =>{
            yogaExercises('Cobra Pose', 30000, () =>{
                yogaExercises('Downward-Facing Dog', 30000, () =>{
                    yogaExercises('Four-Limbed Staff Pose', 30000, () =>{
                        yogaExercises('Plank', 30000, () =>{
                            yogaExercises('Tree Pose', 30000, () =>{
                                yogaExercises('Triangle Pose', 30000)
                            })
                        })
                    })
                })
            })
        })
    })
})