# Day 1: Understanding Python Type Hints
# These are the "Recipes" we saw in the FastAPI source code!

from typing import Annotated, TypeVar

# 1. Basic Type Hints
# name: type = value
def greet(name: str) -> str:
    return f"Hello, {name}"

# 2. TypeVar (The Placeholder)
# Used when you don't know the exact type yet, but you want to say 
# "whatever type comes in, that same type comes out"
T = TypeVar("T")

def get_first_item(items: list[T]) -> T:
    return items[0]

# 3. Annotated (The Type with a Sticky Note)
# Annotated[Type, Metadata]
# FastAPI uses this to add documentation (Doc) to parameters
def process_user(
    username: Annotated[str, "The unique name of the user"]
) -> None:
    print(f"Processing user: {username}")

if __name__ == "__main__":
    # Test Basic Hint
    print(greet("Student"))
    
    # Test TypeVar
    numbers = [10, 20, 30]
    first_num = get_first_item(numbers) # Python knows first_num is an int
    print(f"First number: {first_num}")
    
    # Test Annotated
    process_user("fastapi_learner")

# --- Key Takeaway for FastAPI ---
# FastAPI reads these "Recipes" (Type Hints) to:
# 1. Validate your data (make sure it's the right type)
# 2. Convert your data (e.g., turn text "123" into number 123)
# 3. Generate the Documentation page automatically!
