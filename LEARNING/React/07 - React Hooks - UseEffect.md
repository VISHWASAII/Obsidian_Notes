- UseEffect is a hook in react that allows you to perform side effects in function components
- like direact update the DOM
- it has two argument -  callback and dependency array
- Only run on initial render not in re render
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