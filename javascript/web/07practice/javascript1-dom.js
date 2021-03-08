// EX5 : Changing Attributes of Element Nodes
window.addEventListener("load", function() {
  var section5 = document.querySelector("#section5");
  var srcInput = section5.querySelector(".src-input");
  var imgSelect = section5.querySelector(".img-select");
  var changeBtn = section5.querySelector(".change-btn");
  var img = section5.querySelector(".img");

  changeBtn.onclick = function() {
    img.src = "../images/"+srcInput.value;
    //img.src = "../images/"+imgSelect.value;
  }

});

// EX4 : Selection Using Child Nodes
window.addEventListener("load", function() {
  var section4 = document.querySelector("#section4");
  var box = section4.querySelector(".box");

  var input1 = box.children[0];  // childNodes는 tag들 사이의 공백까지 자식으로 친다....
  var input2 = box.children[1];  // children은 tag들만 자식으로 친다

  input1.value = "Hello";
  input2.value = "Okey";

});

// EX3 : Selectors API Level1
window.addEventListener("load", function() {
  var section3 = document.getElementById("section3");
  var txtX = section3.querySelector("input[name='x']");
  var txtY = section3.querySelector(".txt-y");
  var btnAdd = section3.querySelector(".btn-add");
  var txtSum = section3.querySelector(".txt-sum");

  btnAdd.onclick = function () {
    var x = parseInt(txtX.value);
    var y = parseInt(txtY.value);
    
    txtSum.value = x + y;
  };
});

// EX2 : Improving Element Selection
window.addEventListener("load", function() {
  var section2 = document.getElementById("section2");
  var txtX = section2.getElementsByClassName("txt-x")[0];
  var txtY = section2.getElementsByClassName("txt-y")[0];
  var btnAdd = section2.getElementsByClassName("btn-add")[0];
  var txtSum = section2.getElementsByClassName("txt-sum")[0];

  /*
  var inputs = document.getElementsByTagName("input");


  var txtX = inputs[0];
  var txtY = inputs[1];
  var btnAdd = inputs[2];
  var txtSum = inputs[3];
  */

  btnAdd.onclick = function () {
    var x = parseInt(txtX.value);
    var y = parseInt(txtY.value);
    
    txtSum.value = x + y;
  };
});

// EX1 : Calculator Program
window.addEventListener("load", function() {
  var txtX = document.getElementById("txt-x");
  var txtY = document.getElementById("txt-y");
  var btnAdd = document.getElementById("btn-add");
  var txtSum = document.getElementById("txt-sum");

  btnAdd.onclick = function () {
    var x = parseInt(txtX.value);
    var y = parseInt(txtY.value);
    
    txtSum.value = x + y;
  };
});