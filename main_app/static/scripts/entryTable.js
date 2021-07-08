function exerciseFunction() {
    let input = document.getElementById("exerciseQuery");
    let filter = input.value.toUpperCase();
    let table = document.getElementById("entryTable");
    let tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    // exercisename = td for exercise name 
    for (i = 0; i < tr.length; i++) {
      exerciseName = tr[i].getElementsByTagName("td")[1];
      if (exerciseName) {
        let txtValue = exerciseName.textContent || exerciseName.innerText;
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
      let table = document.getElementById("entryTable");
      let tr = table.getElementsByTagName("tr");
    
      // Loop through all table rows, and hide those who don't match the search query
      for (i = 0; i < tr.length; i++) {
        entryDate = tr[i].getElementsByTagName("td")[0];
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
  