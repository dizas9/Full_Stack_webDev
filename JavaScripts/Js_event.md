# 3. JavaScript Events
<p>In JavaScript, events are actions or occurrences that can be detected and used to trigger specific behaviors in a web page. Events can be user-generated, like clicking a button or typing on a keyboard, or they can be triggered by other sources, such as the browser or external scripts. JavaScript provides a way to listen for and respond to these events.</p>
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