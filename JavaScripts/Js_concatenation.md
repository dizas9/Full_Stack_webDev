# JavaScript concatenation

 Literally, __concatenation__ means ___A series of interconnected things___ or ___events___.
<br>

Concatenation refers to the ___process of combining___ or ___linking___ _two_ or more strings, sequences, or elements together to create a new string or sequence. In programming, concatenation is a common operation used to ___join___ strings together.

```javascript
const str1 = "Hello";
const str2 = "World";
const result = str1 + " " + str2; //Output : "Hello World"
```

## let`s see some 👽👽extraterrestrial👽👽 example : <br>

<span style="color : yellow">Guess the output </span><span style="font-size: 30px">🤯</span>

```javascript 
console.log("3" + "3")// output : 33
console.log(3 + 3)// output : 6
console.log("3" + "3" + "3")// output : 333
console.log("3" + "3" - "3")// output : ???
```
<details>
<summary>See Output</summary><br>

```
30
```
</details><br>

## How ??
 In JavaScript, when you perform arithmetic operations using the ' + ' , ' - ' , ' * ' , or  ' / ' operators, JavaScript will automatically try to convert the operands to numbers if they are not already numbers. <br>

 At ___first___ , in above expression addition(+) oparetors used with two string operand "3" and "3" , become "33"(Since both are string) , means JavaScript performs ___string concatenation___ instead of _numerical addition_ . ___Then___  the subtraction operator (-) is used between the concatenated string "33" and the string "3" . Here the interesting part, when JavaScript encounters an arithmetic operator like " - ", it tries to convert the operands to numbers ( "3" can be converted to the number 3) . JavaScript converts both "33" and "3" to numbers.






