# Day 2: Understanding Context Managers
# Key Concept: The 'with' statement handles setup and cleanup automatically.

# 1. Without context manager (clunky and risky)
# If the program crashes after 'open', the file might stay "locked" forever.
file = open("test.txt", "w")
file.write("Hello, Student!\n")
file.close()  # Easy to forget this line!


# 2. With context manager (clean and safe)
# The file is GUARANTEED to close, even if an error happens.
with open("test.txt", "a") as file:
    file.write("Hello, Student!\n")
# File automatically closes right here.


# 3. Custom Context Manager (How it works under the hood)
# This is what you see in FastAPI for database connections.
class MyConnection:
    def __enter__(self):
        print("--- Step A: Opening connection... (This is __enter__)")
        return self
    
    def query(self, sql):
        print(f"--- Step B: Running Query: {sql}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("--- Step C: Closing connection... (This is __exit__)")

# Usage:
print("\n--- Starting the 'with' block ---")
with MyConnection() as conn:
    conn.query("SELECT * FROM users")
print("--- Finished the 'with' block ---\n")


# --- Why this matters for FastAPI ---
# FastAPI uses this pattern for "Dependencies." 
# For example, when you connect to a database:
# 1. It opens the connection for you (__enter__)
# 2. It lets your function run
# 3. It closes the connection for you automatically (__exit__) 
# This way, you never accidentally leave 1,000 database connections open!
