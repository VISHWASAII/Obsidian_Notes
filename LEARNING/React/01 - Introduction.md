- The basic way to create a react environment we are going to use thuis command 
```
npx create-react-app myapp

npm start
```
- Boilerplate
- remove src folder
- create src folder
-  create index.js inside src
- toggle sidebar CMD + B
- shortcuts settings/keyboard shortcuts

01 - **Root**
- This is the root we need to inject our code into the browser [Entry point]
```
import React from 'react';
import ReactDOM from 'react-dom/client';

function Greeting() {
  return <h2>My First Component</h2>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(<Greeting />);
```

02 - **JSX Rule**
```
1 - Syntax Rules
always want to return a single element

<div className = 'someName'>
   <h2>
   <h2>
<div>
It is consider as a single element or parent element [single parent element]

we can use the Fragment instead of Fragement or Section in react 
<>
  //Opening and closing of the element
<>

2 - Naming Conversion

camelCase
```

03 - **Intendation**
```
if the tags are below the return then it will be like this

return {
<h2> hello <h2>
}
function Greeting() {
  return <h2>My First Component</h2>;
}
```

04 - **Nested Component**
```
return {
   <Greeting/>
   <welcome/>
}
```

05 - **We need to put our img in public**
```
if we put image in public then directly we can use it

```

06  - **JSX Rules for css**
```
const Author = () => (
  <h4 style={{ color: '#617d98', fontSize: '0.75rem', marginTop: '0.5rem' }}>
    Jordan Moore
  </h4>
);
```

07 - **Seperate css**
```
const Author = () => {
  const inlineHeadingStyles = {
    color: '#617d98',
    fontSize: '0.75rem',
    marginTop: '0.5rem',
  };
  return <h4 style={inlineHeadingStyles}>Jordan Moore </h4>;
};
```

08 - **Using the constants values inside**
```
const author = 'Jordan Moore';
const Book = () => {
  const title = 'Interesting Facts For Curious Mindssssss';
  return (
    <article className='book'>
      <img
        src='./images/book-1.jpg'
        alt='Interesting Facts For Curious Minds'
      />
      <h2>{title}</h2>

      <h4>{author.toUpperCase()} </h4>
      {/* <p>{let x = 6}</p> */}
      <p>{6 + 6}</p> //only pass expression for this
    </article>
  );
};
```
