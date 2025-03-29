Hi, I'm Vishwa!

I'm currently a final-year M.Tech Software Engineering student. I recently completed my internship at Genpact as a backend developer. I'm familiar with Java Spring Boot, Python FastAPI, and system design concepts.

I have implemented several architectural styles, including microservices, Saga, CQRS, and service discovery. 

and also i implemented spring security like OAuth and Jwt for Authentication and Authorization 

I've worked with message brokers like Kafka and RabbitMQ,  implement event-driven and asynchronous comminication betweent the services.

I have also dockerized my applications.

Additionally, I am knowledgeable about various database strategies, including pessimistic and optimistic approaches, to maintain data consistency.

Furthermore, I have created multiple CI/CD pipelines in Jenkins as well as on AWS.

during the intership ive been the tech lead for the backend

what is optimistic and pessimitic

1. **User A** reads a record (Version = 1).
2. **User B** also reads the same record (Version = 1).
3. **User A** updates the record (Version = 2). ✅
4. **User B** tries to update, but sees the version has changed (Version = 2 ≠ 1). ❌ Update fails.

if i have two user those two access the data at the same time then it lead to data inconsistance to overcome this one we need to lock one user until user completes the transaction.

what is the difference between http nd https
- **HTTP (HyperText Transfer Protocol)** is the protocol used to transfer data between a web browser (client) and a web server. 
- Https is more secure compare to the Http becoz the data's are secure [Secure (data is encrypted using SSL/TLS)]
- **SSL (Secure Sockets Layer)** is a security protocol that encrypts data sent between a web browser (client) and a web server.
routing:
**Routing** is the process of directing network traffic or requests to the correct destination.

what is serialization:
**Serialization** is the process of converting a Java/Python object **into a format** (JSON, XML, or binary) so that it can be **stored or sent** over a network.

Middleware:
- it will intercept each and every request and it will check whehter the user is authenticate or not if not authenticate it will naviagate to login page.

**RESTful architecture** is a software design style for building web services that follow the principles of **REST (Representational State Transfer)**. It relies on **stateless communication**
- it is stateless url based communication between client and the server using the https method like put, create, update, and delete

|Feature|**WebSocket**|**Webhook**|**SSE (Server-Sent Events)**|
|---|---|---|---|
|**Type**|Bi-directional communication|Event-driven callback|One-way server-to-client communication|
|**Direction**|Both client & server can send messages|Server calls client’s URL|Server sends updates to the client|
|**Connection**|Persistent connection|No persistent connection|Persistent connection|
 
what is the difference between authentication and authorization
 - we will do replicas of our application and 
- Authentication is used to identify the user whether he is genuine or not
- Authorization is used to to check whether the user is 
**what youll do to reduce scalable the application:**

-  ill do serveral replica of the instance
- And illl use the load balancer to distribute the traffic accors the servicer
- And also we can use data base replicas to reduce the strain to the database
- we can use the CQRS Design pattern


What strategies have you used to make a backend application scalable?
I have used several strategies, including:

Load Balancing to distribute traffic across multiple servers. [ill use loadbalancer to distribute the traffic across the instance or service]

Database Replication to create read replicas and reduce the load on the main database. [We can use the database replicas]

Caching using Redis or Memcached to store frequently accessed data.
[we can use the redis to reduce the latency]

Asynchronous Processing with message queues like Kafka and RabbitMQ to handle background tasks.

Microservices Architecture to break the application into smaller, independent services.

2. How does a load balancer help in scaling a server-side application?
A load balancer acts as a traffic manager that distributes incoming requests across multiple servers.

It prevents a single server from getting overloaded.
It improves response times and system reliability.
If one server goes down, the load balancer redirects traffic to the healthy servers, ensuring availability.

- **Multiple instances of the monolithic app** → Run the same app on different servers (e.g., three instances).
- **Load Balancer (Nginx, HAProxy, AWS ELB, etc.)** → Distributes requests across these instances.
- **Single Database** → All instances connect to a shared database.


Microservices architecture breaks down an application into small, independent services. Each service handles a specific function (e.g., authentication, payments, orders).

- **Independent Scaling** – Services can scale individually based on demand.
- **Fault Isolation** – A failure in one service doesn’t affect the entire system.
- **Technology Flexibility** – Different services can use different tech stacks.
- **Faster Development** – Teams can work on separate services simultaneously.