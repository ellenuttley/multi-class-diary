class DiaryEntry:
    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents
    
    def format(self):
        return f'{self.title}: {self.contents}'

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        word_count = self.count_words()
        word_time = 60 / wpm

        total_seconds = word_count * word_time
        return int(total_seconds // 60)

