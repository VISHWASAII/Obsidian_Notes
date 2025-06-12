- it is stateManager
- it is used to manage the state
- it is alternative of useState
- When two or more method need to change then we need to use the useReducer
- if the states are in diff types then we need to use that
- it is used to manage multiple state
```
data.jsx
export const INITIAL_VALUE = {

  name: "",

  email: "",

  password: "",

}

useReducer.jsx

import { useReducer } from "react"

  

export const postReducer = (state, action) => {

  

    switch (action.type) {

        case "HANDLE_INPUT":

            return {

              ...state,

              [action.payload.name]: action.payload.value

            };

        case "RESET_INPUT":

            return {

                name: "",

                email: "",

                password: ""

            }

          default:

            return state;

      }

  

}


APP.jsx
import React, { useReducer } from "react";

import { INITIAL_VALUE } from "./data";

import { postReducer } from "./useReducer";

  

function App() {

  const [state, dispatch] = useReducer(postReducer, INITIAL_VALUE);

  

  const handleChange = (e) => {

    dispatch({

      type: "HANDLE_INPUT",

      payload: {

        name: e.target.name,

        value: e.target.value,

      },

    });

  };

  

  const handleReset = () => {

    dispatch({ type: "RESET_INPUT" });

  };

  

  return (

    <div>

      <input

        type="text"

        name="name"

        placeholder="Name"

        value={state.name}        

        onChange={handleChange}

      />

      <input

        type="email"

        name="email"

        placeholder="Email"

        value={state.email}        

        onChange={handleChange}

      />

      <input

        type="password"

        name="password"

        placeholder="Password"

        value={state.password}    

        onChange={handleChange}

      />

      <button type="button" onClick={handleReset}>

        Reset

      </button>

      <pre>{JSON.stringify(state, null, 2)}</pre>

    </div>

  );

}

  

export default App;
```