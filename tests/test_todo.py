from lib.todo import *
import pytest

def test_todo_functional():
    todo = Todo('Do a task')
    assert(todo)

def test_todo_initialises_with_task():
    todo = Todo('Do a task')
    assert todo.task == 'Do a task'

def test_todo_initialises_task_incomplete():
    todo = Todo('Do a task')
    assert todo.complete == False

def test_todo_mark_complete_marks_task_complete():
    todo = Todo('Do a task')
    todo.mark_complete()
    assert todo.complete == True

def test_todo_mark_complete_if_task_already_complete_throw_error():
    todo = Todo('Do a task')
    todo.mark_complete()
    with pytest.raises(Exception) as err:
        todo.mark_complete()
    error_message = str(err.value)
    assert error_message == 'This task is already done!'

# def test_todo_():
#     pass

# def test_todo_():
#     pass