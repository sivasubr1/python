class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        return Money(self.amount + other.amount)

    def __repr__(self):
        return f"Money({self.amount})"


print(Money(10) + Money(5))

