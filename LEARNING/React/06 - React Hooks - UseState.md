- First we need to create react environment using vite<span style="color:rgb(255, 0, 0)"> environment</span>

01 - Use State
```
if i click the button the count need to increase

function App() {

  

  let count = 0

  
  

const handleClick = () => {

  count = count + 1;

  console.log(count)

}

  

  return (

    <>

    <h2>{count}</h2>

    <button type="button" onClick={handleClick}>

      increase

    </button>

    </>

  )

}

  

export default App

if we do this the count is not visible inthe page so we need to re render it.

// for this we are going to use the React Hook
import {userstate} from react

it is array function which have [value, function]

  const[count, setCount] = useState()

// instead of the previous one we can use this

function App() {

  const[count, setCount] = useState(0)

  

  console.log(useState('hello'))

  
  

const handleClick = () => {

  setCount(count + 1)

}
```
- General rules of hooks 
- Comp must be in uppercase
- Hooks not working in the conditions
1.1 - Use state Array
```
// Printing the array value

function App() {

  const[people, setPeople] = React.useState(data)

  return (

    <div className="container">

    {people.map((people) => {

      const{id,name} = people;

      console.log(people)

      return <div key={id}>

        <h4>{name}</h4>

      </div>

     })}

    </div>

  )

}
```

- We are removing the item in the code using usestate
```
  

  const[people, setPeople] = React.useState(data)

  

  const removeItem = (id) => {

    console.log(id);

    const newPeople = people.filter((person) =>

    person.id !== id)

    setPeople(newPeople)

  }

  const clearAllItems = () => {

    setPeople([])

  }

  return (

    <div className="container">

    {people.map((people) => {

      const{id,name} = people;

      console.log(people)

      return <div key={id}>

        <h4>{name}</h4>

        <button type="button" onClick={

          () => removeItem(id)}>

          remove Item

        </button>

      </div>

     })}

     <button type="button" style={{margin: '2rem'}}

     onClick={clearAllItems}>clear Items</button>

    </div>

  )

}
```

1.3 - Use State Object
- React using auto-batching using that group state update a bunch of the values together
```
function App() {

// Instead of doing one by one we can pass the object also

const[Person , setPerson] = useState({
name:'vishwa',
age: 12
})
  const[name, setName] = useState('vishwa')

  const[age, setAge] = useState(21)

  const[degree, setDegree] = useState('M.tect')

  

  const changeBio = () => {

    setName('logesh')

    setAge(14)

    setDegree('B.tect')

//we can use this also
setPersion(...Person, name: 'susan')

  }

  return (

    <div className="container">

    <h1>{name}</h1>

    <h1>{age}</h1>

    <h1>{degree}</h1>

    <button type="button" onClick={

      changeBio

    }>Click to change</button>

    </div>

  )

}

  

export default App
```
- If we update the function is updated by one for that we can use the previous State for this
```
setState((prevState) => {
 return{...prevState, value:newValue}
})
```

1.3 SetTimeOut
- if we set the timing for 3 sec if we click how many times it wont change
```
unction App() {

  const[value, setValue] = useState(0);

  

  const changeBio = () => {

    setTimeout(() => {

      setValue(value + 1)

     }, 3000)

  }

  return (

    <div className="container">

    <h1>{value}</h1>

    <button type="button" onClick={

      changeBio

    }>Click to change</button>

    </div>

  )

}

  

export default App
```
- Where as in the case of this we are addning previous value with the currect value
```
like it will update the value increase by one


function App() {

  const[value, setValue] = useState(0);

  

  const changeBio = () => {

    setTimeout(() => {

      setValue((currentValue) => {

        return currentValue + 1;

      }

      )

     }, 3000)

  }

  return (

    <div className="container">

    <h1>{value}</h1>

    <button type="button" onClick={

      changeBio

    }>Click to change</button>

    </div>

  )

}
```
- Code to handle the login and the logout
```
import React, { useEffect, useState } from "react";

import { people } from "./data";

  

function App() {

  const[user, SetUser] = useState(null);

  

  const login = () => {

    SetUser({name: 'vishwa'})

   }

  

   const logout = () => {

    SetUser(null);

   }

  return(

    <div>

      {user? (<div>

        <h2>{user.name}</h2>

        <button type="button" onClick={() => { logout() }}>logout</button>

      </div>): (<div>

        <h2>User name is not found</h2>

        <button type="button" onClick={() => { login() }}>login</button>

        </div>)}

    </div>

  )

}
```

```js

setState((prevState) => {

  return { ...prevState, value: newValue };

});

```