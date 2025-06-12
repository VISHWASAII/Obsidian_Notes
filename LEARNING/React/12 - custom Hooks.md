- like wise we can use our own custom hook using that we can build the application
```
app.js
import React from "react";

import useToggle from "./useToggle"; // Correct import path

  

function App() {

  const { show, toggle } = useToggle(true); // Passing true as the default state

  

  return (

    <div>

      <button onClick={toggle}>Click</button>

      {show && <h4>Some Stuff</h4>}  {/* Shows 'Some Stuff' when show is true */}

    </div>

  );

}

  

export default App;


useToggle.jsx
import { useState } from "react";

  

const useToggle = (defaultValue) => {

  const [show, setShow] = useState(defaultValue); // Default state is passed here

  

  const toggle = () => {

    setShow((prev) => !prev); // This ensures the state toggles properly

  };

  

  return { show, toggle };

};

  

export default useToggle;

```
- similarly we can use this for fetching the data