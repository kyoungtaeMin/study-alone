//EX11 : Sorting records by column clicked 1
window.addEventListener("load", function() {
  
  var notices = [
    {"id" : 1, "title" : "Javascript란...", "regDate" : "2021-03-09", "writerId" : "min", "hit" : 2},
    {"id" : 2, "title" : "Python만 배우면 될줄 알았는데...ㅜㅜ", "regDate" : "2021-03-08", "writerId" : "yoen", "hit" : 7},
    {"id" : 3, "title" : "기본기가 튼튼해야되", "regDate" : "2021-03-07", "writerId" : "moon", "hit" : 11},
    {"id" : 4, "title" : "근데 너무 어려운거 아니냐", "regDate" : "2021-03-06", "writerId" : "joo", "hit" : 35}
  ];

  var section11 = document.querySelector("#section11");

  var noticeList = section11.querySelector(".notice-list");
  var titleId = section11.querySelector(".title");
  var tbodyNode = noticeList.querySelector("tbody");

  var bindData = function() {
    var template = section11.querySelector("template");
    
    for(var i=0; i<notices.length; i++){

    var cloneNode = document.importNode(template.content, true);
    var tds = cloneNode.querySelectorAll("td");
    tds[0].textContent = notices[i].id;

    //tds[1].innerHTML = '<a href="'+ notices[0].id +'">'+ notices[0].title+"</a>";
    
    var aNode = tds[1].children[0];
    aNode.href = notices[i].id;
    aNode.textContent = notices[i].title;

    tds[2].textContent = notices[i].regDate;
    tds[3].textContent = notices[i].writerId;
    tds[4].textContent = notices[i].hit;

    tbodyNode.append(cloneNode);
    }
  }

  bindData();

  var titleSorted = false;

  titleId.onclick = function() {
    
    tbodyNode.innerHTML = "";

    if(titleSorted)
      notices.sort(function(a, b){
        titleSorted = true;
        
        if (a.title < b.title)
          return -1;
        else if (a.title > b.title)
          return 1;
        else
          return 0;

    });
    else
      notices.reverse();

    bindData();

  }
});

//EX10 : Multiple element selection and batch deletion
window.addEventListener("load", function() {

  var section10 = document.querySelector("#section10");

  var noticeList = section10.querySelector(".notice-list");
  var tbody = noticeList.querySelector("tbody");
  var allCheckBox = section10.querySelector(".overall");
  var delBtn = section10.querySelector(".del-btn");
  var swapBtn = section10.querySelector(".swap-btn");

  allCheckBox.onchange = function() {

    var inputs = tbodyNode.querySelectorAll("input[type='checkbox']");

    for(var i=0; i<inputs.length; i++) {
      inputs[i].checked = allCheckBox.checked;
    }
  }

  delBtn.onclick = function() {
    var inputs = tbodyNode.querySelectorAll("input[type='checkbox']:checked");
    //console.log(inputs.length);
    
    for(var i=0; i<inputs.length; i++ ) {
      inputs[i].parentElement.parentElement.remove();
    }
  }

  swapBtn.onclick = function() {

  var inputs = tbodyNode.querySelectorAll("input[type='checkbox']:checked");

  if(inputs.length != 2) {
    alert("두 개만 선택해야 합니다.");
    return;
  }
  var trs = [];
  for(var i=0; i<inputs.length; i++) {
    trs.push(inputs[i].parentElement.parentElement);

  }
  var cloneNode = trs[0].cloneNode(true);
  trs[1].replaceWith(cloneNode);
  trs[0].replaceWith(trs[1]);
  
  }


});

//EX9 : Node insertion and node traversal
window.addEventListener("load", function() {

  var section9 = document.querySelector("#section9");

  var noticeList = section9.querySelector(".notice-list");
  var tbodyNode = noticeList.querySelector("tbody");
  var upBtn = section9.querySelector(".up-btn");
  var downBtn = section9.querySelector(".down-btn");

  var currentNode = tbodyNode.firstElementChild;
  
  downBtn.onclick = function() {
    
    var nextNode = currentNode.nextElementSibling;
    
    if(nextNode == null) {
      alert("더 이상 이동할 수 없습니다.");
      return;
    }
    //tbodyNode.removeChild(nextNode); //없어도 된다
    //tbodyNode.insertBefore(nextNode, currentNode);
    currentNode.insertAdjacentElement("beforeBegin", nextNode)
    // 테이블 행 이동은 이거 하나로 끝난다...
  }
  
  upBtn.onclick = function() {
    
    var prevNode = currentNode.previousElementSibling;

    if(prevNode == null) {
      alert("더 이상 이동할 수 없습니다.")
      return;
    }
    //tbodyNode.removeChild(currentNode); // 너도 없어도 됬구나
    //tbodyNode.insertBefore(currentNode, prevNode);
    // insert에는 Before 밖게 없다...ㅜㅜ 그래서 삭제되는 Node를 조정해줘야 한다.
    currentNode.insertAdjacentElement("afterend", prevNode);
  }
});

//EX8 : Node cloning and Template tagging
window.addEventListener("load", function() {
  var notices = [
    {id : 5, title : "빅데이터 재밌니?", regDate : "2021-03-05", writerId : "min", hit : 54},
    {id : 6, title : "개발자는 어떠냐?", regDate : "2021-03-04", writerId : "min", hit : 22}
  ];
  var section8 = document.querySelector("#section8");

  var noticeList = section8.querySelector(".notice-list");
  var tbodyNode = noticeList.querySelector("tbody");
  var cloneBtn = section8.querySelector(".clone-btn");
  var templateBtn = section8.querySelector(".template-btn");

  cloneBtn.onclick = function() {
    var trNode = noticeList.querySelector("tbody tr");
    var cloneNode = trNode.cloneNode(true);

    var tds = cloneNode.querySelectorAll("td");
    tds[0].textContent = notices[0].id;
    tds[1].innerHTML = '<a href="'+ notices[0].id +'">'+ notices[0].title+"</a>";
    tds[2].textContent = notices[0].regDate;
    tds[3].textContent = notices[0].writerId;
    tds[4].textContent = notices[0].hit;

    trNode.append(cloneNode);
  }

  templateBtn.onclick = function() {
    var template = section8.querySelector("template");
    var cloneNode = document.importNode(template.content, true);

    var tds = cloneNode.querySelectorAll("td");
    tds[0].textContent = notices[0].id;

    tds[1].innerHTML = '<a href="'+ notices[0].id +'">'+ notices[0].title+"</a>";
    var aNode = tds[1].children[0];
    aNode.href = notices[0].id;
    aNode.textContent = notices[0].title;

    tds[2].textContent = notices[0].regDate;
    tds[3].textContent = notices[0].writerId;
    tds[4].textContent = notices[0].hit;

    tbodyNode.append(cloneNode);
  }
});

// EX7 : Append Element Nodes
window.addEventListener("load", function() {
  var section7 = document.querySelector("#section7");

  var titleInput = section7.querySelector(".title-input");
  var menuListUl = section7.querySelector(".menu-list");
  var addBtn = section7.querySelector(".add-btn");
  var delBtn = section7.querySelector(".del-btn");

  addBtn.onclick = function() {
    var title = titleInput.value;

    var html = '<a href="">' + title + "</a>";
    var li = document.createElement("li");
    li.innerHTML = html;

    //menuListUl.appendChild(li);
    menuListUl.append(li);

    //menuListUl.innerHTML += '<li><a href="">' + title + "</a></li>";
    // 위의 코드를 +를 사용하여 누적형으로 만들면 코드 짜기는 편하지만 계속해서 더 큰 문자열을
    // node로 만들기 때문에 성능상 문제가 생길 수 있다. 귀찮지만 아래 처럼 해야 할 때도 있다

    // var title = titleInput.value;
    // var textNode = document.createTextNode(title);

    // var aNode = document.createElement("a");
    // aNode.href="";
    // aNode.appendChild(textNode);

    // var liNode = document.createElement("li");
    // liNode.appendChild(aNode);

    // menuListUl.appendChild(liNode);

    
    // var title = titleInput.value;
    // var textNode = document.createTextNode(title);
    // menuListDiv.appendChild(textNode);
  }

  delBtn.onclick = function() {
    //var textNode = menuListUl.childNodes[0]; // 얘는 모든 Node들을 대상으로
    var liNode = menuListUl.children[0]; // 얘는 Element Node만을 선별해서 골라준다
    //menuListUl.removeChild(liNode);
    liNode.remove();
  }

});

// EX6 : Nodes Manipulation : Add Menu(createNode, Element)
window.addEventListener("load", function() {
  var section6 = document.querySelector("#section6");

  var titleInput = section6.querySelector(".title-input");
  var menuListDiv = section6.querySelector(".menu-list");
  var addBtn = section6.querySelector(".add-btn");
  var delBtn = section6.querySelector(".del-btn");

  addBtn.onclick = function() {
    var title = titleInput.value;
    var textNode = document.createTextNode(title);
    menuListDiv.appendChild(textNode);
  }

  delBtn.onclick = function() {
    var textNode = menuListDiv.childNodes[0];
    menuListDiv.removeChild(textNode);
  }

});

// EX5 : Changing Attributes of Element Nodes And Attributes of Css
window.addEventListener("load", function() {
  var section5 = document.querySelector("#section5");
  var srcInput = section5.querySelector(".src-input");
  var imgSelect = section5.querySelector(".img-select");
  var changeBtn = section5.querySelector(".change-btn");
  var img = section5.querySelector(".img");
  var colorInput = section5.querySelector(".color-input");

  changeBtn.onclick = function() {
    img.src = "../images/"+srcInput.value;
    //img.src = "../images/"+imgSelect.value;

    //img.style["border-color"] = colorInput.value; // key 값으로 만들어 이용할 수 있다
    img.style.borderColor = colorInput.value; // dash는 구분자로 사용하지 못하기 때문에 dash다음에 오는 문자를 대문자로 만들어서 사용할 수 있다.
    console.log(img.className);
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