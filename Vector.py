class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __len__(self):
        return 2


v1 = Vector(2, 4)
v2 = Vector(1, 1)

print(v1 + v2)
print(v1 == Vector(2, 4))
