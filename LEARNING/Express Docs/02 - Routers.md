- similar to the app we need to use the router and configure into the index for the starting
- This is how the routers are working
```import {Router} from "express";

import getListOfUsers from "../utils/Constants.mjs";

import { v4 as uuidv4 } from 'uuid';

  
//Instead of app we are using the routes

const router = Router(); //here what name we mention it need to be in the export

  

//Get Request

router.get('/getUsers', (req, res) => {

    return res.status(200).send(getListOfUsers)

})


//post Request

router.post('/createUser', (req, res) => {

    const {name, position} = req.body;

    if(!name || !position){

         return res.status(400).send({message: "User name and postion not found"});

     }

    const users = {

        id: uuidv4(),

        name,

        position

    }

    return res.status(201).status({message: "user Created Successfully"});

})


//Delete Request

  
  

export default router
```
- we are going to use the Middleware and the import statement for this
```//import statement

import router from './Routers/User.mjs';

import express from 'express';

import "dotenv/config";

  

//Instance of express

const app = express();

  

//Port instance

const PORT = process.env.PORT || 3001

  

//MiddleWare functions

app.use(express.json())

app.use('/api',router)

  

//check the connection

app.get('/', (req, res) => {

    res.send({message: "working fine"});

})

  

//config the port with the Server

app.listen(PORT, () => {

    console.log("Server Running on Port", PORT);

})
```
- the list of users are the constant becoz it contains the list of users
- Need to learn what is Match data in the validator
- Again we need to import to the index.js file
Gathering the import files
- Instead of import js files one by one we need to use the centralized router

