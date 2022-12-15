# Need to create a Human class with attributes: name, surname, age, phone, address
# Attributes must be filled in the __init__ method
# You also need to write methods:
#
# get_info(self) - which returns a dictionary containing information about the person
# call(self, phone_number) - which will output "{self.phone} calling {phone_number}"
# You need to create 3 objects of the Human class and call the get_info method on them


class Human:

    def __init__(self, name: str, surname: str, age: int, phone: str, address: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        human_info = {
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'phone': self.phone,
            'address': self.address,
            }
        return human_info

    def call(self, phone_number):
        print(f'{self.phone} calling {phone_number}')


info1 = Human('Bob', 'Dylan', 45, '+981234567890', 'Fulton St. 654')
info2 = Human('Jim', 'Carrie', 59, '+380234342313', 'Lafayette Av. 12')
info3 = Human('Mishel', 'Pfeiffer', 23, '+86783451242', 'St. Marks Pl. 1')
print(info1.get_info())
print(info2.get_info())
print(info3.get_info())

