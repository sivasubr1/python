class CountUpIterable:
    def __init__(self, start, end):
        self.start, self.end = start, end

    def __iter__(self):
        return CountUpIterator(self.start, self.end)


class CountUpIterator:
    def __init__(self, current, end):
        self.current, self.end = current, end

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1

        return value

counter = CountUpIterable(1, 3)
print(list(counter))
print(list(counter))

