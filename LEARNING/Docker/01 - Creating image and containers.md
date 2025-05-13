- This is the way to create docker image
- [The container is extra thin command layer which will run on top of the images] example [Our Code  layer-> node layer]
```

#Getting Base image for Docker

FROM node:latest  

  

#Set Working directory to /app/codes

WORKDIR /app/codes/

  

#Copying package.json file before code which will not cache it again

COPY package.json /app/codes/

  

#Lets install the dependencies

RUN npm install

  

#Coping the whole files into the /app inside the container

COPY . /app/codes/

  

#Expose into container not for outside we need to do that

EXPOSE 80

  

#Using CMD we running to container. it wil not work when container is being created

CMD ["node", "server.js"]

docker build . 


```

- Run and publish the docker in 3000
```
 docker run -p3000:3000  sha256:fa865ce5d569cc49e5283c13276fa94d51a877cd6162e8657923d   

```

- Start and stop the container 
```
docker start id

docker stop names [PandaMan]
```

- How the image related with the container
- Docker - The container which contains the actual package with the configuration is called containers previous example [Concrete Running instance]
- Images are the blue  print of the previous code.  using the container we can run many instance  once we created.
- Two way to use the image - First Pre-build image [Docker hub]
```
docker run node  //To run the pre build images


docker ps -a //it will show all the images that we pulled


docker run -it node // we will go to the interactive shell
```
- Second we itself build our own image
- Container wont expose our container to our local machine

#Rebuild
- if we re build the image again it will cache all the data if done
- and the image is layer based 
- and container is Layer based which work on top of the Images 
- changes will not re exec the whole process
- It is called ``Layed architecture``
```
Example

Linux -> node -> dependencies -> server
```
