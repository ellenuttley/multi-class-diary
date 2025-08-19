class TodoList:
    def __init__(self):
        self.full_list = []

    def add(self, todo):
        self.full_list.append(todo)

    def incomplete(self):
        return [task for task in self.full_list if task.complete == False]

    def complete(self):
        return [task for task in self.full_list if task.complete == True]

    def give_up(self):
        for task in self.full_list:
            task.mark_complete()

