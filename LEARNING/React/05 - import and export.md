- There or two types to export it
- For exporting the data
```
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

import {books} from './books'
```
- The second approach is using export default
```
export default books;
import {book} from './Book'
```