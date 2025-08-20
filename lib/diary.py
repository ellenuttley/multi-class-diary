from .diary_entry import DiaryEntry
from .todo_list import TodoList
# from diary_entry import DiaryEntry
# from todo_list import TodoList

class Diary:
    def __init__(self):
        self.full_diary = []
        self.todo_list = TodoList()
        self.contacts = set()

    def add(self, entry):
        self.full_diary.append(entry)
        self._extract_contacts(entry)
        self._extract_todos(entry)

    def _extract_contacts(self, entry):
        if '0' in entry.contents:
            index = entry.contents.find('0')
            slice = entry.contents[index:index + 11]
            if slice.isdigit():
                self.contacts.add(slice)

    def _extract_todos(self, entry):
        if '#todo' in entry.contents:
            index = entry.contents.find('#todo')
            slice = entry.contents[index + 6:]
            self.todo_list.add(slice)

    def read_diary(self):
        if len(self.full_diary) == 0:
            raise Exception('Theres nothing to read!')
        
        formatted_diary = []
        for entry in self.full_diary:
            formatted_diary.append(entry.format())

        return '\n'.join(formatted_diary)
    
    def all(self):
        return self.full_diary

    def count_words(self):
        total = 0
        for entry in self.full_diary:
            total += entry.count_words()
        return total

    def reading_time(self, wpm):
        word_count = self.count_words()
        word_time = 60 / wpm

        total_seconds = word_count * word_time
        return int(total_seconds // 60)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        for entry in self.all():
            if entry.reading_time(wpm) == minutes:
                return entry
        
        sorted_diary = sorted(self.all(), key=lambda x: x.reading_time(wpm), reverse=True)

        if sorted_diary[-1].reading_time(wpm) > minutes:
            raise Exception("No Appropriate Entry for Time Available")
        
        for entry in sorted_diary:
            if entry.reading_time(wpm) > minutes:
                continue
            else:
                return entry


# def load_diary():
#     with open('diary.txt', 'r') as file:
#         return file.read()

# def load_diary_100():
#     with open('diary_100.txt', 'r') as file:
#         return file.read()

# def load_diary_200():
#     with open('diary_200.txt', 'r') as file:
#         return file.read()
    
# diary_contents = str(load_diary())
# diary_100 = str(load_diary_100())
# diary_200 = str(load_diary_200())

diary = Diary()
# # diary_entry_1 = DiaryEntry('300 Word Entry', f'{diary_100} {diary_200}' )
# # diary_entry_2 = DiaryEntry('400 Word Entry', f'{diary_200} {diary_200}')
# # diary_entry_3 = DiaryEntry('1000 Word Entry', diary_contents)
# # diary_entry_4 = DiaryEntry('800 Word Entry', f'{diary_200} {diary_200} {diary_200} {diary_200}')
# # diary_entry_5 = DiaryEntry('500 Word Entry', f'{diary_200} {diary_200} {diary_100}')
# # diary.add(diary_entry_1)
# # diary.add(diary_entry_2)
# # diary.add(diary_entry_3)
# # diary.add(diary_entry_4)
# # diary.add(diary_entry_5)

# entry_contact = DiaryEntry("Contact", "Call 07123456789")
entry_todo = DiaryEntry("Todo", "Another busy day #todo Finish report")
# diary.add(entry_contact)
diary.add(entry_todo)

# # for item in diary.all():
# #     print(str(item.title), str(item.contents))
# # print(diary.find_best_entry_for_reading_time(100, 6))