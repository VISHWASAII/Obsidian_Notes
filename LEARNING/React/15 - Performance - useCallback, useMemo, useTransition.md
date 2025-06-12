   - we need to lower the state which means we need to sperate the component by component
   - the memo check where the props chaning if not it will not rerender the whole thing

**React.memo()**:
```
Return memoized Component

in the component we if we return there in the export we need to add the memo

export default memo(listOfData)

it will only return the component
```

**UseCallback:**
- used to memoize the function 
- it is like constructor it will read the data only once when its re render
- using the useCallback used to reder component only once like if we delete the user using the id in the function it will load only once
- instead of reder as whole
```
- we need to use the combination of the user
- And if we you it it will not render whole component
```
