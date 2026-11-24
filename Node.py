import gc

class Node:
    def __init__(self):
        self.other = None


a, b = Node(), Node()

a.other = b
b.other = a

del a, b

gc.collect()

