**Setup**
- first we need to initiate the server by
- by importing express
```
i need to create npm init for first
```
- initiatiating the express
- importing the the port
- and listeing the port
```
import express from 'express'
const express = require('express');

const dotenv = require('dotenv').config();

const app = express();

PORT = process.env.PORT || 3001

app.listen(PORT, () => {

    console.log("Server Started...");

})
```

**Add the routes**
```
app.get('/', (req, res) => {

    res.status(201).json({message : "Hello world"});

})
```

**Routes Param**
- used to get the route param
```
app.get('/getUser/:id/:name', (req, res) => {

  res.status(201).send(req.params.id);  

})
```
- Get the user by there id
```
app.get('/getUser/:id', (req, res) => {

    const parseToInt = parseInt(req.params.id);

    if(isNaN(parseToInt)){

        return res.status(400).send({message : "invalid request"});

    }

    const getUser = listOfUsers.find((user) => user.id == parseToInt);

    if(!getUser){

        return res.status(404).send({message: "User not found"});

    }

    return res.status(201).send(getUser);

})
```

Using Query param
 
- The query used to send on the path using this we can filter the user
```
app.get('/getUserByFilter', (req, res) => {

    const {filter, value} = req;

    if(!filter && !value){

        return res.status(400).send({message : "filter and value is not present"});

    }

    if(filter && value){

        const getUserByFilter = listOfUsers.find((user) => {

            user[filter].includes(value);

        })

    }

});
```

POST
- Whenever we pass the data it is payload or body in the endpoint
- we need to use the middleware to handle the json format
- Becoz we are going to handle the json format we need to use this
```
app.use(express.json)
```
- This is the way to represt the post request
```
app.use(express.json) // This is the middleware to handle the req body

app.post('createNewUsers/api', (req, res) => {

    const {name, position} = req.body;

    if(!name || !position){

        res.status(400).send({message : "name and position not found"});

    }
    const users = {

        id: uuidv4(),

        name,

        position

    }
    res.status(201).send(users);

})
```

- Now we are going to use the put and the patch
- Put complete update the body
- Patch partially update the request
-  There are many diff in the both get user by find and findIndex
```
app.put('/updateUserbyIdGet/:id', (req, res) => {

    const{body, params: {id}} = req;

    const userId = parseInt(id);

    if(isNaN(userId)) {

        res.status(400).send({message: "user id not found"});

    }

    const getIndexOfUser = listOfUsers.findIndex((user) => {

        user.id === userId;

    })

    if(getIndexOfUser === -1){

        res.status(404).send({message: "user user not found"});

    }

    listOfUsers[getIndexOfUser] = {id: userId, ...body};

    return res.send({message: "user Created"});

})
```
- For deleting the user we need to add the "splice - index ,  no of ele"
```
app.delete('/deleteUserById/api/:id', (req, res) => {

    const{ param: {id} } = req;

    const parseInt = parseInt(id);

    if(isNaN(parseInt)){

        return res.status(400).send("Invalid reques");

    }

    const getUserIdx = listOfUsers.findIndex(parseInt);

    listOfUsers.splice(getUserIdx, 1);

  

})
```
