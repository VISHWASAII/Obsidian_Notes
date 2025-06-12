- UseEffect is a hook in react that allows you to perform side effects in function components
- like direact update the DOM
- it has two argument -  callback and dependency array
- Only run on initial render not in re render
```
Interview example

The `useEffect` hook is used to run code in a React component **after it renders.  
This code can be for side effects like:

- Fetching data from an API
    
- Setting a timer
    
- Changing the page title
    
- Manually updating the DOM
```
A **side effect** is any action that affects **something outside** the component, or needs to happen **after rendering**.
### 💡 Think Like This:

1. React shows the screen first — maybe empty or loading.
    
2. Then we say: “Now go get the data from the server.”
    
3. That "go get the data" part is a **side effect**, so we put it in `useEffect`.

```
import {useEffect} from 'react'

// lets consider i have function
const value = () => {
   clg('print') 
}

value(); // it will call the function every time re-dering an application

// using the UseEffect we can restrict them
userEffect(()=>{
clg("hello")
}, []) 
// []it will say run only once


```
- we can pass the value also we needed like we can pass the button value also if we needed

**Fetch**
- Example we can use the fetch also instead of axios lets try using the use effect
```
// Used to fetch the data from the url

  const url = 'https://api.github.com/users';

  

  const FetchData = () => {

    const[users, setUsers] = useState([]);

  }

  useEffect(() => {

    const fetchData = async() =>{

     try{

      const response = await fetch(url)

      const users = await response.json();

      setUsers(users)

      console.log(users)

     }catch(error){

      console.log(error)

     }

    };

    fetchData();

   }, []);

  

  return (

    <div className="container">

    <ul className="">

      {users.map((user) => {

        console.log(user)

        const {id, login, avatar_url, html_url} = user;

        return

       })}

    </ul>

    </div>

  )

}
```

**UseEffect Cleanup**
- We will complete later