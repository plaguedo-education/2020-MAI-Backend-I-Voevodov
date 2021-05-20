from collections import OrderedDict

class LRUCache():

    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self.ordered_dict = OrderedDict()

    def get(self, key: str) -> str:        
        return self.ordered_dict.get(key) or ''

    def set(self, key: str, value: str) -> None:
        if len(self.ordered_dict) >= self.capacity:
            self.ordered_dict.popitem(last=False)
        self.ordered_dict[key] = value

    def rem(self, key: str) -> None:
        del self.ordered_dict[key]
        