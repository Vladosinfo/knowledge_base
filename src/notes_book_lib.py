from collections import UserDict
from classes.record_notes import RecordNotes

class NotesBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, value):
        self.data[value.title] = value

        print("Notes has been added.")

    def search(self):
        for key, val in self.data.items():
            print(f"key: {key} | title: {val.title} | description: {val.description}")
    