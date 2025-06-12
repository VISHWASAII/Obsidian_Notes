```
//Build a image
docker build -t feedback:latest -- image name] .

//Running any number of contianer on top of the image3
docker run -p 3000:80 -d --rm --name [feedback --  container name] feedback:latest

//used to start the shutdown container
 docker start volume
 
//Creating a named volumes which will not be deleted
docker run -p 3000:80 -d -v feedback:/app/feedback  --name volume feedback:volume
```
- Steps
```
- First we need to run the image using build
- Second we need to run the container using container name
- then we need to created mouted volume from localmachine to the docker image
```
- In docker file we are just provide definition for the image not for the container