**Critical Section**
- Code segment, where shared Resource are being access and modified
- it is import for the concurrent access of data
- Using Transactional we can achieve the ACID principle
- Atomicity - any fails entire transaction will roll back
- Consistency - Before and After transaction db should be consistent
- Isolation - Multiple transaction will run parallely in isolation environment
- Durability - Once the transaction dont 'commit' the data will be consistent

**Definition:**
- It will apply to method and class level
- if we use it on the class level only public will work
- if we use one method specifically only apply there
- It uses *AOP* using this we can avoid Duplicates
```
Begin_transaction:
   - Debit from A
   - Credit from B
   if all success 
        Commit;
   else 
      RollBack;
```

**Transaction Manager**
- It has a hierarchy For Transaction
- Type of Transactional Manager - Declerative - @Transactionl
- Using platform Transactional Manager class we are modify like datasource like username, password
- And we need to add this into the annotation
- Second type - Programmatic Approach
```
@Transactional
public void updateUser(){
  //update DB
  //External API call
  //Update DB
}
```
- The above will choke when load when traffic is arrived
```
Approach one

First finish the transaction then we are going to do the operation

then commit it
```
- The second approach we are using the transactional template
```
we can modify the transaction

the function going to happen then we are going to declear the transaction

in the bussiness logic we are chaning the transaction which we are going to do
```

**Propagation:**
- when we create new Transaction check propagation value set and this tell whether we have to create new transaction or not
- Types
```
- @Transactional(propagation = Propagation.REQUIRED)- default --- How many transational method it invoke it will use **only one Transaction**
- " " ".REQUIRED_NEW -- suspend the parent transacion will it will create new transaction. once child transaction completed the parent transaction will be resumed
- " ' ".SUPPORTS --- if parent transaction is present use it else without transaction use it
- " " ".NOT_SUPPORTS --- if parent transaction is there suspend and exec the method
- ""  " ".MANDITORY --- if parent transaction is there use it else throw error
- """ " ".NEVER ---- if parent is exists then throw exp else exec method
```

**Isolation Level:**
- it will maintain the concurrency
- Dirty read problem
```
Transaction A reads the uncommited data which is roll backed

ticket Booking
Transaction a 

Tranaction b

trans b - booked -- payment

trans a - Read status booked 

trans b - payment failed

Rollbacked
```
- Non-repeatable Read problem
```
Trans a - started

trans a - read id 1 - free (status)

some trans - id 1 - booked -commited

trans a - again read - booked (status)
```
