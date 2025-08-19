# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

┌──────────────────────────────┐
│ Diary                        │
│                              │
│ - all_entries                │
│ - contacts                   │
│ - todo_list (ToDoList)       │
│                              │
│ + add(entry)                 │
│ + read_diary()               │
│ + select_entry(wpm, minutes) │
│ + all_contacts()             │
└──────────────┬───────────────┘
               │
               │ owns a list of
               ▼
┌─────────────────────────┐      ┌───────────────────────┐
│ DiaryEntry              │      │ ToDoList              │
│                         │      │                       │
│ - title                 │      │ - full_list           │
│ - contents              │      │ - diary (backref)     │
│                         │      │                       │
│ + format()              │      │ + add(todo)           │
│ + count_words()         │      │ + completed()         │
│ + reading_time(wpm)     │      │ + incomplete()        │
└─────────────────────────┘      │ + give_up()           │
                                 └─────────┬─────────────┘
                                           │
                                           │ owns a list of
                                           ▼
                                 ┌───────────────────────┐
                                 │ ToDo                  │
                                 │                       │
                                 │ - task                │
                                 │ - complete            │
                                 │                       │
                                 │ + mark_complete()     │
                                 └───────────────────────┘

```

_Also design the interface of each class in more detail._

```python
class Diary:
    # User-facing properties:
    #   all_entries: list of instances of DiaryEntry
    #   todo_list: ToDoList objects
    #   contacts: list of phone numbers

    def __init__(self):
        pass # No code here yet

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Side-effects:
        #   Adds the entry to the self.all_entries list
        #   -uses helper function to extract phone number, and add to contacts
        #   -uses helper function to extract todos, and add to todo list 
    
    def _extract_contacts(self, entry):
        # helper function
        #   scans the entry for a phone number, based on a pattern
        #   if it finds a number, it adds it to the contacts list

    def _extract_todos(self, entry):
        # helper function
        #   scans the entry for a todo, based on a pattern
        #   if it finds a todo, it creates a Todo object and adds it to list

    def read_diary(self):
        # Returns:
        #   A formatted list of all the entries in self.all_entries
        #   using the .format() method in DiaryEntry

    def select_entry(self, wpm, minutes):
        # Parameters:
        #   wpm: int representing how many words per minute can be read
        #   minutes: int representing how many minutes user has to read
        # Side-effects:
        #   returns the best entry to read given the wpm and how many minutes
        #   raises Exception, if no entry is appropriate 
        

class DiaryEntry:
    # User-facing properties:
    #   title: string
    #   contents: string

    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        # Side-effects:
        #   Sets the title and content properties

    def format(self):
        # Returns:
        #  A formatted string f'{title}: {contents}'
    
    def count_words(self):
        # Returns : int count of words in entry
    
    def reading_time(self, wpm):
        # Parameters:
        #   wpm: (words per minute) int
        # Returns: int, minutes required to read

class Todo:
    def __init__(self, task):
        # Parameters:
        #   task: string
        #   complete: bool
        # Side-effects:
        #   Sets the task and sets complete to False
    
    def mark_complete(self):
        # set complete to True
        # if complete is already True, throws an error

class ToDoList:
    def __init__(self):
        # full_list = list of all the todos
        # Side-effects:
        #   Sets the full_list as empty list
    
    def add(self, todo):
        # appends todo to the full_list
    
    def complete(self):
        # return list of completed tasks
    
    def incomplete(self):
        # return list of incompleted tasks
    
    def give_up(self):
        # mark all tasks as complete

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

## 4. Create Examples as Unit Tests

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
