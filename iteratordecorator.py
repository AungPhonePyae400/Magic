# iterator + decorator in same file

# ---------- Iterator ----------
class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


# ---------- Decorator ----------
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


# ---------- Testing ----------
print("Iterator output:")
nums = NumberIterator([1, 2, 3])
for n in nums:
    print(n)

print("\nDecorator output:")
say_hello()
