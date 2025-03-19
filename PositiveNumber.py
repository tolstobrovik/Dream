class PositiveNumber:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        x = instance.__dict__.get(self.name)
        return x

    def __set__(self, instance, value: str):
        if all(k.isdigit() for k in value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError("It is not digit")


class Number:
    num_create = PositiveNumber("number")

number = Number()
number.num_create = "998991234567"
print(number.num_create)