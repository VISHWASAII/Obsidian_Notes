```
const isLoggedIn = (req, res, next) => {

    if (req.user) {

      next();

    } else {

      res.status(401).send('Not Logged In');

    }

  }

  export {isLoggedIn}
```

```
import express from "express";

import dotenv from "dotenv";

import cookieSession from "cookie-se
```

- This is how we are passing the configuration
```
import passport from "passport";

import GitHubStrategy from 'passport-github2';

  
  

passport.serializeUser(function(user, done){

    document(null, user);

})

  

passport.deserializeUser(function(user, done) {

    done(null, user);

  });

  

  passport.use(new GitHubStrategy({

    clientID: "Ov23liKSqJrducwAvBCz",

    clientSecret: "4605c773b4f4e596a8b831c7b17a3f90ff76c04c",

    callbackURL: "http://localhost:8000/auth/github/callback"

  },

  function(accessToken, refreshToken, profile, done) {

    return done(null, profile);

  }

  ));

  

  export default passport; //This one is main
```

#Routers
- This is how i need to route the user
```
import  Router  from "express";

  
  

const urlShortner = Router();

  

urlShortner.get('/urlShortener', (req, res) => {

    return res.send("Working fine");

 })

  
  

export default urlShortner
```

- The middleware need to be in order
```
app.use(express.json()); // <== First, add body parser
app.use('/api', router); // <== Then mount the routes

```