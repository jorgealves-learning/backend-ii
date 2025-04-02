# Backend II
## Session 1: Fundamentals of Big O Notation in Python Performance

**Goal:**
Understand how algorithm complexity is measured with Big O notation and why it matters for performance in Python.

**Definition:**
Big O notation expresses the upper bound of an algorithm’s runtime relative to its input size. It helps you compare algorithms and identify potential bottlenecks. Use cases include analysing search, sort, or any iterative processes. In Python, knowing Big O is essential for writing efficient code when dealing with large datasets.

**Documentation Reference:**
- https://docs.python.org/3/tutorial/datastructures.html
- https://en.wikipedia.org/wiki/Big_O_notation
- https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/

### Tutorial:

- Write a simple linear search function:
```py
def linear_search(lst, target):
    for item in lst:
        if item == target:
            return True
    return False
```
- Explanation: This function’s runtime grows linearly with the size of the list, hence O(n).

- Comparison: Briefly discuss how a binary search (O(log n)) differs in performance.

### Exercise:

- Problem: Write a recursive function to calculate factorial and determine its time complexity.
- Steps to Solve:
    - Define the recursive factorial function.
    - Analyse how many times the function is called relative to the input.

### Challenge:

- Problem: Optimise a bubble sort algorithm so that it stops early if the list is already sorted.
> Hint: Use a flag to detect whether a swap occurred.

## Session 2: Implementing Design Patterns in Python for Robust Architecture

**Goal:**
Learn key design patterns and how to implement them in Python to build maintainable and robust applications.

**Definition:**
Design patterns are standard solutions to common software design problems. They promote reusability and cleaner code structure. Use cases include managing shared resources (Singleton), abstracting object creation (Factory), and handling events (Observer). Mastery of these patterns leads to clearer communication among developers and more scalable applications.

**Documentation Reference:**
- https://refactoring.guru/design-patterns/python
- https://www.tutorialspoint.com/python_design_patterns/index.htm
- https://realpython.com/design-patterns-python/

### Tutorial:
- Introduction to Singleton: Explain why you might need only one instance of a class.
```py
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)
```
- Explanation: Both instances refer to the same object.
- Discussion: Briefly mention other patterns (Factory, Observer) for context.

### Exercise:

- Problem: Implement the Factory pattern to create shape objects (e.g., Circle and Square).

- Steps to Solve:
    - Define an abstract Shape class.
    - Create concrete classes for Circle and Square.
    - Write a factory function to return the correct object.

### Challenge:

- Problem: Implement the Observer pattern to notify multiple observers when a subject’s state changes.
- Hint: Create a Subject class that maintains a list of observers.

## Session 3: Mastering Multi-threading in Python

**Goal:**
Learn how to run code concurrently using threads to improve performance for I/O-bound tasks.

**Definition:**
Multi-threading splits a program into multiple threads running in parallel. In Python, this is ideal for I/O-bound operations because threads share the same memory space. Use cases include network operations, file I/O, and handling multiple user requests. Despite the Global Interpreter Lock (GIL), multi-threading remains effective for many practical scenarios.

**Documentation Reference:**
- https://docs.python.org/3/library/threading.html
- https://realpython.com/intro-to-python-threading/
- https://www.tutorialspoint.com/python/python_multithreading.htm

### Tutorial:

- Introduction: Explain the threading module.

```py
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```
- Explanation: This runs the print_numbers function in a separate thread.
- Discussion: Mention when to use threads (e.g., I/O-bound tasks).

### Exercise:

- Problem: Create two threads that print letters and numbers concurrently.
- Steps to Solve:
    - Define two functions—one for letters and one for numbers.
    - Create and start a thread for each function.

### Challenge:

- Problem: Create a multi-threaded program that downloads multiple files concurrently from given URLs.
- Hint: Use the threading module along with urllib.request.urlretrieve.


## Session 4: Multi-processing in Python for Scalability
**Goal:**
Understand how to run tasks concurrently in separate processes to boost performance in CPU-bound tasks.

**Definition:**
Multi-processing uses separate processes with their own memory space, bypassing the Global Interpreter Lock (GIL). This technique is ideal for CPU-intensive tasks such as heavy computations or large data processing, where parallel execution on multiple cores can lead to significant speed improvements. It is commonly used in scenarios that require isolated execution environments.

**Documentation Reference:**

- https://docs.python.org/3/library/multiprocessing.html
- https://realpython.com/python-multiprocessing/
- https://www.geeksforgeeks.org/multiprocessing-python-set-1/

**Tutorial:**
- Introduction: Explain the difference between threading and multi-processing.
- Step-by-Step Example:
    - Import the multiprocessing module.
    -  Define a simple function (e.g., compute a square).
    - Create and start multiple processes.
```py
import multiprocessing
import time

def compute_square(n):
    time.sleep(1)  # Simulate a heavy computation
    print(f"Square of {n} is {n*n}")

if __name__ == "__main__":
    numbers = [2, 3, 4, 5]
    processes = []
    for number in numbers:
        p = multiprocessing.Process(target=compute_square, args=(number,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

```
- Explanation: Each process runs independently, and joining ensures all complete before the script ends.

### Exercise:

- Problem: Create a program that concurrently computes the factorial of several numbers using multi-processing.
- Steps to Solve:
    - Define a recursive factorial function.
    - Spawn a process for each number in a list.

### Challenge:

- Problem: Create a multi-process program that divides a large list of numbers into sublists and computes the sum of squares for each sublist concurrently.
- Hint:
  Use the Pool class from the multiprocessing module.
