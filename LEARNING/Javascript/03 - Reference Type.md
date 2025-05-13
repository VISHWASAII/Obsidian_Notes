- Types Objects, Arrays, Functions
- What is the diff btw the ref and pre
- if we copy to other it will copy the reference not the value but value which copies the actual value

#Objects

```
// Define an object

const person = { name: "John", age: 30, city: "New York" };

  

// 1. Object.keys()

console.log("Keys:", Object.keys(person));

  

// 2. Object.values()

console.log("Values:", Object.values(person));

  

// 3. Object.entries()

console.log("Entries:", Object.entries(person));

  

// 4. Object.assign()

const newPerson = Object.assign({}, person, { country: "USA" });

console.log("New Person:", newPerson);

  

// 5. Object.freeze()

Object.freeze(person);

person.age = 35; // No effect

console.log("After freeze:", person);

  

// 6. Object.seal()

const sealedPerson = { name: "Alice", age: 25 };

Object.seal(sealedPerson);

sealedPerson.age = 26; // Allowed

// sealedPerson.city = "Los Angeles"; // Not allowed

console.log("After seal:", sealedPerson);

  

// 7. Object.getOwnPropertyNames()

console.log("Property Names:", Object.getOwnPropertyNames(person));

  

// 8. Object.getPrototypeOf()

console.log("Prototype:", Object.getPrototypeOf(person));

  

// 9. Object.setPrototypeOf()

const animal = { type: "mammal" };

const dog = { breed: "Labrador" };

Object.setPrototypeOf(dog, animal);

console.log("Dog Type:", dog.type);

  

// 10. Object.hasOwn()

console.log("Has 'name':", Object.hasOwn(person, "name"));

console.log("Has 'gender':", Object.hasOwn(person, "gender"));
```

#Array

```
// Define an array
const numbers = [1, 2, 3, 4, 5];

// 1. Array.isArray()
console.log("Is Array:", Array.isArray(numbers));

// 2. Array.push()
numbers.push(6);
console.log("After push:", numbers);

// 3. Array.pop()
numbers.pop();
console.log("After pop:", numbers);

// 4. Array.shift()
numbers.shift();
console.log("After shift:", numbers);

// 5. Array.unshift()
numbers.unshift(0);
console.log("After unshift:", numbers);

// 6. Array.concat()
const moreNumbers = [6, 7, 8];
const combined = numbers.concat(moreNumbers);
console.log("After concat:", combined);

// 7. Array.join()
console.log("Join:", numbers.join(" - "));

// 8. Array.slice()
console.log("Slice:", numbers.slice(1, 3));

// 9. Array.splice()
numbers.splice(2, 1, 9);
console.log("After splice:", numbers);

// 10. Array.indexOf()
console.log("Index of 4:", numbers.indexOf(4));

// 11. Array.includes()
console.log("Includes 3:", numbers.includes(3));

// 12. Array.find()
console.log("Find > 3:", numbers.find(num => num > 3));

// 13. Array.findIndex()
console.log("Find Index > 3:", numbers.findIndex(num => num > 3));

// 14. Array.filter()
console.log("Filter > 2:", numbers.filter(num => num > 2));

// 15. Array.map()
console.log("Map * 2:", numbers.map(num => num * 2));

// 16. Array.reduce()
console.log("Reduce Sum:", numbers.reduce((acc, num) => acc + num, 0));

// 17. Array.some()
console.log("Some > 4:", numbers.some(num => num > 4));

// 18. Array.every()
console.log("Every > 0:", numbers.every(num => num > 0));

// 19. Array.reverse()
numbers.reverse();
console.log("After reverse:", numbers);

// 20. Array.sort()
numbers.sort((a, b) => a - b);
console.log("After sort:", numbers);

```

