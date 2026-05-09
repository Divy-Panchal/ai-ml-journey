# Day 2: Understanding Python Generators
# Key Concept: 'yield' allows a function to return data one piece at a time.

# 1. Without generator (loads everything into memory)
def count_to_5_list():
    print("--- List Version: Preparing ALL data... ---")
    result = []
    for i in range(1, 6):
        result.append(i)
    return result

print("Starting List Loop:")
for num in count_to_5_list():
    print(f"Got: {num}")
# Result: The list is fully built in memory before the loop even starts.


# 2. With generator (lazy loading)
def count_to_5_generator():
    print("--- Generator Version: Preparing data ONE BY ONE... ---")
    for i in range(1, 6):
        yield i  # <--- This PAUSES the function and returns 'i'

print("\nStarting Generator Loop:")
for num in count_to_5_generator():
    print(f"Got: {num}")
# Result: 'i' is generated only when the loop asks for the next number.


# 3. Real-world example: Reading a large file line by line
# Imagine a file with 10 million lines. You CANNOT load it all at once.
def read_large_file(filepath):
    with open(filepath, "r") as file:
        for line in file:
            yield line.strip()

# This is very memory efficient:
# for line in read_large_file("huge_data.txt"):
#     process(line)


# --- Why this matters for FastAPI ---
# FastAPI uses generators for "Streaming Responses."
# If you are sending a 2GB file to a user, FastAPI doesn't load 
# the 2GB into your RAM. Instead, it "yields" small chunks of the 
# file to the user's browser one by one!
