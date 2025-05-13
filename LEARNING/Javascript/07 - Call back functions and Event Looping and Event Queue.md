- It is non Blocking and asynchronous 
#Callback
- A function to be called when certain task happen it is called the call back function
- It is called Async
- When we receive the data we need to do Something using that it is called Async
- After some operation done we are calling the function then it is called the call back function
```
function fetchData (callback) {

    setTimeout(() => {

        const data = 'fecthed data';

    callback(data, null);

 }, 5000)

}

  

fetchData(callback);

  

function  callback(data, err){

    if(data) {

        console.log('This is the value');

    }else{

        console.log("Errot");

    }

}
```
- Need to learn the Event Looping which is taught by the node user
- Pyramid of doom calling call back again and again
- To avoid the Call back hell we are using the promises.
- we are giving the control to another function call inversion of control
- Promise - objects - Pending, Fulfilled, Rejected
```
function getData() {

    return new Promise((resolve, reject) => {

        setTimeout(() => {

            resolve('data Fetched');

         },5000)

     })

}

//We are keep chaining it.

getData()

    .then((result) => { //If we use the reslove invoke the result

        console.log(result);

    })

    .catch((error) => { //if we access error it will call the error

        console.log(error);

     })
```