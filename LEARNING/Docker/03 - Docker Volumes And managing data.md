#DataInDocker
- Images are ready only if we want we need to rebuild the images
- Types of data
- ``Temporary App Data - Store the data into an variable store into the container not in the image`` 
- without changing on the image it changing on the container layer
- ``Permanent App Data - Fetching and producing in the container Store the data into an database``
- If we restart it wont be restart
- It is read write data
```
[Important]
If we have read and write the data if we restart it will be erased becoz the container sits on top of the images

Becoz of thin read write layer its happing to overcome this we are going to store that into the layer of the image
```
#Volumes
- Volumes is help us to persist the data
```
Volumes are map the path from the docker to the volume

volumes --> localmachine path

connect btw inside and outside of the container
```
- A container can write into volume and also read 
- If the system is restarted it will mount into the Local machine into the docker image
- Two type of volumes
```
Anonymous Volumes -- only exists when container running

FROM node:14

  

WORKDIR /work/app

  

COPY package.json .

  

RUN npm install

  

COPY . .

  

EXPOSE 80

  

VOLUME [ "/app/feedback" ]

  

CMD [ "node", "server.js" ]


''Named Volumes -- volumes will be survived when restart''

docker run -p 3000:80 -d -v feedback:/app/feedback  --name volume feedback:volume

- This will be not deleted
```
- Using the docker volume we will see the volumes
```
docker volume ls
```
- 