# AuckPUG
Setup for May 2023 presentation in relation to Python Liskov Substitution Principle

Start with a couple of bad/messy/ugly ways then move to a "better" way with OOP utilising the Liskov Substitution Principle

The made up scenario is an application which has "successfully" run on an SQLite database is now moving to a Microsoft SQL Server. The main server is sitting within a Windows Domain (this is the trusted connection - using the already authenticated user details).  The test server is not on this domain but on the spare room wardrobe server of the developer, this server needs to have userID/password sent to it for authentication.

The SQLite database is still being used, although it is called "old" within the script.  

How do you choose between the three databases within the script?  Environment variables and if/elif/else, or maybe some functions or.. is it better Classes!


## Code Summary
1. Extensibility:
By defining an abstract base class `DatabaseConnection` and using concrete subclasses like `OldConnection`, `NewConnection`, and `TestConnection`, this_is_the_way allows for easy extensibility. If a new type of database connection needs to be added, a new subclass can be created that inherits from `DatabaseConnection` and implements the `connect()` method specific to that database type. This ensures that the new subclass can be seamlessly used interchangeably with the existing code, without requiring modifications to the rest of the codebase. This adherence to the LSP enables the codebase to grow and evolve by accommodating new database connection types.

2. Modularity:
The class-based approach in this_is_the_way promotes modularity by encapsulating the connection logic within individual classes. Each subclass represents a specific database connection type, and their responsibilities are limited to establishing a connection to their respective databases. This modular design allows for easier maintenance and readability, as each class is responsible for a specific aspect of the database connection. Modifications or enhancements to a specific database connection can be made within its respective class, without affecting the rest of the codebase.

3. Testability:
The LSP implementation in this_is_the_way also enhances the testability of the code. Since each concrete subclass (`OldConnection`, `NewConnection`, and `TestConnection`) implements the `connect()` method differently, they can be tested independently. This makes it easier to write focused unit tests for each database connection type, verifying their individual behavior and ensuring that they function correctly. By isolating the testing of each class, it becomes simpler to identify and fix any issues or bugs related to specific database connections.

4. Flexibility:
this_is_the_way's adherence to the LSP enables greater flexibility in terms of using different database connection types. The `get_connection()` method, based on the provided `db_type` argument, dynamically returns an instance of the appropriate concrete subclass. This flexibility allows the code to work with multiple database types without requiring changes to the calling code. If a new database connection type needs to be supported, a new subclass can be added, and the `get_connection()` method can be updated accordingly. This dynamic nature of this_is_the_way reduces the coupling between the calling code and the specific database connections, making the code more adaptable to future changes.

By utilising the Liskov Substitution Principle, this_is_the_way's design offers extensibility, modularity, testability, and flexibility. These advantages promote maintainable, scalable, and robust code that can handle different database connection requirements efficiently and reliably.
