- instead of this in axios we can use like this
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

- Combination of Axios and the react query

1) instance
```
// src/api/axios.js
import axios from "axios";

const instance = axios.create({
  baseURL: "https://dummyjson.com",
  withCredentials: true, // if needed for auth cookies
});

export default instance;

```

```
2) Axios for fetching
```
```
import axios from "./axios";

export const getCarts = async () => {
  const res = await axios.get("/carts");
  return res.data;
};

export const getCartById = async (id) => {
  const res = await axios.get(`/carts/${id}`);
  return res.data;
};
```
3) Using react query we are fetching the data
```
import React from "react";
import { useQuery } from "@tanstack/react-query";
import { getUsers } from "../api/users";
import { getCarts } from "../api/carts";

const Dashboard = () => {
  const { data: users, isLoading: usersLoading } = useQuery({
    queryKey: ["users"],
    queryFn: getUsers,
  });

  const { data: carts, isLoading: cartsLoading } = useQuery({
    queryKey: ["carts"],
    queryFn: getCarts,
  });

  if (usersLoading || cartsLoading) return <h2>Loading...</h2>;

  return (
    <div>
      <h2>Users</h2>
      {users.users.map((user) => (
        <p key={user.id}>{user.firstName}</p>
      ))}

      <h2>Carts</h2>
      {carts.carts.map((cart) => (
        <p key={cart.id}>Cart #{cart.id} — Total: {cart.total}</p>
      ))}
    </div>
  );
};

export default Dashboard;

```

