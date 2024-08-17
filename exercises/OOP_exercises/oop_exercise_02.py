# Write a Python program to create a person class.
# Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.

from datetime import datetime, date


class Person:
    def __init__(self, name, country, birthDate):
        self.name = name
        self.country = country
        self.birthDate = birthDate
        self.age = self.getAge()

    def getAge(self):
        today = date.today()
        age = today.year - self.birthDate.year
        if today < date(today.year, self.birthDate.month, self.birthDate.day):
            age -= 1
        return age


name = input("Enter the person's name: ")
country = input("Enter the person's country: ")
birthDate = datetime.strptime(
    input("Enter the person's birth date (ex: dd/mm/yy): "), "%d/%m/%Y"
)

person1 = Person(name, country, birthDate)
print(
    "{} was born in {} in the year of {} and lived for {} years.".format(
        person1.name, person1.country, person1.birthDate.year, person1.age
    )
)
