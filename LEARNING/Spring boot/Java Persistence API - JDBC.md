**Introduction to JDBC**
![[Pasted image 20250515111817.png]]````

```
Workflow
- Application Login user writes the code
- the JPA is a interfcae which provide method
- And the hibernate is a implementation of the interface
- And hibernate takes with the JDBC
- Specific DB driver for the Relational database
- Relational Database
```

- ORM - bridge between Java object with relational database

**JDBC:** provide intercate
- Make connection with db
- Query with db
- and process the result
```
- Load the driver
- we need to make the db connection
- we need to write a query and the configure it properly
- we need to handle the plain jdbc
```

**JDBC in spring boot:**
```
-First we need to add the jdbc configuration in tht spring boot

- Annoteded with the repository

-@Autowired the JdbcTemplate;
-then we need to do like jdbcTemplate.execute(), update(), query();

- it uses Hikari connection pool
```

persistan  unit - configuration -> db, driver, dialect 
it will convert the config to object -> entity manager factory   [The previous and this need to be equal (1:1)]


Entity manager - session - Entity Is a interface that allow to use all the Jpa method the repository is the wrapper of the repository [this and the previous are one to many relationship [1:M]]

per context - it will hold the object which we pass in the repository or placeholder

from the per context we can update it. This will help first level caching

Dialect - Help to convert jql into Sql

dialect talk to Jdbc and that wil to the operation


- we need to manualy create the transaction manager if we create multiple instance of the database

