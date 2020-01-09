var a, b

function add (a, b) {
	return a + b;
};

function subtract (a, b) {
	return a - b;
};

function multiply (a, b) {
	return a * b;
};

function divide (a, b) {
  return a / b;
}

function operate (a, b, callback) {
  var answer = callback(a,b);
};

// document.getElementById("answer").textContent = answer;

var answer = document.getElementById("answer") ;    

function assign(clicked) {
  answer.innerHTML = clicked;
};