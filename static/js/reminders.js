function addRem() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("myInput").value;
  var t = document.createTextNode(inputValue)
  li.appendChild(t);
  if (inputValue === '') {
    alert("You must write something!");
  } else {
    document.getElementById("reminder-list").appendChild(li);
  }
  document.getElementById("myInput").value = "";
}

var myNodelist = document.getElementsByClassName("reminder-item");
console.log(myNodelist);
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("button");
  span.type = "submit";
  var form = document.createElement("form");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  form.action = "/deleterem"
  form.method = "POST"
  form.style = "display:inline;"
  var input = document.createElement("input");
  input.type="hidden"
  input.name="node"
  input.value=myNodelist[i].innerHTML
  console.log(input.value)
  form.appendChild(span)
  form.appendChild(input)
  myNodelist[i].appendChild(form);
}

var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";

  }
}
