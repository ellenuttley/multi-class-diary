from lib.todo import *
from lib.todo_list import *

def test_todo_list_functional():
    todo_list = TodoList()
    assert(todo_list)

def test_todo_list_initialises_with_empty_list():
    todo_list = TodoList()
    assert todo_list.full_list == []

def test_todo_list_add_adds_todo_to_list():
    todo_list = TodoList()
    todo = Todo('Do a task')
    todo_list.add(todo)
    assert todo_list.full_list == [todo]

def test_todo_list_add_adds_multiple_todos_to_list():
    todo_list = TodoList()
    todo = Todo('Do a task')
    two_do = Todo('Do another task')
    todo_list.add(todo)
    todo_list.add(two_do)
    assert todo_list.full_list == [todo, two_do]

def test_todo_list_incomplete_returns_list():
    todo_list = TodoList()
    assert type(todo_list.incomplete()) == list

def test_todo_list_incomplete_returns_incomplete_tasks():
    todo_list = TodoList()
    todo = Todo('Do a task')
    todo_list.add(todo)
    assert todo_list.incomplete() == [todo]

def test_todo_list_complete_returns_list():
    todo_list = TodoList()
    assert type(todo_list.complete()) == list

def test_todo_list_complete_returns_complete_tasks():
    todo_list = TodoList()
    todo = Todo('Do a task')
    todo_list.add(todo)
    todo.mark_complete()
    assert todo_list.complete() == [todo]

def test_todo_list_give_up_marks_all_tasks_complete():
    todo_list = TodoList()
    todo = Todo('Do a task')
    two_do = Todo('Do another task')
    todo_list.add(todo)
    todo_list.add(two_do)
    todo_list.give_up()
    assert len(todo_list.complete()) == len(todo_list.full_list)