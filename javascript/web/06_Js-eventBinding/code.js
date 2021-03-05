//window.onload = function()
window.addEventListener("load", function()
{
  var btnPrint = document.getElementById("btn-print");

  var add = function(x, y)
  {
    return x + y;
  }

  btnPrint.onclick = function()
  {
    var x = prompt("x 값을 입력하세요", 0);
    var y = prompt("y 값을 입력하세요", 0);

    x = parseInt(x);
    y = parseInt(y);

    btnPrint.value = x + y;
  }
}); // 괄호 닫기 주의;;; 잘 열고 잘 닫혔는지 확인 필수.

// 다른 js file 과 function 이 겹쳐 나중에 읽히는 것만 실행되는 오류를 해결하기 위해
// window.addEventListener 를 사용한다. 진짜 소괄호 주의...