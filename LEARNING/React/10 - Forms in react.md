- This is common for the forms in the react and all other input using this we can pass the data
```
import React, { useEffect, useState } from "react";

import users from "./data";

  

function App() {

  const [name, setName] = useState('');

  const [user, setUser] = useState(users);

  

  const handleSubmit = (e) => {

    e.preventDefault();

    if(!name) return;

    const newUser = {username: name, password : "vishwa"}

    const updatedUsers = [...user,newUser ]

    console.log(updatedUsers)

    setUser(updatedUsers)

    setName('');

  }

  const removeUsers = (userName) => {

    const updatedUser = user.filter((person) => person.username !== userName);

    setUser(updatedUser)

  }

  

  return (

   <div>

      <form onSubmit={handleSubmit}>

      <label>Enter your name:

        <input

          type="text"

          value={name}

          onChange={(e) => setName(e.target.value)}

        />

      </label>

      <button type="submit">Submit</button>

    </form>

    <h2>users</h2>

    {user.map((user) => {

      return (

        <div key={user.username}>

          <h2>{user.username}</h2>

          <button onClick={() => removeUsers(user.username)}>Remove item</button>

        </div>

      )

     })}

   </div>

  );

}

  

//Multiple user inputs need to learn

  

export default App
```

- Must need to use the Formdata api
- Likewise we can use it
```
  const handleSubmit = (e) => {

    e.preventDefault();

    const formData = new FormData(e.currentTarget)

    const email = formData.get('name')

    console.log(email)

    console.log(first)

    if(!name) return;

    const newUser = {username: name, password : "vishwa"}

    const updatedUsers = [...user,newUser ]

    console.log(updatedUsers)

    setUser(updatedUsers)

    setName('');

  }
```
- We can use the object of it also
```
const newUser = Object.fromEntries(formData);
```