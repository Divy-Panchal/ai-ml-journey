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
