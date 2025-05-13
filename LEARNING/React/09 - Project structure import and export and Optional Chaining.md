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