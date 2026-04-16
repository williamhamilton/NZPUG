
# RDBMS & SQL Primer

## What is an RDBMS?

A **Relational Database Management System (RDBMS)** stores data in structured tables and manages relationships between them.

### Key Concepts

* **Table**: A collection of rows (records) and columns (fields)
* **Row**: A single record
* **Column**: A specific attribute (e.g., `Name`, `Date`)
* **Primary Key (PK)**: Uniquely identifies each row
* **Foreign Key (FK)**: Links one table to another
* **Schema**: The structure/definition of the database

### Example

```
Customers
---------
CustomerID (PK)
Name
Email

Orders
------
OrderID (PK)
CustomerID (FK)
OrderDate
```

---

## Relationships

* **One-to-One**: One record relates to one record
* **One-to-Many**: One customer → many orders
* **Many-to-Many**: Requires a **junction table**

---

## What is SQL?

**Structured Query Language (SQL)** is used to interact with an RDBMS.

---

## Core SQL Operations (CRUD)

### 1. Create (INSERT)

```sql
INSERT INTO Customers (Name, Email)
VALUES ('Alice Smith', 'alice@example.com');
```

---

### 2. Read (SELECT)

```sql
SELECT Name, Email
FROM Customers
WHERE Name = 'Alice Smith';
```

---

### 3. Update (UPDATE)

```sql
UPDATE Customers
SET Email = 'alice.new@example.com'
WHERE CustomerID = 1;
```

---

### 4. Delete (DELETE)

```sql
DELETE FROM Customers
WHERE CustomerID = 1;
```

---

## Filtering & Sorting

```sql
SELECT *
FROM Orders
WHERE OrderDate >= '2025-01-01'
ORDER BY OrderDate DESC;
```

---

## Joins (Combining Tables)

### INNER JOIN (most common)

```sql
SELECT c.Name, o.OrderDate
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID;
```

### LEFT JOIN

Returns all customers, even if no orders:

```sql
SELECT c.Name, o.OrderDate
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID;
```

---

## Aggregation

```sql
SELECT CustomerID, COUNT(*) AS OrderCount
FROM Orders
GROUP BY CustomerID;
```

Common functions:

* `COUNT()`
* `SUM()`
* `AVG()`
* `MIN()`
* `MAX()`

---

## Constraints

Used to enforce data integrity:

* `PRIMARY KEY`
* `FOREIGN KEY`
* `NOT NULL`
* `UNIQUE`
* `CHECK`

---

## Indexes

* Improve query performance
* Trade-off: slower writes

```sql
CREATE INDEX idx_customer_name ON Customers(Name);
```

---

## Transactions

Ensure reliability:

```sql
BEGIN TRANSACTION;

UPDATE Accounts SET Balance = Balance - 100 WHERE ID = 1;
UPDATE Accounts SET Balance = Balance + 100 WHERE ID = 2;

COMMIT;
-- or ROLLBACK;
```

---

## Normalisation (Quick Idea)

Organising data to:

* Reduce duplication
* Improve consistency

Typical goal: **3rd Normal Form (3NF)**

---

## Common RDBMS Systems

* SQL Server
* PostgreSQL
* MySQL
* SQLite
* Oracle

---

## Practical Tips

* Always use a **WHERE** clause in `UPDATE`/`DELETE`
* Use meaningful keys and constraints
* Prefer joins over duplicating data
* Index selectively (not everything)
* Think in **sets**, not loops

---


