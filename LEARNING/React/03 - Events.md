```
There are three types of react events\

onClick -- used for During button input
onSubmit -- used after submition 
collect the input fields [input type need to be submit] (imp)
onChange -- Used for form input

Example 

//This is event for handling
const EventExamples = () => {
  const handleButtonClick = () => {
    alert('handle button click');
  };

//When the onclick is happening it will trigger that function
  return (
    <section>
      <button onClick={handleButtonClick}>click me</button>
    </section>
  );
};

for the form submition if we want to get the input form the input field

then we need to use this
const handleFormInput = (e) => {
clg.log(e.target.name)
clg.log(e.target.value)
}

```

- Instead of creating a sperate function we can use the runnable class in java
```
return (
    <button onClick={() =>     shoot("Goal!")}>Take the shot!</button>
  );
}
```

