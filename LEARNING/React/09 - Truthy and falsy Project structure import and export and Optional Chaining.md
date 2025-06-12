```
Example

import { useState , useEffect} from 'react';

export default function App() {
    const[Toggle, setToggle] = useState(false);
    return(
        <div>
            <button type="button" onClick={() => setToggle(!Toggle)}> Click to view</button>
            {Toggle || <div>Working fine</div>}
                {Toggle && <div>Working fine</div>}
        </div>
    );
}

```
## 🔹 1. **Truthy & Falsy Values**

| Concept    | Meaning                                            | Example                                        | Result                     |
| ---------- | -------------------------------------------------- | ---------------------------------------------- | -------------------------- |
| **Truthy** | Any value that **acts like `true`** in conditions  | `'hello'`, `123`, `{}`, `[]`                   | All are treated as `true`  |
| **Falsy**  | Any value that **acts like `false`** in conditions | `''`, `0`, `null`, `undefined`, `false`, `NaN` | All are treated as `false` |


## 🔹 2. **Short-Circuit Evaluation**

|Operator|Rule|Example|Result|
|---|---|---|---|
|`||` (OR)|Returns **first truthy** value|
|`&&` (AND)|Returns **first falsy** value|`'' && 'hello'`|`''`|

## 🔹 4. **React: `!` (NOT) Operator**

| Use      | Meaning           | Example                           | Result                                                |
| -------- | ----------------- | --------------------------------- | ----------------------------------------------------- |
| `!value` | Negates the value | `!true` → `false`, `!''` → `true` | Used to show something only if the value is **falsy** |

|Expression|Meaning|React Output (Example)|Why It Works This Way?|
|---|---|---|---|
|`{text||'hello world'}`|If `text` is falsy, show `'hello world'`|
|`{text && 'hello world'}`|If `text` is truthy, show `'hello world'`|Nothing (because `text = ''` is falsy)|`&&` returns the **second** value only if the first is **truthy**|
|`{name||'hello world'}`|If `name` is truthy, show it; else fallback|
|`{name && 'hello world'}`|If `name` is truthy, show `'hello world'`|`hello world` (because `name = 'susan'` is truthy)|First value is truthy, so `&&` returns the second|
|`{!text}`|`true` if `text` is falsy|`true` (because `text = ''`)|`!` negates — empty string is falsy, so `!''` becomes `true`|
|`{!name}`|`false` if `name` is truthy|`false` (because `name = 'susan'`)|`!name` negates the truthy value|
|`{user && <SomeComponent />}`|If `user` is truthy, render component|`<SomeComponent />` rendered|If user exists, show the component|
|`{isEditing ? 'edit' : 'add'}`|If true, show edit, else add|`add` (because `isEditing = false`)|Ternary operator used for **simple inline if-else** logic|
|`{user ? <h4>Hello</h4> : <h2>Login</h2>}`|Show one or the other based on `user`|`<h4>Hello</h4>` (because `user` is truthy)|Great for conditional blocks of JSX|


```
After creating component we need to import like

import Navbar from './tutorial/name'

in the navbar we need to put export default App;
```
- instead of creating the seperate export as default we need to create index.js file in that we can export it.
```
index.js

//Like this we can use it
export {default} from './Navbar'
```

- Named Export 
```
index.jsx

import Home from "./Home"
import About from "./About"

export {Home, About}

int app.jsx
import {Home, About} from './tutorial'

```
- Export Group
```
index.jsx

import FristComp from './first'
import SecondComp from './second'

const Example = () => {
return ( 
   <FristComp/>
   <SecondComp/>
)
}

in the app.jsx
import example from tutorial 

we can use it
```
- To import the data from the js file for importing using glean extension
```
listen dinamically checking the value

const data  = {
  name:vishwa,
  age: 12
  image: url
},
{
  name: mitai,
  age: 14,
}

we need to check where image is present or not

const values = {name, age, image}

const img = image && image[0] && image[0].small


or we can use the chaining property

const imgs = image?.[0]?.smaill?.url || avatar;

//if not present then we need to add the default image
```



