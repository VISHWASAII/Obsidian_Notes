- It is used for refactor or reuse of the code
- What is parameters?
```
// parameters
const someFunc = (param1, param2) => {
  console.log(param1, param2);
};
// arguments
someFunc('job', 'developer');
```
- instead of Parameters we are going to user the probs
```
for this we are going to use the probs
like self in python

const author = 'Jordan Moore';
const title = 'Interesting Facts For Curious Minds';

const Book = (props) => {
  console.log(props);
  return (
    <article className='book'>
      <img src={props. img} alt={title} />
      <h2>{props.title}</h2>
      <h4>{props.author} </h4>
      {console.log(props)}
    </article>
  );
};

//Accessing an props or object
props.title
props.number
```

**Types of Props**
```
- there is no right or wrong - again preference !!!
    
- Destructuring (object) [JS Nuggets 
    
- destructuring in Vanilla JS
    
- saves time/typing
    
- pull out the properties
    
- don't need to reference object anymore
```
01 - Deconstruct Props
-  Deconstruct the props
```
const {img, title, author} = props;
```

02 - Deconstruct using the function also
```
const Book = ({ img, title, author }) => {
  return (
    <article className='book'>
      <img src={img} alt={title} />
      <h2>{title}</h2>
      <h4>{author} </h4>
    </article>
  );
};
```

03 - Children Props
```
we can put the piece of code in between the component

<Book>
	<h2> Hello </h2>
</Book>

const Book = (props) => {
  const { img, title, author, children } = props; //Need to use like this
  console.log(props);
  return (
    <article className='book'>
      <img src={img} alt={title} />
      <h2>{title}</h2>
      <h4>{author} </h4>
      {children}
    </article>
  );
};
```

04 - Proper List
```
//THis is the list we are going to use i throught the map

export const books = [

  {

    author: 'Jordan Moore',

    title: 'Interesting Facts For Curious Minds',

    img: './images/book-1.jpg',

    id: 1,

  },

  {

    author: 'James Clear',

    title: 'Atomic Habits',

    img: 'https://images-na.ssl-images-amazon.com/images/I/81wgcld4wxL._AC_UL900_SR900,600_.jpg',

    id: 2,

  },

];


  
//In the book we are destructing and passing the data
function BookList() {

  return (

    <section className='bookList'>

      {books.map((book) => {

          const {img, title, author} = book;

        return (

          <Book img={img} title={title} author = {author}/>

        )

       })}

    </section>

  );

}

```

05 -  Key props
- While loop through the arrays we need to use the key props or else it will through the error
- Add the key in the padding compotent
- if we provide index it will work automatically
```
  {

    author: 'Jordan Moore',

    title: 'Interesting Facts For Curious Minds',

    img: './images/book-1.jpg',

    id: 1,

  },

function BookList() {

  return (

    <section className='bookList'>

      {books.map((book, index) => {

          const {img, title, author, id} = book;

        return (

          <Book img={img} title={title} author = {author} key ={index}/> 
          //Here we need to add this

        )

       })}

    </section>

  );

}
```

05 - Object Props
- There are several approach to pass the object
- We can use the spread Operator best one
```
 function BookList() {

  return (

    <section className='bookList'>

      {books.map((book) => {

        return (

          <Book {...book} key={book.id}/>

        )

       })}

    </section>

  );

}
```

06 - props drilling

```
//We can pass the function as a paramener

someValue ->[Drilled] -> function -> [Drilled fun] --> parameter

function BookList() {
  const someValue = 'shakeAndBake';
  const displayValue = () => {
    console.log(someValue);
  };
  return (
    <section className='booklist'>
      {books.map((book) => {
        return <Book {...book} key={book.id} displayValue={displayValue} />;
      })}
    </section>
  );
}

const Book = (props) => {
  const { img, title, author, displayValue // we can pass the function as a parameter also } = props;

  return (
    <article className='book'>
      <img src={img} alt={title} />
      <h2>{title}</h2>
      <button onClick={displayValue}>click me</button>
      <h4>{author} </h4>
    </article>
  );
};
```
