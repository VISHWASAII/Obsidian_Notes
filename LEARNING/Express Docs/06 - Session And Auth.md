![[Pasted image 20250402131036.png]]
- The cookie is the medium to send the session to the server 
- Like each user have own session using that the Server will authenticate the user
- Using session id it will authenticate
- We can achieve using express session library
```
npm i install express-session
we need to reg with middleware
app.use(session())
```
- To use this import the session
- And configure these things
```
app.use(session(

   { secret: "amson dev", //it need to be complicated

    saveUninitialized: false, //it will not save the session

    resave: false,

    cookie: {

        maxAge: 600000 * 60, //One hour

    }

   }

))

  

//check the connection

app.get('/', (req, res) => {

    console.log(req.session);

    console.log(req.session.id);

    res.cookie('Hello', 'worldYes', {message: "working fine"});

    res.send({message: "working fine"});

})
```
- if the cookie is not exp it will not generate the new session for the users
- we can set the single session id for the user using the visited: true 
- Using this we can achieve it
``` 
req.session.visited = true;
```
- check browser we will see the cookies
```
s%3Aw1WDD1xrSfZdRmRj6t9hrg4epDO7yCel.o4Rr%2BNKdG1%2FGDBsNmI6lFpkirkwdP0MP3V%2BHA2SOras
```
- to get the session form the session storage we need to use the session store
```
request.sessionStore.get();
```

Authenticate
- Using this i attached the user details into the cookies
- Then we can check whether it is authenticated o not.
```
//authenticate the User

app.post('/api/auth', (req, res) => {

    const{ body: { name, position}} = req;

    if(!name || !position){

        return res.status(400).send(name);

    }

    const getValueOfUser = getListOfUsers.find((users) => users.name === name); //this one is predicate

    if(getValueOfUser.position === position){

        req.session.user = getValueOfUser;

    }

    return res.status(200).send(req.session);

})
```

This is the output for that
```
{

    "cookie": {

        "originalMaxAge": 3600000,

        "expires": "2025-04-02T09:47:40.134Z",

        "httpOnly": true,

        "path": "/"

    },

    "user": {

        "id": 1,

        "name": "John Doe",

        "position": "Software Engineer"

    }

}
``` 
- Using the user we can authenticate it.

#Definition
### **How is the session stored if you don’t have a session storage DB?**

By default, **Express.js uses in-memory session storage** (via `MemoryStore`).

- This means **sessions are stored in the server’s memory** and **will be lost when the server restarts**.
    
- Express automatically assigns a **unique session ID** (`req.sessionID`) to each new user and **stores session data in memory**.
    

---

### **What is `sessionID`?**

The **`sessionID`** is a unique identifier assigned to each user session.

- When a user makes their first request, **Express generates a session and assigns a session ID**.
    
- This ID is then stored in a **cookie on the client’s browser** (e.g., `connect.sid`).
    
- On every subsequent request, the browser **sends back the session ID**, allowing Express to retrieve the session.
```
app.get('/api/auth/status', (req, res) => {

    console.log(req.sessionID);

    req.sessionStore.get(req.sessionID, (err, session) => {

        if (err) {

            return res.status(500).json({ error: "Error retrieving session" });

        }

        if (!session || !session.user) {

            return res.status(401).json({ authenticated: false, message: "User not authenticated" });

        }

        return res.status(200).json({ authenticated: true, user: session.user });

    });

});
```