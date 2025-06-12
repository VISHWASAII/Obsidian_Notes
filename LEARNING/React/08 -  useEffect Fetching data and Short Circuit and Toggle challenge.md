- We are resting dom until it gets for single time
- If we put the useEffect in the circuit function then will render each time according the useState property

### 📦 Real-Life Examples — Where You Can Use `useEffect`

| Scenario                                   | What It Means in Real Life                                                                                     |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| ✅ **Get data from the internet**           | Imagine you open a page and it _automatically loads_ your profile — that’s `useEffect`.                        |
| ✅ **Listen when screen size changes**      | You want to show a mobile layout if the screen becomes small — `useEffect` listens for resize.                 |
| ✅ **Start a timer**                        | Like a countdown in an exam app — `useEffect` can start that when the page loads.                              |
| ✅ **Clean up mess**                        | When you leave a room, you turn off the lights. Similarly, `useEffect` can clean things when the page changes. |
| ✅ **When something changes, do something** | Like: “If the user types something, and it changes, check if the name is already taken.”                       |
| ✅ **Change the title of the tab**          | Like making the browser tab say “1 New Message” — you can update it using `useEffect`.                         |
| ✅ **Save to local storage**                | If someone types their name, you can store it in the browser for next time.                                    |
| ✅ **Detect online/offline**                | If the internet goes off, `useEffect` can help you show “You’re offline”.                                      |
```
import React, { useEffect, useState } from "react";

import { people } from "./data";

  

function App() {

  

  const [isLoading, setIsLoading] = useState(true);

  
// Use effect for holding false value
  useEffect(() => {

    setTimeout(() => {

      setIsLoading(false)

     }, 3000);

   }, []);

  

  if(isLoading){

    return <h2>Loading...</h2>

  }

  return <h2>Multiple Return Basics</h2>

}

  
  

export default App
```
- The data fetching is in 3 Stage
- Loading - waiting for data arrive
- error - there was an error
- success - received data
```
// This is how we are fetching the data from the url using the useState and useEffect

import React, { useEffect, useState } from "react";

import { people } from "./data";

  

function App() {

  const url = 'https://api.github.com/users/QuincyLarson';

  const[isLoading,setIsloading] = useState(true)

  const [user, setUser] = useState(null);

  const[isError, setIsError] = useState(false)

  

  useEffect(() => {

    const fetchUser = async () => {

      try {

        const response = await fetch(url)

        const user = await response.json()

        setUser(user)

      } catch (error) {

        setIsError(true)

      }

      setIsloading(false)

    }

    fetchUser();

   }, []);

  

   if(isLoading){

    return <h2>Loding...</h2>

   }

   if(isError){

    return <h2>There is an error</h2>

   }

   return <div>

    <img style={{width: '150px', borderRadius: '25px' }}

    src={user.avatar_url}/>

    <h2>{user.name}</h2>

    <p>{user.bio}</p>

   </div>

}

  
  

export default App
```
- Here order is matter below that like after fetching the data only we can able to destructure it 


**Short Circuit**:

- 0, Null, undefined, NaN, " ".
- Create two state Values
- one -- Falsy and second -- truthy
-  Those circuits are the truthy value
- {user || 'default Value'} -- it show first value if it is true else it will show the second value
- {user && 'defaultValue' } -- it need to be both true value not false, null, Nan, or zero
```
//We can use the ternary operator for this like

<button>
     {user ? (<div>
        hello user user.name
     <div/>) :  <div>
         hello user name thats it
     <div/>}

<button/>
```


 