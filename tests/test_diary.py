from lib.diary import *
from lib.diary_entry import *
import pytest

def test_diary_functional():
    diary = Diary()
    assert(diary)

def test_diary_add_entry():
    diary = Diary()
    diary_entry = DiaryEntry('title', 'contents')
    diary.add(diary_entry)

    assert len(diary.full_diary) == 1
    assert diary.full_diary[0] == diary_entry

def test_diary_add_helper_extracts_contact():
    diary = Diary()
    entry_contact = DiaryEntry("Contact", "Call 07123456789")
    diary.add(entry_contact)
    assert '07123456789' in diary.contacts

def test_diary_add_helper_extracts_todo():
    diary = Diary()
    entry_todo = DiaryEntry("Todo", "Another busy day #todo Finish report")
    diary.add(entry_todo)
    assert 'Finish report' in diary.todo_list.full_list

def test_diary_add_helper_extracts_multiple_todos():
    diary = Diary()
    entry_todo = DiaryEntry("Todo", "Need to #todo walk cat")
    entry_todo2 = DiaryEntry("Todo2", "Also #todo do dishwasher")
    diary.add(entry_todo)
    diary.add(entry_todo2)
    assert 'walk cat' and 'do dishwasher' in diary.todo_list.full_list

def test_diary_read_diary_single_entry():
    diary = Diary()
    diary_entry = DiaryEntry('this title', 'this is the contents')
    diary.add(diary_entry)
    assert diary.read_diary() == diary_entry.format()

def test_diary_read_diary_throws_error_no_entries():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.read_diary()
    error_message = str(err.value)
    assert error_message == 'Theres nothing to read!'

# def test_diary_():
#     diary = Diary()


# entry_contact = DiaryEntry("Contact", "Call 07123456789")
# entry_todo = DiaryEntry("Todo", "Another busy day #todo Finish report")
# diary.add(entry_contact)
# diary.add(entry_todo)
# def test_diary_():
#     diary = Diary()

# def test_diary_():
#     diary = Diary()