- using ref also we can get the data from the form
- like this get doesnt trigger or re-render
- Preserves the value between the render
- TargetDOM Notes/ element
- once we got the DOM we can use anything using use ref
```
💡 Super Short Summary:

- `useState` – Show and change something (and re-render).
    
- `useEffect` – Run side actions (like fetch or timer).
    
- `useRef` – Keep a value or point to something, quietly.
```
- This is the code for that code
```
import React, { useRef, useState } from 'react';

function ClickTracker() {
  const countRef = useRef(0);           // 🟢 Step 1: Create a ref to store the count
  const [showCount, setShowCount] = useState(0); // Only to show count when you want

  const handleClick = () => {
    countRef.current += 1;              // 🔄 Step 2: Update the value silently
    console.log("Button clicked", countRef.current); // 📌 It changes, but doesn’t re-render

    // Optional: If you want to show it, then update state
    setShowCount(countRef.current);
  };

  return (
    <div>
      <p>Button clicked: {showCount} times</p>
      <button onClick={handleClick}>Click Me</button>
    </div>
  );
}


```

| Line                    | What it does                                      |
| ----------------------- | ------------------------------------------------- |
| `useRef(0)`             | Creates a box with value 0                        |
| `countRef.current`      | You access the current value in that box          |
| `countRef.current += 1` | You increase the value, but no re-render happens  |
| `setShowCount(...)`     | Optional – only if you want to **show the value** |

## 🧠 Simple Summary:

### 🔹 `useState`

- ✅ **Stores value**
    
- ✅ You **get** the value directly
    
- ✅ You **set** value using `setState` function
    
- 🔄 Every time you set, it **re-renders the screen**
    
- 🔁 `useEffect` runs after re-render (if the value it depends on changes)
    

---

### 🔹 `useEffect`

- 📢 **Listens** for changes (like value updates or first page load)
    
- 📦 Can be used to fetch data, start timers, etc.
    
- 🔁 It runs **after rendering**
    

---

### 🔹 `useRef`

- ✅ **Stores a value** or **points to an element**
    
- ❌ Changing it **does NOT re-render**
    
- 👻 It’s like a hidden value that stays during the life of the component