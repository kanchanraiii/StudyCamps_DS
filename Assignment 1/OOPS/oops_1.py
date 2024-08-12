
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = 2024  
        birth_year = int(self.date_of_birth.split("-")[0])  
        age = today - birth_year
        return age

person = Person("Kanchan Rai", "India", "2005-01-22")
print(f"{person.name} is {person.calculate_age()} years old.")
