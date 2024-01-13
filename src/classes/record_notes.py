class RecordNotes():
    def __init__(self, title, description):
        self._title = None
        self._description = None
        self._tags = []
        self.title = title
        self.description = description

    @property
    def title(self):
        return self._title
    
    @property
    def description(self):
        return self._description
    
    @property
    def tags(self):
        return self.tags
    
    @title.setter
    def title(self, title):
        self._title = title

    @description.setter
    def description(self, description):
        self._description = description

    @tags.setter
    def tags(self, tags):
        pass
        # for symbol in self.title:
        #     print si
        # self._tags = tags
