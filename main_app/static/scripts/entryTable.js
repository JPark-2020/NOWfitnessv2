let table = document.getElementById("entryTable");
let tr = table.getElementsByTagName("tr");

function exerciseFunction() {
    let input = document.getElementById("exerciseQuery");
    let filter = input.value.toUpperCase();
  
    // Loop through all table rows, and hide those who don't match the search query
    // exercisename = td for exercise name 
    // workoutname = td for workoutname 
    for (i = 0; i < tr.length; i++) {
      let workoutName = tr[i].getElementsByTagName("td")[1];
      if (workoutName) {
        let txtValue = workoutName.textContent || workoutName.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }
  
function dateFunction() {
    let input = document.getElementById("dateQuery");
    let filter = input.value.toUpperCase();

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      let entryDate = tr[i].getElementsByTagName("td")[0];
      if (entryDate) {
        let txtValue = entryDate.textContent || entryDate.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
}

function setColor(setNumber){
  for(i = 0; i < setNumber.length; i++){
    if(setNumber[i].innerHTML == 'True'){
      setNumber[i].style.color = 'green';
      setNumber[i].innerHTML = '<i class="fas fa-check"></i>';
      setNumber[i].style.visibility = "visible";
    }
    else if(setNumber[i].innerHTML == 'False'){
      setNumber[i].style.color = 'red';
      setNumber[i].innerHTML = '<i class="fas fa-times"></i>'
      setNumber[i].style.visibility = "visible";
    }
  }
}

function countCompleteSets(entry){
  for(let i=0; i < entry.length; i++){
    
    let count = 0 
    let countFailure = 0 
    let entrySets = entry[i].getElementsByClassName("setcompletion");
    let setsComplete = entry[i].getElementsByTagName("td")[7]

    for(let j = 0; j < entrySets.length; j++){
      
      if(entrySets[j].innerHTML == '<i class="fas fa-check"></i>'){
          count++;
          setsComplete.innerHTML = count; 
      }
      else{
        countFailure--; 
        if(countFailure == -5){
          setsComplete.innerHTML = count; 
        }
      }
    }
  }
}

// unecessary

// function checkImprovement(entry){
//   let firstEntryImprovement = entry[1].getElementsByTagName("td")[8]
//   let workoutName = entry[i].getElementsByTagName("td")[1]
//   // firstEntryImprovement.innerHTML = 'none';

//   for(let i=2; i < entry.length; i++){
//     let baseEntry = entry[i].getElementsByTagName("td")[7];
//     let priorEntry = entry[i-1].getElementsByTagName("td")[7];
//     let improvement = entry[i].getElementsByTagName("td")[8];


//     if(baseEntry.innerHTML > priorEntry.innerHTML && priorEntry.innerHTML != 0){
//       percentage_improve = (baseEntry.innerHTML-priorEntry.innerHTML)/priorEntry.innerHTML;
//       improvement.innerHTML = percentage_improve * 100 + '%';
//     }

//     else if(priorEntry.innerHTML == 0){
//       percentage_improve = (baseEntry.innerHTML-priorEntry.innerHTML/1);
//       improvement.innerHTML = percentage_improve * 100 + '%';
//     }
//     else{
//       improvement.innerHTML = 'NO';
//     }
// }
// }
document.getElementById("getData").addEventListener("click", function(){
  let set1 = document.getElementsByClassName("setCompletion1");
  let set2 = document.getElementsByClassName("setCompletion2");
  let set3 = document.getElementsByClassName("setCompletion3");
  let set4 = document.getElementsByClassName("setCompletion4");
  let set5 = document.getElementsByClassName("setCompletion5");
  
  // let setsComplete = document.getElementsByClassName("sets-complete");
  // let setsIncomplete = document.getElementsByClassName("sets-incomplete");
  // let improvement = document.getElementsByClassName("improvement-check");

  setColor(set1);
  setColor(set2);
  setColor(set3);
  setColor(set4);
  setColor(set5);
  countCompleteSets(tr);
  checkImprovement(tr);
})

