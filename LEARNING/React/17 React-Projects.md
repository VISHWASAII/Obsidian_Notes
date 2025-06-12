- UseState Project
```
import data from "./data";

import { useState } from "react";

  

const App = () => {

  const[user, SetUser] = useState(data);

  

  const removeAllData = () => {

    SetUser('');

  }

  

  const removeOneUser = (id) => {

    const deleteSpecificUser = user.filter((userObj) => userObj.id !== id);

    SetUser(deleteSpecificUser);

  };

  return (

    <div>

      {

        user.map((users) => {

          return(

            <div key={users.id}>

            <img src={users.image} style={{width: '40px', height: '40px'}}></img>

            <h2>{users.age}</h2>

            <h2>{users.name}</h2>

            <button type="button" onClick={() => removeOneUser(users.id)}>Delete this user</button>

          </div>

          )

         })

      }

      <button type="button" onClick={removeAllData}>Delete ALl Users</button>

    </div>

  )

  

};

export default App;
```

- UseEffect project
```
- In this code we are passing the props using props drilling
- and hierarchy the section, article, div and main
- how use effect handling the loading and data fetching

Tour.jsx

import React from 'react'

  

function Tour({id, name, image, info, price, removeTours}) {

  console.log(image)

  return (

   <article key={id}>

    <img src={image} style={{width: '20px'}}></img>

    <span>{price}</span>

    <h3>{name}</h3>

    <h3>{info}</h3>

    <button type='button' onClick={() => removeTours(id)}>Click button</button>

   </article>

  )

}

  

export default Tour


Tours.jsx

import Tour from './Tour'

//Here we are using the Section

const Tours = ({tours, removeTours}) => {

  console.log(tours)

  return <section>

    <div>

      <h2>Tours</h2>

    </div>

    <div>

      {tours.map((tour) => {

        return <Tour key={tour.id} {...tour} removeTours={removeTours}/>

       })}

    </div>

  </section>

}

  

export default Tours

App.jsx

import { useState, useEffect } from "react";

import Loading from "./Loading";

import Tours from "./Tours";

  

const url = 'https://www.course-api.com/react-tours-project';

  

const App = () => {

  const [loading, setLoading] = useState(true);

  const [tours, setTours] = useState([]);

  

  const fetchData = async () => {

    setLoading(true);

    try {

      const response = await fetch(url);

      const data = await response.json();

      setTours(data);

      setLoading(false);

    } catch (err) {

      console.log(err);

      setLoading(false);

    }

  };

  const removeTours = (id) => {

    const removedTours = tours.filter((tour) => tour.id !== id);

    setTours(removedTours);

  }

  

  useEffect(() => {

    fetchData();

  }, []);

  

  if (loading) {

    return (

      <div>

        <Loading />

      </div>

    );

  }

  

  if(tours.length === 0){

    return <main>

      <div>

        <h2>no data is there mamae</h2>

      </div>

      </main>

  }

  return (

    <div>

      <Tours tours={tours} removeTours={removeTours}/>

    </div>

  );

};

  

export default App;
```