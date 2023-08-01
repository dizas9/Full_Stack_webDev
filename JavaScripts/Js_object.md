# 1. JavaScript Objects
<p> JavaScript objects are one of the fundamental data types in JavaScript, and they play a crucial role in representing and organizing data. You have already learned that JavaScript variables are containers for data values. Objects are variables too. But objects can contain many values <a href="https://www.w3schools.com/js/js_objects.asp">w3schools.</a></p><br>

### Example of Variable 
``` javascript
//this is variable example where variable 'name' contains single values 

let name = "sazid";

```
### Example of  objects
``` javascript
//this is javascript object example where object 'info' contains multiple value values 

const info = {name : "sazid" , id : "A02147" , phone_no : "012xxxxxxx"};

// Important note : name and value separated by a colon

// here values (eg. name) also called property , you can access property by object.
// for example:

document.write(info.name); //or

document.write(info.phone_no);

```

### Another way to accessing object properties 

```javascript
info["id"]
```
<p> Space and line breaks are not important. But it is good practice for Butifying your code & increase readability</p>
<br>

```javascript
const info = {name : "sazid",
              id : "A02147",
              phone_no : "012xxxxxxx"
              };
```
**Note :-** _See Practice folder for actual code Preview_
<br>
<br>

## Object Methods
<p>Objects can have methods. Methods are <b>actions</b> that can be performed on objects. <a href="https://www.codecademy.com/resources/docs/javascript/objects">Learn more.</a> </p>
<p>Simply, A method is a function stored as a property. For example: </p>

```HTML
<body>
    <h3>Method as Property</h3>
    <p id="demo"></p>

    <script>
        const Name = {
            firstname : "Sazidul",
            lastname : "Islam",
            fullname : function(){                          
                return this.firstname + " " + this.lastname;
            }
            //Here 'fullname' hold function() value that will be return when function called.
        }
        document.getElementById("demo").innerHTML =Name.fullname();

           // when 'Name.fullname()' invoke the corresponding function will run. 
    </script>
</body>
```
<p>In this example, the 'Name' object has a 'fullname' method, where a function stored as the value of the 'fullname' property. By calling 'person.greet()', we can execute the code inside the method and produce the output like following :-</P>

```
Sazidul Islam
```
<p>Another Example , </p>

```HTML
<body>
    <h3>Method as property</h3>
    <p id="demo"></p>

    <script>
        const Name = {
            firstname: "Sazidul",
            lastname: "Islam",
            nikename: "Sazid",
            fullname: function () {
                return `My name is ${this.firstname} ${this.lastname}. You Can call me ${this.nikename}. `
            }
            //Here 'fullname' hold function() value that will be return when function called.
        }
        document.getElementById("demo").innerHTML = Name.fullname();

           // when 'Name.fullname()' invoke the corresponding function will run. 
    </script>
</body>

```
<p>Output: </p>

```
My name is Sazidul Islam. You Can call me Sazid
```

<br>

### what is _this_?

<p><i> <b> this </b> </i> keyword refers to an object. Remember its just a keyword not variable. You cannot change value of <i> <b> this </b> </i>. </P>
<p>In the context of JavaScript, the this keyword refers to the current execution context, which can vary depending on how and where it is used.</P> 
for example:  
<br>
<br>

<table align = "center">
  <tr>
    <th colspan="2"  style="text-align: center"><h3>The meaning of<b><i> 'this' </i></b> keyword in different situaton </h3> </th>
  </tr>
  <tr>
    <th style="text-align: center">Used</th>
    <th style="text-align: center">What is mean</th>
  </tr>
  <tr>
    <td>In an object method</td>
    <td>'this' refers to the object.</td>
  </tr>

  <tr>
    <td>Alone</td>
    <td>'this' refers to the global object..</td>
  </tr>
  
  <tr>
    <td>In a function</td>
    <td>'this' refers to the global object..</td>
  </tr>

   <tr>
    <td>In an event</td>
    <td>'this'  refers to the element that received the event.</td>
  </tr>
 <tr>
    <td>Methods like call(), apply(), and bind()</td>
    <td>'this'  to any object.</td>
  </tr>

</table>
<br>
<br>
learn more about <a href="https://www.w3schools.com/js/js_this.asp">'this'</a> <br>

___Note___ : See use of this  in coding section.

<p> We give 'In an object method' earlier. </p>

### when used  __this__ alone
```HTML
<body>
    <p id="demo"></p>

    <script>
        function sayHello() {
            document.write("Hello," + this.name);
            //here, 'name' property of the object (eg. person1, person2), referenced by 'this'.
        }

        // object 1
        const person1 = {
            name: "sazid",
            greet: sayHello
        }

        // object 2
        const person2 = {
            name: "dizas",
            greet: sayHello
        }

        // Standalone function invocation
        document.getElementById('demo').innerHTML = sayHello();
         // Output: Hello, undefined (or Hello, [window object] in a browser)
    </script>
</body>

```

<p>Output:</p>

```
undefined
Hello,

```
<p> when  we invoke sayHello(), [as standalone function] the value of 'this' is 'undefined' as there is no specific object to bind 'this'.  </p>

<p>But if we invoke this function with object : </p>

```HTML
<body>
    <p id="demo"></p>

    <script>
        function sayHello() {
            document.write("Hello," + this.name);
        }

        // object 1
        const person1 = {
            name: "sazid",
            greet: sayHello
        }

        // object 2
        const person2 = {
            name: "dizas",
            greet: sayHello
        }

        // Method invocation
        person1.greet(); // Output: Hello, sazid
        person2.greet(); // Output: Hello, dizas
    </script>
</body>

```
<p>Output:</p>

```
Hello, sazid Hello, dizas
```
<p>When greet() is invoked as a method of 'person1' and 'person2', the 'this' keyword inside sayHello refers to the respective objects (person1 and person2), allowing us to access the name property (sazid, dizas) of each object.</p>
<p>Here, another example:</p>

```javascript
function addition(){
  return (this.a + this.b);
}

let  num = {
  a :12,
  b :8,
  sum : addition
}

num.sum();
```
<p>Output:</p>

```
20
```
### when used  __this__ in function
<p>If we call 'this' within a function, its refer again to the general window object, and we'll get this in our console: [object Window]. </p>

```javascript
function demo(){
  console.log("this is this function", this);
}

demo();
```
<p>Output</p>

```
this is this function[object Window]
```
<p>In JavaScript, the window object represents the global window in a browser environment.  It is the top-level object in the browser's Document Object Model (DOM) hierarchy. . It serves as the global scope for JavaScript code running in a web page. Here is an example : </p>

```javascript
var x = 20;

window.x + 20; // Output : 40
```
### Arrow function

<p>Arrow function consise syntax for defining function. Its help for shorter way to function expression.</p>

#### Example 1: Arrow function without parameters

```javascript
const name = () => {
  console.log("hello");
}

name(); //Output : hello
```
___Note___ : - here '( )' contains parameters.

#### Example 2: Arrow function with a single parameter

```javascript
const math = (num) => {
  return num+10;
}

console.log(math(5)); // output : 15
```

<p>Another Example : </p>

```javascript
const info = (name) =>  {
  document.write("My name is ",name + "." );
}

info('sazid'); //Output : My name is sazid.
```
####  Example 3: Arrow function with multiple parameters and implicit return

```javascript
const add = (a,b) => a+b;

add(5,3); //Output : 8
```
```javascript
const name = (name , age) => {

document.write(`my name is ${name} an i am ${age}`);
}
name('sazid' , '22')
```
#### Description of code:

<p></p>
<p></p>

```javascript

```


