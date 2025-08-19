from lib.todo import *
from lib.todo_list import *
from lib.diary import *
from lib.diary_entry import *
import pytest

def load_diary():
    with open('diary.txt', 'r') as file:
        return file.read()

def load_diary_100():
    with open('diary_100.txt', 'r') as file:
        return file.read()

def load_diary_200():
    with open('diary_200.txt', 'r') as file:
        return file.read()
    
diary = str(load_diary())
diary_100 = str(load_diary_100())
diary_200 = str(load_diary_200())

def test_diary_adds_diary_entry():
    diary = Diary()
    diary_entry = DiaryEntry('title', 'contents')
    diary.add(diary_entry)
    assert diary.full_diary[0] == diary_entry

def test_diary_all_returns_all_entries():
    diary = Diary()
    diary_entry = DiaryEntry('title_1', 'contents_1')
    diary_entry_2 = DiaryEntry('title_2', 'contents_2')
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    assert diary.all() == [diary_entry, diary_entry_2]

def test_diary_count_words_returns_int():
    diary = Diary()
    diary_entry = DiaryEntry('title_1', 'this is the first')
    diary_entry_2 = DiaryEntry('title_2', 'and second')
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    assert type(diary.count_words()) == int

def test_diary_count_words_accurate():
    diary = Diary()
    diary_entry = DiaryEntry('title_1', 'this is the first')
    diary_entry_2 = DiaryEntry('title_2', 'and second')
    diary.add(diary_entry)
    diary.add(diary_entry_2)
    assert diary.count_words() == 6

def test_diary_reading_time_returns_int():
    diary = Diary()
    diary_entry = DiaryEntry('title', 'contents')
    assert type(diary.reading_time(1)) == int

def test_diary_reading_time_accurate():
    diary = Diary()
    diary_entry_100 = DiaryEntry('100 Word Sample', diary_100)
    diary_entry_200 = DiaryEntry('200 Word Sample', diary_200)
    diary.add(diary_entry_100)
    diary.add(diary_entry_200)
    assert diary.reading_time(100) == 3

def test_diary_find_best_entry_for_reading_time_exact_match():
    diary = Diary()
    diary_entry_100 = DiaryEntry('100 Word Sample', diary_100)
    diary_entry_200 = DiaryEntry('200 Word Sample', diary_200)
    diary.add(diary_entry_100)
    diary.add(diary_entry_200)
    assert diary.find_best_entry_for_reading_time(100, 1) == diary_entry_100

def test_diary_find_best_entry_for_reading_time_error_no_appropriate_entry():
    diary = Diary()
    diary_entry_100 = DiaryEntry('100 Word Sample', diary_100)
    diary.add(diary_entry_100)
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(50, 1)
    error_message = str(err.value)
    assert error_message == "No Appropriate Entry for Time Available"

def test_diary_find_best_entry_for_reading_time__not_exact_match():
    diary = Diary()
    diary_entry_100 = DiaryEntry('100 Word Sample', diary_100)
    diary_entry_200 = DiaryEntry('200 Word Sample', diary_200)
    diary.add(diary_entry_100)
    diary.add(diary_entry_200)
    assert diary.find_best_entry_for_reading_time(150, 1) == diary_entry_200

'''
As a user I want to add multiple tasks to a list
So that I have a list of tasks that I need to complete
'''
def test_todo_integration_():
    todo_list = TodoList()
    todo = Todo('Do a task')
    two_do = Todo('Do another task')
    todo_list.add(todo)
    todo_list.add(two_do)

    assert len(todo_list.incomplete()) == 2
    assert todo and two_do in todo_list.incomplete()

'''
As a user I want to mark my tasks as complete
So that I can track my progress
'''
def test_todo_integration_track_completed_tasks():
    todo_list = TodoList()
    todo = Todo('Do a task')
    two_do = Todo('Do another task')

    todo_list.add(todo)
    todo_list.add(two_do)

    todo.mark_complete()

    assert len(todo_list.complete()) == 1
    assert todo_list.complete() == [todo]

'''
As a user I want to see how many complete and incomplete tasks I have
So that I know what I have done, and what is left to do
'''
def test_todo_integration_track_complete_and_incomplete_tasks():
    todo_list = TodoList()

    todo = Todo('Do a task')
    two_do = Todo('Do another task')
    three_do = Todo('Do a different task')
    four_do = Todo('Do yet another task')

    todo_list.add(todo)
    todo_list.add(two_do)
    todo_list.add(three_do)
    todo_list.add(four_do)

    two_do.mark_complete()
    four_do.mark_complete()

    assert len(todo_list.complete()) == 2
    assert todo_list.complete() == [two_do, four_do]
    assert len(todo_list.incomplete()) == 2
    assert todo_list.incomplete() == [todo, three_do]

'''
As a user I want to mark all of my tasks as complete
So that I can start fresh on a new list
'''
def test_todo_integration_give_up_marks_all_complete():
    todo_list = TodoList()

    todo = Todo('Do a task')
    two_do = Todo('Do another task')
    three_do = Todo('Do a different task')
    four_do = Todo('Do yet another task')

    todo_list.add(todo)
    todo_list.add(two_do)
    todo_list.add(three_do)
    todo_list.add(four_do)

    todo_list.give_up()

    assert len(todo_list.incomplete()) == 0
    assert len(todo_list.complete()) == 4
    assert todo_list.complete() == [todo, two_do, three_do, four_do]

'''
As a user I want to see an error when I try and set an already complete task as complete
So that I know when a task is already done
'''
def test_todo_integration_error_thrown_for_already_complete_tasks():
    todo_list = TodoList()
    todo = Todo('Do a task')

    todo_list.add(todo)
    todo.mark_complete()

    with pytest.raises(Exception) as err:
        todo.mark_complete()
    error_message = str(err.value)
    assert error_message == 'This task is already done!'

'''
As a user I want my todo lists to work correctly, even when the list is empty
So that my application doesn't break when I have no tasks
'''
def test_todo_integration_todo_list_methods_can_be_used_empty_todo_list_no_errors():
    todo_list = TodoList()

    todo_list.give_up()

    assert len(todo_list.incomplete()) == 0
    assert len(todo_list.complete()) == 0