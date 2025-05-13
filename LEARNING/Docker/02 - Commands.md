#AttachAndDetach
- Docker Start - It is detached mood
- Docker run - it is in attached mood

```
If we run on the attach mood we can see the logs and clg when we are running in the attached Mood
```
```
If we use the -d then we will be in the detach mood for the run command
```
- Docker logs - to get the docker logs
- Docker logs -f id -  Using this we will find the logs in attach mode
- Docker start -a id - Using to on into the Attach mood
```
This is main
- Build the docker using docker build
docker build -t goals:latest .

- While run the docker we need to specify the -d detach default it is attach
docker run -p 3000:80 --d  sha256:edbae1675fdba4f9eb907c7383764ba6e432833f7fbb1644b2c719de650e0ee5 

- If we want to attach then we need to do this
docker attach name

-If it is in the detach mood. if we want to see the logs we can use the docker logs -f name
```

#DeletingContainer
- docker rm name - unable to remove the running containers
```
For deleting

docker stop name
docker rm name1 name2 name3 //we can remove by this way

docker rmi id //it will remove the layer which is not in usage

docker image prune //Remove unused images of all containers

```
- whenever the conatiner stopes then i will automatically removed 
```
docker run -p -d --rm 
```

#Interception
- docker inspect id -  it will provide  more important details about the image
- we will see all details about the images
#Copy
- docker cp - used to the files into the docker
```
//Copy from local to docker
docker cp dummy/. elegant_moore:/test

//Copy from docker to local
docker cp elegant_moore:/test dummy
```
- This is used to see the logs of the container
#TaggingAndNaming
- Image tag name and repo 
- name : tag 
- Name is general name - group of possible  more example NODE
- Tag is like version like Node : 12
```
docker run --name vishwa goals:latest dfsa8r9834u2

//while Building we can specify the tag name combo
docker build -t goals:latest .
```
#SharingImages
- We can control the access of the container
```
docker push IMAGE_NAME
docker pull IMAGE_NAME
```
- We need to create Repository in that we need to push the code
- we need to create the name and the tag like |``Local -> git``|
 - The naming is more important
 ```
docker login

Enter the username and password
```
- It will only code not node becoz it already is there