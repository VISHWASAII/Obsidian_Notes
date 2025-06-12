Here is your Docker **Data Management** section presented in a **clean Markdown table format**, ideal for use in **Obsidian** or any Markdown-supported editor:

---

### 💾 Data in Docker

#### 🔄 Data Types

|Type|Description|Persistence|
|---|---|---|
|**Temporary App Data**|Data stored in container's writable layer (not in image).  <br>Used for variable/temp storage.|**Lost** on container restart.|
|**Permanent App Data**|Data stored in databases/filesystems inside container.  <br>Supports read & write.|**Lost** if not persisted outside.|

> 🧠 **Note:** Container data is lost on restart because of Docker’s **thin writable layer**. To **persist data**, use **Volumes**.

---

### 📦 Docker Volumes

|Concept|Description|
|---|---|
|**Volumes**|A method to **persist and share** data between container and host machine.|
|**Mounted Path**|Maps path from container to **host machine** path.|
|**Persistence**|Volumes persist data even after container restarts or is removed.|
|**Access**|Containers can **read and write** to volumes.|

---

#### 📁 Types of Volumes

|Type|Description|Behavior|
|---|---|---|
|**Anonymous Volume**|No name assigned, only exists when container is running.|Removed with container.|
|**Named Volume**|Volume with a specific name, managed by Docker.|Survives restarts and deletions.|

```
docker volume ls
```

bind mount with example
```
Bind mount similar to the named volume but we can specify our needed path manually
```

- This is the code for that
```
docker run -d \
  -v ~/my-app:/usr/src/app \
  -w /usr/src/app \
  -p 3000:3000 \
  node:latest \
  node app.js

```

```
- `-v ~/my-app:/usr/src/app` → Bind mount your local folder to `/usr/src/app` in the container.
    
- `-w /usr/src/app` → Sets working directory.
    
- `node:latest` → Uses Node.js official image.
    
- `node app.js` → Runs your app.
```
- Live sync with host — great for **local development**

#### 📁 Bind mount
[Important]
- When you run the container with a **bind mount**, your local folder (without `node_modules`) **overrides** the container’s `/app` (which had `node_modules` during build), so the app crashes due to missing dependencies.
- when we are doing the bind mount without node module and while build we are doing npm install during the bind mount it will override the previous version
- If you're using a **named volume**, Docker **manages the storage separately**, so your app code and `node_modules` won't be overridden.  
- This ensures that `node_modules` installed during image build **remain intact**, preventing runtime issues. ✅
- To overcome this thing we need to use the seperate volume
```
docker run -d \
  -v ~/my-app:/usr/src/app \
  -v /usr/src/app/node_modules \
  -w /usr/src/app \
  -p 3000:3000 \
  node:latest \
  node app.js
-- we need to create anonymous as well as for the host machine folder
```
- When you bind mount your local project (e.g. `~/my-app:/usr/src/app`), it **replaces everything** in `/usr/src/app`, including `node_modules` that were installed during Docker image build.
- the bind mount will do live update to our application whatever change we made
- or if we restar t the application it will work fine.
- Then the subfolder `/usr/src/app/node_modules` is **overmounted** by the **named volume**, which hides whatever is in the bind mount at that path.
```
- we need to use the nodemon we need live update or reflect when it updated
```

#### 📁 Read-only volume
- we can set the volume read only after internal path we specify
- it is good practice to use not to override internal code
```
internalpath:ro
```
```
docker volume ls  // it will show all the volume inside the container
docker volume inspect feedback  // we can see all the volumes   
docker volume rm feedbacak //it will remove the volume
```
