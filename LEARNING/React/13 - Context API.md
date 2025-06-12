 - it will return provider and consumer
 - we can access one value from one jsx file to another jsx file
 - Context API allows data to be passed through a component tree without having to pass props manually at every level. This makes it easier to share data between components.
```
```jsx
import { createContext } from 'react';

export const MyContext = createContext("");


```jsx
import { useState, React } from "react";
import { MyContext } from "./MyContext";
import MyComponent from "./MyComponent";

function App() {
  const [text, setText] = useState("");

  return (
    <div>
      <MyContext.Provider value={{ text, setText }}>
        <MyComponent />
      </MyContext.Provider>
    </div>
  );
}

export default App;



```jsx
import { useContext } from 'react';
import { MyContext } from './MyContext';

function MyComponent() {
  const { text, setText } = useContext(MyContext);

  return (
    <div>
      <h1>{text}</h1>
      <button onClick={() => setText('Hello, world!')}>
        Click me
      </button>
    </div>
  );
}

export default MyComponent;
```

- we can use also global context api
``` 
we need to create global Context api provider then we need to complete it

- we need to put name and setName
- we can se the useState globaly in the value we need to put value ={{name, setName}}
- in the main.jsx we need to import into the AppContext into <React.StrictMode>
- inbetween the contextProvide we need to add the app props child
```