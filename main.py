class Number:
    def __init__(self, value):
        self.value = value

    # Addition (+)
    def __add__(self, other):
        return Number(self.value + other.value)

    # Division (/)
    def __truediv__(self, other):
        return Number(self.value / other.value)

    # In-place subtraction (-=)
    def __isub__(self, other):
        self.value -= other.value
        return self

    # Representation
    def __repr__(self):
        return f"Number({self.value})"


# Test the methods
n1 = Number(10)
n2 = Number(5)

# __add__
add_result = n1 + n2
print("Addition:", add_result)

# __truediv__
div_result = n1 / n2
print("Division:", div_result)

# __isub__
n1 -= n2
print("After -= :", n1)

# __repr__
print("Representation:", repr(n1))