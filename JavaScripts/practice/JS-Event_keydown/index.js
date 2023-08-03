const inputText = document.getElementById('inputText');
const output = document.getElementById('output');

inputText.addEventListener('keydown', function(e){
  const keypressed = e.key;
  output.textContent = `${keypressed}`;
});