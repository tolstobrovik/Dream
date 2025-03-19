class ValiFullName:
    # def __init__(self,fullnema):
    #     self.fullname = fullnema
    def __get__(self, instance, owner):
        return instance.__dict__.get("fullname", "")

    def __set__(self, instance, value):
        if isinstance(value, str) and " " in value:
            name, surname = value.split()
            if name[0].isupper() and surname[0].isupper():
                instance.__dict__["fullname"] = value
            else:
                raise ValueError("Ism va familiya katta harf bilan boshlanishi kerak!")
        else:
            raise ValueError("error")

class Pupils:
    fullname = ValiFullName()

user = Pupils()
user.fullname = "Asliddin Mamatov"
print(user.fullname)