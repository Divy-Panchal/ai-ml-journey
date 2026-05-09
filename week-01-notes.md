# Week 1: Diving into FastAPI Source Code

# Day 1

---

## 1. What is `TypeVar`?
**Answer:** Think of `TypeVar` as a **"placeholder"** for a type that isn't known yet.

In line 38: `AppType = TypeVar("AppType", bound="FastAPI")`
This says: "I'm creating a name called `AppType`. It can be `FastAPI` or anything that is based on `FastAPI` (like a plugin)."
It's like saying, "I need a `Vehicle` (`TypeVar`), which could be a `Car` or a `Truck` (specific types)."

---

## 2. How do `from` and `import` work?
**Answer:** This is how Python shares code between files.

`from X import Y`: This means "Go to the library/folder/file named **X** and bring the specific tool named **Y** into this file."

**Where do they come from?**
*   **`collections.abc`**: Built into Python itself (Standard Library).
*   **`starlette`**: An external library that FastAPI uses as its "engine."
*   **`fastapi`**: This is the library itself! It's importing other files within the same folder (like `routing.py`).

---

## 3. What is `Annotated`?
**Answer:** `Annotated` is like a **"Type with a Sticky Note."**

In line 94: `title: Annotated[str, Doc("...")]`
*   **The Type** is `str` (the title must be text).
*   **The Sticky Note** is `Doc(...)`.

FastAPI uses these sticky notes to automatically build your documentation page (`/docs`). The code runs fine without them, but the sticky notes tell the documentation generator what to say about each variable.

---

## 4. What is happening in the First 50 lines in simple terms?
**Answer:** At its simplest, the `FastAPI` class is the **"Manager"** of your web application. When you write `class FastAPI(Starlette):`, you are building a manager that:

*   **Inherits** from an older manager named `Starlette` (so it already knows how to handle basic web requests).
*   **Organizes** your routes (the URLs people visit).
*   **Handles Mistakes**: It knows what to do if someone sends bad data (Error Handling).
*   **Generates Docs**: It automatically writes a manual (the `/docs` page) for your API based on those "Sticky Notes" (`Annotated`) we discussed!

When you do `app = FastAPI()`, you are hiring this manager to run your project.

---

## 5. What is `self` (Line 58)?
**Answer:** Think of `self` as the word **"Me"** or **"Myself."**

In Python classes, every function needs to know which specific object it is working on. When you do `app = FastAPI()`, the `__init__` function runs. Inside that function, `self` refers to that specific `app` you just created. It allows the manager (the class) to keep track of its own settings, like "My name is FastAPI" or "My debug mode is off."

---

## 6. What is the star `*` (Line 59)?
**Answer:** The `*` is a **"Border Guard."**

It tells Python: "Every setting after this point **MUST** be named explicitly."
*   **Without the star**: You could write `FastAPI(True)`.
*   **With the star**: You **must** write `FastAPI(debug=True)`.

This is a safety feature. Because FastAPI has dozens of settings, the developers use the `*` to force you to be clear about which setting you are changing.

---

## 7. What are `debug`, `routes`, etc.?
**Answer:** These are **Parameters** (settings) for the manager.

*   **`debug`**: If set to `True`, the manager will show you very detailed (and sometimes scary) error messages to help you fix bugs.
*   **`routes`**: This is a list of all the "roads" (URLs) in your web app.

---

## 8. Are these "Lists" because of the square brackets `[]`?
**Answer:** You are half-right! In Python, square brackets are used for two different things:

1.  **Creating Data**: `my_list = ["apple", "banana"]` (This is a real list of items).
2.  **Type Hinting (The "Recipe")**: In lines like `list[BaseRoute]`, the brackets are used to describe a **Recipe**.
    *   `list[BaseRoute]` means: "This setting must be a **List** that contains **BaseRoute** objects."
    *   `Annotated[str, Doc(...)]` means: "This setting must be **Text** (`str`), and here is some **Documentation** (`Doc`) about it."

**Summary**: When you see `[]` inside the `def __init__(...)` section, it's usually part of the **Type Hint** (the rules for what data is allowed). When you see `[]` in your own code like `tags = ["users"]`, that's usually the **Data** itself!

---

# Day 2: Advanced Python Patterns

## 9. What are Context Managers (`with` statement)?
**Answer:** Think of them as a **"Safety Sandwich"** or the **"Automatic Fridge."**

*   **Analogy**: When you cook, you have to remember to put the milk back in the fridge. If you forget, it spoils. A Context Manager is like a fridge that automatically opens when you reach for milk and closes the moment you're done.
*   **How it works**: 
    *   `__enter__`: The "Setup" (Opening the fridge).
    *   `__exit__`: The "Cleanup" (Closing the fridge automatically).
*   **Real-World Example**: **Database Connections**. You open a connection, run your query, and the Context Manager ensures the connection is closed even if your code crashes. This prevents "Database Leaks."

---

## 10. What are Generators (`yield`)?
**Answer:** Think of this as the **"Buffet vs. Waiter"** approach.

*   **Analogy**: 
    *   **List (Buffet)**: You prepare ALL the food and put it on the table at once. It takes a lot of space (Memory) and prep time.
    *   **Generator (Waiter)**: The waiter brings you one small plate at a time. You finish one, and they bring the next. This takes very little space (Memory) because you only have one plate at a time.
*   **How it works**: The `yield` keyword **pauses** the function and hands over one piece of data. The function resumes only when the next piece is requested.
*   **Real-World Example**: **Streaming a 2GB file**. Instead of loading the whole 2GB into your RAM (which might crash your computer), a Generator "yields" small chunks of the file to the user's browser one by one.

---

# Linear Algebra for ML

## 11. What is a Vector and how is it represented in space?
**Answer:** A vector is the fundamental building block of Linear Algebra. You can think of it in three ways:
1.  **The Physics View**: An **arrow** pointing in space that has a specific **length** and **direction**.
2.  **The Computer Science View**: An **ordered list of numbers** (like `[7, 3]`).
3.  **The Visual View**: On a grid, a vector is an arrow that starts at the **origin (0,0)** and ends at a specific coordinate. 

*   **Example**: A vector `[4, 2]` tells you to move 4 steps to the right and 2 steps up.

## 12. How is a Vector represented on a graph in an ML application?
**Answer:** In Machine Learning, we use vectors to represent **"Features"** or traits of data. Each axis on the graph represents a different piece of information.

*   **Real-World Example (House Pricing)**:
    *   **Axis X**: Square footage of the house.
    *   **Axis Y**: Number of bedrooms.
    *   If a house has 2000 sq ft and 3 bedrooms, it becomes a **Vector**: `[2000, 3]`.
*   **On the Graph**: This house is represented as a single **point** (or an arrow pointing to that point) in a 2D space. 
*   **The Power of ML**: By representing data as vectors, a computer can use math to calculate the "distance" between two houses to see how similar they are!
