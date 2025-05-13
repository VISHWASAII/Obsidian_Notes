- Using psycopg we can able to connect with the postgres
- I need to use the ``Psycopg``
```
import psycopg

app = FastAPI()

  
  

try:

    conn_string = "host='localhost' dbname='postgres' user='postgres' password='Saivishwa13'"

    print( "Connecting to database\n    ->%s" % (conn_string))

    conn = psycopg.connect(conn_string)

    cursor = conn.cursor()

    print("Connected!\n")

except Exception as err:

    print(f"Error while connecting to the database", err)
```

- Google it can we can connect it
```
        tb = cursor.execute("""

            CREATE TABLE articles(

                id INT  PRIMARY KEY,

                title VARCHAR(255),

                content TEXT,

                published BOOLEAN DEFAULT FALSE                  

            )

            """)

        print("Table")
```

- THis is how we are going to connect
```
cursor.fetchAll() -- Used to fetch the data
```
- By reading the blog we will connect all types of data crud
- 