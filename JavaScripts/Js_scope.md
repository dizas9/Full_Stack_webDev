# JavaScript Scope

<p>JavaScript scope refers to the accessibility and visibility of variables, functions, and objects in a particular part of your code during runtimen . there are 3 types of scope : </p>
<ol>
<li>Block Scope</li>
<li>Function Scope</li>
<li>Global Scope</li>
</ol>

### Block Scope 
<p>Before ES6 (2015), JavaScript had only 'Global Scope' and 'Function Scope' . ES6 introduced two important new JavaScript keywords: 'let' and 'const'.These two keywords provide' Block Scope' in JavaScript. For Example: </p>

```javascript
{let x =2;} // let

document.write(x); // Output : Uncaught ReferenceError: x is not defined
```

```javascript
{const x =2;} // const

document.write(x); // Output : Uncaught ReferenceError: x is not defined
```
<p>With 'var' keyword :</p>

```javascript
{var x =2;} // let

document.write(x); // Output : 2
```
<p>Variables declared with the 'var' keyword not have block scope.</p>



### Local Scope
<p>Variables declared within a JavaScript function, become LOCAL to the function.</p>

 ```javascript
function demo (){
  let x = 20;
   return x;
  // can use 'x' here
}

document.write(demo()); //return 'x' here 
document.write(x); //cannot use 'x here'2
```
<p>Local Scope only be accessed from within the function.</p>

### Function Scope
### Global Scope
<p>A variable declared outside a function, becomes GLOBAL.</p>

```javascript
let str = "dizas";

function demo () {
  return `this access 'str' inside function --> ${str}`;
}

document.write(demo() + "<br>");
document.write("this access 'str' outside function -->",str);
```
<p>Output : </p>

```
this access 'str' inside function --> dizas
this access 'str' outside function -->dizas
```
<p>So , All scripts and functions on a web page can access Global Scope . </p>

### Automatically  Global Scope
<p>In JavaScript, variables declared without any explicit keyword (such as 'var', 'let', or 'const') are automatically assigned global scope. These variables become part of the global object ( 'window' object in browsers or 'global' object in Node.js ) and can be accessed from anywhere in the code.</p>

```javascript
function demo() {
  car = 'BMW';
  document.write(car);
}

demo();
document.write("<br>");

document.write(car);
```
<p>Output :</p>

```
BMW
BMW
```
___Note___ :- In "Strict Mode", undeclared variables are not automatically global.

```javascript
'use strict'
function demo() {
  car = 'BMW';
  document.write(car);
}

demo();
document.write("<br>");

document.write(car);
```



<p></p>


```javascript

```
