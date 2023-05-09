import numpy as np

class node:
    def __init__(self, data):
        self.data = data
        self.link = None

    def __str__(self) -> str:
        return (f'{self.data}')

    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_link(self, link):
        self.link = link

    def get_link(self):
        return self.link
    
class linkedList:
    def __init__(self, data = []):
        data = np.array(data)
        self.length = len(data)

        if len(data) > 0:
            self.head = node(data[0])

            focus = self.head

            for i in data[1:]:
                tmp = node(i)
                focus.set_link(tmp)
                focus = focus.get_link()

            self.tail = focus
        else:
            self.head = None
            self.tail = None

    def __str__(self) -> str:
        result = []
        focus = self.head

        while focus:
            result.append(focus.get_data())
            focus = focus.get_link()

        return str(result)
    
    def append(self, data):
        tmp = node(data)
        self.tail.set_link(tmp)
        self.tail = tmp
        self.length += 1
    