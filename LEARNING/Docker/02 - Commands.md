### 🐳 Docker Commands Overview

#### 📌 Attach and Detach Modes

|Command|Description|
|---|---|
|`docker start`|Starts an **existing container** in **detached mode**.|
|`docker run`|Runs a container in **attached mode by default**.|
|`docker run -d`|Runs container in **detached mode (background)**.|
|`docker logs <id>`|Shows logs from the container.|
|`docker logs -f <id>`|Follows logs in real time (like `tail -f`).|
|`docker attach <name>`|Attaches to a running container (see live output).|
|`docker start -a <id>`|Starts a container and attaches to it immediately.|
#### 🗑️ Deleting Containers and Images

| Command                 | Description                                    |
| ----------------------- | ---------------------------------------------- |
| `docker stop <name>`    | Stops a running container.                     |
| `docker rm <name>`      | Removes a **stopped** container.               |
| `docker rm name1 name2` | Remove multiple containers at once.            |
| `docker rmi <id>`       | Removes an image (if not used).                |
| `docker image prune`    | Removes **all unused** Docker images.          |
| `docker run --rm`       | Automatically removes container when it stops. |

---

#### 🔍 Inspect Details

|Command|Description|
|---|---|
|`docker inspect <id>`|Shows detailed metadata in JSON format (network, volume, etc.).|

---

#### 📁 Copy Files

|Command|Description|
|---|---|
|`docker cp <src> <container>:<dest>`|Copies from **local machine to container**.  <br>Example: `docker cp dummy/. container:/test`|
|`docker cp <container>:<src> <dest>`|Copies from **container to local machine**.  <br>Example: `docker cp container:/test dummy/`|

---

#### 🏷️ Tagging and Naming Images

|Command|Description|
|---|---|
|`docker build -t <name>:<tag> .`|Builds image with a name and tag.  <br>Example: `goals:latest`|
|`docker run --name <name> <image>`|Assigns a custom name to a running container.|

---

#### ☁️ Sharing Images (Push/Pull)

|Command|Description|
|---|---|
|`docker login`|Logs in to Docker Hub.|
|`docker tag <image> <username>/<repo>:<tag>`|Tags image for upload.|
|`docker push <username>/<repo>:<tag>`|Pushes image to Docker Hub.|
|`docker pull <username>/<repo>:<tag>`|Pulls image from Docker Hub.|