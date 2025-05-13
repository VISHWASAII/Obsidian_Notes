
## Basics
- `Variables` - Store data values (`let x = 5;`)
- `Data Types` - Types of values (number, string, boolean, etc.) (`typeof "hello"`)
- `Operators` - Perform operations (`+`, `-`, `*`, `/`, `%`, `**`)
- `Type Conversion` - Change data types (`String(123)`)
- `Template Literals` - String with embedded expressions (`` `Hello ${name}` ``)

## Functions
- `Function Declaration` - Named function (`function foo() {}`)
- `Function Expression` - Anonymous function assigned to variable (`const foo = function() {}`)
- `Arrow Functions` - Concise function syntax (`() => {}`)
- `Parameters/Arguments` - Function inputs/outputs (`function(a,b) {return a+b}`)
- `Callback Functions` - Function passed as argument (`arr.map(x => x*2)`)

## Objects
- `Object Literal` - Key-value pairs (`const obj = {key: 'value'}`)
- `Properties/Methods` - Object characteristics/actions (`obj.property`, `obj.method()`)
- `this Keyword` - Refers to owner object (`this.property`)
- `Constructor Functions` - Create object instances (`new Date()`)
- `Object Destructuring` - Unpack object properties (`const {prop} = obj`)

## Arrays
- `Array Methods` - Built-in array operations (`push`, `pop`, `map`, `filter`, `reduce`)
- `Array Destructuring` - Unpack array elements (`const [a,b] = arr`)
- `Spread Operator` - Expand array (`[...arr1, ...arr2]`)

## Control Flow
- `Conditionals` - Make decisions (`if`, `else if`, `else`)
- `Switch Statement` - Multi-case conditional (`switch(x) {case 1: ...}`)
- `Loops` - Repeat code (`for`, `while`, `do...while`)
- `Ternary Operator` - Short conditional (`x ? a : b`)

## Advanced Concepts
- `Closures` - Function with preserved outer scope (`function outer() {let x; function inner() {x++}}`)
- `Prototypes` - Object inheritance mechanism (`Array.prototype.newMethod = ...`)
- `Classes` - Blueprint for objects (`class X {constructor() {} method() {}}`)
- `Promises` - Handle async operations (`new Promise((resolve, reject) => ...)`)
- `Async/Await` - Write async code synchronously (`async function f() {await promise}`)
- `Modules` - Split code into files (`import x from 'module'`, `export default x`)

## DOM Manipulation
- `DOM Selection` - Get elements (`document.querySelector('#id')`)
- `DOM Events` - Handle user interactions (`element.addEventListener('click', handler)`)
- `DOM Modification` - Change page content (`element.innerHTML = 'new content'`)

## Error Handling
- `try/catch` - Handle errors (`try {...} catch(err) {...}`)
- `throw` - Create custom errors (`throw new Error('message')`)

## ES6+ Features
- `let/const` - Block-scoped variables (`let x = 1`, `const y = 2`)
- `Default Parameters` - Fallback parameter values (`function(x=1) {}`)
- `Rest Parameters` - Handle variable arguments (`function(...args) {}`)
- `Map/Set` - Special collections (`new Map()`, `new Set()`)
- `Symbols` - Unique identifiers (`const sym = Symbol()`)

## Browser APIs
- `Local Storage` - Store data locally (`localStorage.setItem('key', 'value')`)
- `Fetch API` - Make HTTP requests (`fetch(url).then(res => res.json())`)
- `Timers` - Delay code execution (`setTimeout(fn, 1000)`, `setInterval(fn, 1000)`)