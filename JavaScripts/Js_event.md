# 3. JavaScript Events
<p>In JavaScript, events are actions or occurrences that can be detected and used to trigger specific behaviors in a web page. Events can be user-generated, like clicking a button or typing on a keyboard, or they can be triggered by other sources, such as the browser or external scripts. JavaScript provides a way to listen for and respond to these events.</p>

### __Some key concept of JavaScript Event__ :

1. __Event Listener:__ An event listener is ___a function___ that 'listens for' a _specific event_ to occur and triggers a response when the event occurs. Event listeners are ___used to bind events to HTML elements___ and define what ___should happen___ when the event is triggered.
2. __Event Handler:__ An event handler is the ___function___ that gets executed when the event occurs. It is ___the code that responds to the event___.
3. __Event Object:__ When an event occurs, JavaScript creates an event object that ___contains information about the event___. The event object holds details like the ___type of event___,    ___the element that triggered the event___  , and   ___any additional event-related data___.

```javascript
const button = document.getElementById('myButton');

// The "handleClick()" function is the event handler in this code. 
function handleClick(event) { // Event object (parameter) . Here 'event' is "Event Object"
  console.log('Button clicked!');
}

// Attach the event handler to the button's "click" event
button.addEventListener('click', handleClick); // Here "addEventListener()" method is used to create an event listener.

```
4.__Event Types:__ There are various types of events in JavaScript, such as mouse events (click, mouseover, mouseout), keyboard events (keyup, keydown), form events (submit, input, change), and more.
   
   
<p><b>addEventListener:</b> This is a method available on DOM elements, such as the button element. It is used to register an 'event handler function' to be executed when a specific event is triggered on the element.</p>



```html
<body>
    <button id="mybutton">Click Me</button>

    <script>
        const button = document.getElementById('mybutton');

        button.addEventListener('click', function () {
            console.log('button clicked');
        });
    </script>
</body>
```
### 'event' Type
<p> 'event type' or 'event name' for which the event listener is being added. Such as 'click' , 'mouseenter' , 'keydown'</p>

#### 'keydown' example
```html

<body>
    <input type="text" id="textInput" placeholder="Press any key....">
    <p id="output"></p>

    <script>
        const textInput = document.getElementById('textInput');
        const output = document.getElementById('output');

        textInput.addEventListener('keydown', function (event) {
            const keypressed = event.key;

            output.textContent = `you pressed : ${keypressed}`;
        });
    </script>
</body>
```
<p></p>

```javascript

```