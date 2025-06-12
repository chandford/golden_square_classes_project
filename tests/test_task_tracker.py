from lib.task_tracker import TaskTracker
import pytest

def test_tasktracker_has_empty_list_on_tasks_attribute():
    tracker = TaskTracker()
    assert tracker.tasks == []

def test_add_task_stores_single_task():
    tracker = TaskTracker()
    tracker.add_task("Walk the dog")
    assert tracker.tasks == ["Walk the dog"]
    tracker.add_task("Water the plants") # => tracker.tasks == ["Walk the dog", "Water the plants"]

def test_add_task_stores_multiple_tasks():
    tracker = TaskTracker()
    tracker.add_task("Walk the dog")
    tracker.add_task("Water the plants")
    tracker.add_task("Pack for trip")
    assert tracker.tasks == ["Walk the dog", "Water the plants", "Pack for trip"]

def test_remove_task_removes_single_task():
    tracker = TaskTracker()
    tracker.add_task("Walk the dog")
    tracker.add_task("Water the plants")
    tracker.remove_task("Walk the dog")
    assert tracker.tasks == ["Water the plants"]

def test_remove_task_removes_multiple_tasks():
    tracker = TaskTracker()
    tracker.add_task("Walk the dog")
    tracker.add_task("Water the plants")
    tracker.remove_task("Walk the dog")
    tracker.remove_task("Water the plants")
    assert tracker.tasks == []

def test_remove_task_raises_exception_if_task_not_in_list():
    tracker = TaskTracker()
    tracker.add_task("Walk the dog")
    with pytest.raises(Exception) as err: 
        tracker.remove_task("Water the plants")
    error_message = str(err.value)
    assert error_message == "Task not found."

def test_tasktracker_keeps_task_count():
    tracker = TaskTracker()
    assert tracker.task_count == 0
    tracker.add_task("Walk the dog")
    tracker.add_task("Water the plants")
    assert tracker.task_count == 2
    tracker.remove_task("Walk the dog")
    assert tracker.task_count == 1
