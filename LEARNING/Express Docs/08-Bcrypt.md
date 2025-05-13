- we need to install the bcrypt
```
npm i install bcrypt
```
- we need to import the brcrpyt in the helper file in and bcrypt it
```
import bcrypt from "bcrypt"

  

const saltRounds = 10;

  

export const hashedPassword = (password) => {

    const salt = bcrypt.genSaltSync(saltRounds);

    bcrypt.hashSync(password, salt);

```
- This is how we are going to use the hashed password
```
app.post('/api/users', async (req, res) => {

    try {

      const { name, position } = req.body;

      if (!name || !position) {

        return res.status(400).json({ error: 'Name and position are required' });

      }

      const hashPosition = hashedPassword(position);

      console.log(hashPosition);

      const newUser = await UpdatedUser.create({

        name,

        position: hashPosition  //name must be the entity

      });

      res.status(201).json(newUser);

    } catch (error) {

      console.error('Error creating user:', error);

      res.status(500).json({ error: 'Failed to create user' });

    }

  });
```

- This will used for comparing
```
export const comparePassword = (plain, hashedPassword) => {

    return bcrypt.compareSync(plain, hashedPassword);

}
```