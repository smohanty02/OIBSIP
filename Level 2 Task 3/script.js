function addTask() {
  var taskInput = document.getElementById("taskInput");
  var taskList = document.getElementById("taskList");
  var taskText = taskInput.value.trim();

  if (taskText !== "") {
    var li = document.createElement("li");
    li.textContent = taskText;
    li.addEventListener("click", toggleTask);

    taskList.appendChild(li);
    taskInput.value = "";
  }
}

function toggleTask() {
  this.classList.toggle("completed");
}
