# **An Introduction to SQLModel: Modern Pythonic Data Access**

## **Overview**

In modern application development, working with databases is a fundamental requirement. Traditionally, developers have used **raw SQL** to interact with databases, which gives maximum control but can quickly become verbose, repetitive, and error-prone.

**SQLModel** is a modern library that offers a high-level, Pythonic way to interact with SQL databases. It merges the capabilities of **SQLAlchemy** and **Pydantic**, combining the power of Object-Relational Mapping (ORM) with data validation, serialization, and automatic schema generation.

This guide introduces SQLModel and compares it to using raw SQL, helping you understand when and why you might choose one approach over the other.

---

## **What is SQLModel?**

SQLModel is a library built on top of:

- **SQLAlchemy** – the most powerful and widely used ORM in Python.
- **Pydantic** – a data validation and parsing library, heavily used in FastAPI.

It was created by **Sebastián Ramírez**, also the creator of FastAPI, and is designed to work seamlessly with it. SQLModel lets you define data models as Python classes and use them both as:

- **Database tables** (via SQLAlchemy)
- **Data schemas** (via Pydantic)

### **Key Benefits**

- ✅ Declarative models using standard Python typing
- ✅ Schema generation and migration support
- ✅ Data validation with Pydantic
- ✅ Compatible with asynchronous operations
- ✅ Excellent integration with FastAPI
- ✅ Avoids redundancy between your API and database models

---

## **Example: Comparing SQLModel to Raw SQL**

### **SQLModel Example**

```python
from sqlmodel import SQLModel, Field, create_engine, Session, select

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

# Create database and table
engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

# Insert and fetch data
with Session(engine) as session:
    hero = Hero(name="Deadpond", secret_name="Dive Wilson", age=30)
    session.add(hero)
    session.commit()

    result = session.exec(select(Hero)).all()
    print(result)
```

### **Equivalent Raw SQL Example**

```python
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS hero (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    secret_name TEXT NOT NULL,
    age INTEGER
)
""")

cursor.execute("""
INSERT INTO hero (name, secret_name, age) VALUES (?, ?, ?)
""", ("Deadpond", "Dive Wilson", 30))

conn.commit()

cursor.execute("SELECT * FROM hero")
heroes = cursor.fetchall()
print(heroes)

conn.close()
```

---

## **Detailed Comparison**
*(*taken from ChatGPT response)* 

| Feature                        | SQLModel                                                  | Raw SQL                                                 |
|-------------------------------|------------------------------------------------------------|----------------------------------------------------------|
| **Code Structure**            | Python classes with type hints                             | SQL queries as strings                                   |
| **Data Validation**           | Built-in via Pydantic                                      | Manual validation required                               |
| **Schema Creation**           | Automatic (from model definition)                          | Manual SQL DDL scripts                                   |
| **Query Construction**        | Pythonic with SQLModel + SQLAlchemy                        | Raw SQL strings                                          |
| **Maintainability**           | High (models are reusable and DRY)                         | Low (repeated SQL fragments, prone to typos)            |
| **Integration with APIs**     | Seamless (same model for validation and DB interaction)    | Separate layers for validation and DB                   |
| **Performance Tuning**        | Good, but abstracted through ORM                           | Maximum control, no abstraction                         |
| **Learning Curve**            | Moderate – need to understand SQLAlchemy and Pydantic      | Simple to start, complex for advanced use               |
| **Testing and Mocking**       | Easier with model-based architecture                       | More manual effort                                       |
| **Migration Support**         | Integrates with Alembic (via SQLAlchemy)                   | Manual script-based migrations                          |
| **Async Support**             | Yes, with async engines and sessions                       | Requires use of async-specific DB clients               |

---

## **Advantages of SQLModel**

### 🔹 **Declarative and DRY**
Define your models once and use them across your application — for validation, serialization, and database interaction. This reduces bugs and increases consistency.

### 🔹 **Type-Safe and Validated**
Built on top of Python's typing system and Pydantic, SQLModel ensures that data is validated at the boundaries of your application (e.g., API inputs).

### 🔹 **Automatic Schema Creation**
No need to write repetitive `CREATE TABLE` statements. SQLModel generates the schema from the model automatically.

### 🔹 **FastAPI Integration**
SQLModel is an ideal companion to FastAPI. The same model can define your API schema and your database table — no need for duplication.

### 🔹 **Easier Testing**
Because everything is structured as reusable models and sessions, it’s easier to mock or replace components during testing.

---

## **When to Prefer Raw SQL**

While SQLModel provides many benefits, raw SQL still has its place. You might prefer raw SQL when:

- You need full control over query performance (e.g., query plans, hints, etc.)
- You're working with a legacy database or stored procedures
- You’re doing advanced or database-specific operations
- You're writing a quick one-off script and want minimal dependencies

---

## **Use Cases for SQLModel**

- ✅ CRUD APIs with FastAPI
- ✅ Prototyping database apps quickly
- ✅ Data ingestion pipelines with validation
- ✅ Admin dashboards with clean codebases
- ✅ Projects with high maintainability requirements

---

## **Summary**

**SQLModel** is a modern, clean, and efficient way to work with databases in Python. It reduces boilerplate, increases consistency, and offers strong integration with web frameworks like FastAPI. It’s ideal for developers who want the flexibility of SQLAlchemy and the strictness of Pydantic — all in one place.

For small scripts or performance-critical operations, **raw SQL** might still be the better choice. But for most modern applications — especially web APIs — SQLModel can significantly improve your development experience.

