    class Number:
        def calculate(self, a, b):
            return a + b

    class Multiply (Number):
        def calculate(self, a, b):
            return a * b

    class Add (Number):
        def calculate(self, a, b):
            return a + b

    numbers = [Number(), Multiply(), Add ()]

    for obj in numbers:
        print(obj. calculate(2, 3))
