class RecordNotes():
    def __init__(self, title, description):
        self._title = None
        self._description = None
        self._tags = None
        self.title = title
        self.description = description
        self.tags = title + " " + description

    @property
    def title(self):
        return self._title
    
    @property
    def description(self):
        return self._description
    
    @property
    def tags(self):
        return self._tags
    
    @title.setter
    def title(self, title):
        self._title = title

    @description.setter
    def description(self, description):
        self._description = description

    @tags.setter
    def tags(self, tags):
        tags_from_text = []
        substring = '#'
        substrings = tags.split(substring)
        
        print(f"substrings: {tags}")
        if len(tags) > 0:
            for item in substrings[1:]:
                temp_arr = item.split(" ")
                tags_from_text.append(temp_arr[0].strip())
                continue
        self._tags = tags_from_text
