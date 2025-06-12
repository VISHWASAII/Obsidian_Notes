- it is used to fetch the Data's from the endpoint
src/
├── api/
│   ├── axiosInstance.js
│   ├── userApi.js
│   └── authApi.js
├── components/
│   ├── Login.jsx
│   └── UserList.jsx

- Axios instance jsx
```
// src/api/axiosInstance.js
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
    // Authorization can be set later with interceptors
  }
});

// Optional: Add interceptors here if needed
axiosInstance.interceptors.request.use(
  config => {
    // config.headers['Authorization'] = `Bearer your_token`;
    return config;
  },
  error => Promise.reject(error)
);

export default axiosInstance;

```

- using that we can resue the code where ever we want
// src/api/userApi.js
import axiosInstance from './axiosInstance';

export const getAllUsers = () => axiosInstance.get('/users');

export const getUserById = (id) => axiosInstance.get(`/users/${id}`);

export const createUser = (userData) => axiosInstance.post('/users', userData);

export const updateUser = (id, userData) => axiosInstance.put(`/users/${id}`, userData);

export const deleteUser = (id) => axiosInstance.delete(`/users/${id}`);

- like this we can use it 

```
import React, { useEffect, useState } from 'react';
import { getAllUsers } from '../api/userApi';

const UserList = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    getAllUsers()
      .then(res => setUsers(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Users:</h2>
      {users.map(user => <p key={user.id}>{user.name}</p>)}
    </div>
  );
};

export default UserList;
```