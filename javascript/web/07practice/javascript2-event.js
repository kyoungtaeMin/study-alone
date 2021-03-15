// EX 5 : Implementing trigger
window.addEventListener("load", function(){

  var section = document.querySelector("#section5");

  var fileButton = section.querySelector(".file-button");
  var fileTrigger = section.querySelector(".file-trigger");

  fileTrigger.onclick = function(){
    var event = new MouseEvent("click", {
      "view": window,
      "bubbles":true,
      "cancelable":true
    });

    fileButton.dispatchEvent(event);
  }
});

// EX 4-2 : Blocking the element's basic behavior
window.addEventListener("load", function(){
  
  var section = document.querySelector("#section4-2");
  var tbody = section.querySelector(".notice-list tbody");

  tbody.onclick = function(e){

    e.preventDefault();
    // 현재 click이라는 enent가 발생하는데 preeventDefault는 event가
    // 누구에게 발생하든 그것을 타고오는 bubbling 과정에서 일어나고 있는
    // 어떠한 녀석도 기본행위를 갖지 않게 한다.

    var target = e.target;

    if(target.nodeName != "A"){
      // A tag는 기본적으로 페이지를 다시 요청해 새로운 페이지를 받기 때문에
      // 함수를 호출하더라도 새로운 페이지를 부르기 때문에 바로 리셋된다.
      return;
    }
    if(target.classList.contains("sel-button")){
      // target 이 가진 classList 중에 "sel-button이 있니?"
      var tr = target.parentElement;
      for(; tr.nodeName != "TR"; tr = tr.parentElement);

      tr.style.background = "yellow"
    }
    else if(target.classList.contains("edit-button")){

    }
    else if(target.classList.contains("del-button")){

    }
  }

});

// EX 4-1 : Handling events of buttons with different functions
window.addEventListener("load", function(){
  
  var section = document.querySelector("#section4-1");
  var tbody = section.querySelector(".notice-list tbody");

  tbody.onclick = function(e){
    var target = e.target;

    if(target.nodeName != "INPUT"){
      return;
    }
    if(target.classList.contains("sel-button")){
      // target 이 가진 classList 중에 "sel-button이 있니?"
      var tr = target.parentElement;
      for(; tr.nodeName != "TR"; tr = tr.parentElement);

      tr.style.background = "yellow"
    }
    else if(target.classList.contains("edit-button")){

    }
    else if(target.classList.contains("del-button")){

    }
  }

});

//EX 3 : Stop enent bubbling
window.addEventListener("load", function(){

  var section = document.querySelector("#section3");

  var imgList = section.querySelector(".img-list");
  var addButton = section.querySelector(".add-button");
  var currentImg = section.querySelector(".current-img");

  imgList.onclick = function(e){
    if(e.target.nodeName != "IMG"){
      return;
    }
    currentImg.src = e.target.src;
  }
  addButton.onclick = function(e){
    e.stopPropagation();
    var img = document.createElement("img");
    img.src = "../images/김연아2.jpg";
    currentImg.insertAdjacentElement("afterend", img);
  }
  // add-button은 image-list의 자식Element이기 때문에
  // event가 일어 났을 경우에 부모 Element인 img-list까지 실행이 된다.
  // 이때 사용하는 것이 e.propagation이다.

});

//EX 2 : Handling user events using bubbling
window.addEventListener("load", function(){

  var section = document.querySelector("#section2");

  var imgList = section.querySelector(".img-list");
  //var imgs = section.querySelectorAll(".img");
  var currentImg = section.querySelector(".current-img");

  imgList.onclick = function(e){

    if(e.target.nodeName != "IMG"){
      return;
    }
    currentImg.src = e.target.src;
  }

});

//Practice Problem 1  : Remove selected recode
window.addEventListener("load", function(){

  var section = document.querySelector("#section1-1");

  var delButtons = section.querySelectorAll(".del-button");

  for(var i=0; i<delButtons.length; i++){
    delButtons[i].onclick = function(e){
      var tr = e.target.parentElement.parentElement;
      tr.remove();
    }
  }
});

//EX 1 : Show selected image : Event target
window.addEventListener("load", function(){

  var section = document.querySelector("#section1");

  var imgs = section.querySelectorAll(".img");
  var currentImg = section.querySelector(".current-img");

  // imgs[0].onclick = function(e) {
  //   currentImg.src = e.target.src;
  // }
  // imgs[1].onclick = function(e) {
  //   currentImg.src = e.target.src;
  // }
  // imgs[2].onclick = function(e) {
  //   currentImg.src = e.target.src;
  // }
  // 반복문으로 돌려버리자.
  for(var i=0; i<imgs.length; i++){
    imgs[i].onclick = function(e) {
      currentImg.src = e.target.src;
    }
  }
});