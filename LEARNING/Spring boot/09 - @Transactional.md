# 🔐 Critical Section

## 📌 Definition

- A **critical section** is a segment of code where shared resources (e.g., data, files) are accessed or modified.
    
- It is **crucial for concurrent data access** and needs proper handling to ensure data integrity.
    

## 💡 Characteristics

- Achieves **ACID principles** using `@Transactional`:
    
    - **Atomicity**: If any step fails, the whole transaction is rolled back.
        
    - **Consistency**: DB remains consistent before and after the transaction.
        
    - **Isolation**: Transactions run independently of one another.
        
    - **Durability**: Once committed, the data persists even after crashes.
        

java

Copy code

`Begin_Transaction:     - Debit from A     - Credit to B     if all success         Commit;     else         Rollback;`

---

# 🧩 @Transactional in Spring

## ✅ Usage

- Can be applied at **method or class level**.
    
    - At **class level**: applies to all `public` methods.
        
    - At **method level**: applies only to that method.
        
- Works with **AOP (Aspect-Oriented Programming)** to reduce duplication.
    

java

Copy code

`@Transactional public void updateUser() {     // Update DB     // Call External API     // Update DB again }`

> ⚠️ May choke under heavy load if not handled efficiently.

---

## 💻 Transaction Approaches

### 🔹 Declarative Approach

- Annotation based: `@Transactional`
    
- Managed by **PlatformTransactionManager**
    
    - Can configure `username`, `password`, `datasource`, etc.
        

### 🔸 Programmatic Approach

- Uses `TransactionTemplate` for finer control.
    

java

Copy code

`transactionTemplate.execute(status -> {     // Business logic here     return null; });`

> Useful for modifying transaction behavior during business logic execution.

---

# 🔄 Propagation Types

|Propagation Type|Description|
|---|---|
|`REQUIRED`|✅ _Default_. Uses existing transaction; creates new if none.|
|`REQUIRES_NEW`|🚫 Suspends parent transaction, starts a new one.|
|`SUPPORTS`|✅ Uses parent transaction if exists; else runs without transaction.|
|`NOT_SUPPORTED`|🚫 Suspends transaction and runs non-transactionally.|
|`MANDATORY`|❗ Requires existing transaction, else throws error.|
|`NEVER`|❗ Throws error if transaction exists.|

---

# 🧪 Isolation Levels

Isolation level ensures consistency and avoids concurrency issues.

## 📉 Problems

### 1. **Dirty Read**

- Transaction A reads uncommitted data from Transaction B.
    
- If B rolls back, A has read invalid data.
    

### 2. **Non-Repeatable Read**

- A reads a value.
    
- B updates and commits the value.
    
- A reads the value again, sees a different result.
    

### 3. **Phantom Read**

- A executes a query (e.g., where status = 'free').
    
- B inserts new rows matching the condition.
    
- A re-executes and sees new rows.
    

---

## 🔐 Locking & Isolation

|Level|Locks|Description|
|---|---|---|
|`READ UNCOMMITTED`|❌ No locks|Risky; allows dirty reads.|
|`READ COMMITTED`|✅ Shared locks|Prevents dirty reads. Most commonly used.|
|`REPEATABLE READ`|✅ Stronger lock|Prevents non-repeatable reads; phantom reads still possible.|
|`SERIALIZABLE`|✅ Range locks|Highest isolation. Prevents phantom reads; lowest concurrency.|

> Use **Read/Write locks** or **DB locking mechanisms** to enforce safety in concurrent environments.

---

## 📌 Notes

- Isolation level selection should be based on **read/write patterns**.
    
- **Read-heavy applications** may safely use `READ COMMITTED` or `REPEATABLE READ`.
    
- **Write-intensive apps** might need `SERIALIZABLE` despite lower performance.