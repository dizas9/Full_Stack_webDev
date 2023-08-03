const inputText = document.getElementById("inputText");
const output = document.getElementById("output");
// variable to store pressed key as array
const pressKeys = [];

inputText.addEventListener("keydown", function (e) {
  const keypressed = e.key;
  pressKeys.push(keypressed); // built in JS method used to add elemnt at the end of an array
  output.textContent = `${keypressed}`;
});
//'keydown' event doesnot fire for 'tab' key

//A function to Show pressed key
function ShowPressKeys() {
  const keyString = pressKeys.join("");
  window.alert(`You Pressed : ${keyString}`);
}

//function for reset button

function ResetField(){
  inputText.value = '';
  pressKeys.length = 0;
  output.textContent ='';
}
