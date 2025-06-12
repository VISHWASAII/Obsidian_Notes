- where qualifier bean will be used?
```
- Lets consider we have one interface
- which is override by two implimentation
- For that if we take initialized the object using interface
- we need to specify @Qualifier("value") and we can take which one to initialize
- or we can initialize using the Dynamic initialization like @Value
```
- Conditional bean creation
```
- lets consider if we have two database connection we can conditionally connect it using @ConditionalOnProperty
```