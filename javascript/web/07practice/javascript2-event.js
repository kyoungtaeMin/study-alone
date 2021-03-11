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