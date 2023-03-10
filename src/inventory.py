import collections

class Bag:
    def __init__(self):
        self.contents = []

    def __repr__(self):
        representation = "Bag:\n"
        representation += "====\n"
        for item, count in collections.Counter([item.__repr__() for item in self.contents]).items():
            representation += f"\t{item}: {count}"
            representation += "\n"
        return representation

    def put(self, item):
        self.contents.append(item)

class Item:
    pass

class FiniteItem(Item):
    pass

class InfiniteItem(Item):
    pass

class Box(FiniteItem):
    def __init__(self):
        self.descriptor = "Box"
    def __repr__(self):
        return self.descriptor

class SecondBox(FiniteItem):
    def __init__(self):
        self.descriptor = "Second Box"
    def __repr__(self):
        return self.descriptor
