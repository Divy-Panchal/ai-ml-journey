# Day 1: Understanding Python Decorators
# In FastAPI, you see these as @app.get("/") or @app.post("/")


"""In Python, a decorator is a function that takes another function 
    as an argument and extends its behavior without explicitly modifying 
    the original function's source code"""


# 1. A basic decorator is a function that wraps another function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# 2. Using the decorator with the '@' symbol
@my_decorator
def say_hello():
    print("Hello!")


# 3. Running the function
if __name__ == "__main__":
    # When you call say_hello(), it is actually running the 'wrapper' 
    # inside the decorator
    say_hello()

# --- Key Takeaways for FastAPI ---
# When you see @app.get("/"), FastAPI is "wrapping" your function.
# It registers your function as a "path operation" so it knows to run it 
# whenever someone visits that URL!
