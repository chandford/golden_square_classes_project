# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.


As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskTracker:

    def __init__(self):
        # self.tasks
        #   empty list for storing tasks
        pass 

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing (optional print statement => f"Task added: {task}.")
        # Side-effects
        #   Saves the task to the self object "self.tasks"
        pass

    def remove_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing (optional print statement => f"Task removed: {task}.")
        # Side-effects:
        #   Removes specified task from self object "self.tasks"
        #   Throws exception if no task found
        pass 
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given no tasks
TaskTracker's tasks attribute is empty
"""
tracker = TaskTracker()
tracker.tasks # => []

"""
Given a task
add_task saves task to task list
"""
tracker = TaskTracker()
tracker.add_task("Walk the dog") # => tracker.tasks == ["Walk the dog"]
tracker.add_task("Water the plants") # => tracker.tasks == ["Walk the dog", "Water the plants"]

"""
Given a task
remove_task removed specific task from task list
"""
tracker = TaskTracker()
tracker.add_task("Walk the dog") # => tracker.tasks == ["Walk the dog"]
tracker.add_task("Water the plants") # => tracker.tasks == ["Walk the dog", "Water the plants"]
tracker.remove_task("Walk the dog") # => tracker.tasks == ["Water the plants"]

"""
Given a task not in the task list
remove_task raises an exception
"""
tracker = TaskTracker()
tracker.add_task("Walk the dog") # => tracker.tasks == ["Walk the dog"]
tracker.remove_task("Water the plants") # => raises an error with the message "No task set."

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
