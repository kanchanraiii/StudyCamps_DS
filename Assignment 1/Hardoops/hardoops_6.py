class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def eat(self):
        return f"{self.name} the {self.species} is eating."
    
    def sleep(self):
        return f"{self.name} the {self.species} is sleeping."
class Mammal(Animal):
    def __init__(self, name, species, age, is_warm_blooded=True):
        super().__init__(name, species, age)
        self.is_warm_blooded = is_warm_blooded
    
    def nurse(self):
        return f"{self.name} the {self.species} is nursing its young."

class Bird(Animal):
    def __init__(self, name, species, age, can_fly=True):
        super().__init__(name, species, age)
        self.can_fly = can_fly
    
    def lay_eggs(self):
        return f"{self.name} the {self.species} is laying eggs."
    
    def fly(self):
        if self.can_fly:
            return f"{self.name} the {self.species} is flying."
        else:
            return f"{self.name} the {self.species} cannot fly."

class Reptile(Animal):
    def __init__(self, name, species, age, is_cold_blooded=True):
        super().__init__(name, species, age)
        self.is_cold_blooded = is_cold_blooded
    
    def crawl(self):
        return f"{self.name} the {self.species} is crawling."
class ZooKeeper:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def take_care_of(self, animal):
        return f"Zookeeper {self.name} is taking care of {animal.name} the {animal.species}."
    
    def feed_animal(self, animal):
        return f"Zookeeper {self.name} is feeding {animal.name} the {animal.species}."
    
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.zookeepers = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
        return f"{animal.name} the {animal.species} has been added to the zoo."
    
    def remove_animal(self, animal_name):
        for animal in self.animals:
            if animal.name == animal_name:
                self.animals.remove(animal)
                return f"{animal.name} the {animal.species} has been removed from the zoo."
        return f"No animal named {animal_name} found in the zoo."
    
    def assign_zookeeper(self, zookeeper):
        self.zookeepers.append(zookeeper)
        return f"Zookeeper {zookeeper.name} has been assigned to the zoo."
    
    def generate_report(self):
        report = f"Zoo Report for {self.name}:\n"
        report += "Animals:\n"
        for animal in self.animals:
            report += f"- {animal.name} the {animal.species}, Age: {animal.age}\n"
        report += "Zookeepers:\n"
        for zookeeper in self.zookeepers:
            report += f"- {zookeeper.name}, Employee ID: {zookeeper.employee_id}\n"
        return report
# Creating animals
lion = Mammal("Leo", "Lion", 5)
eagle = Bird("Eddie", "Eagle", 3)
snake = Reptile("Slyther", "Snake", 2)

# Creating a zookeeper
zookeeper = ZooKeeper("John", "ZK001")

# Creating a zoo and adding animals and zookeepers
zoo = Zoo("Wildlife Park")
print(zoo.add_animal(lion))
print(zoo.add_animal(eagle))
print(zoo.add_animal(snake))

print(zoo.assign_zookeeper(zookeeper))

# Zookeeper taking care of animals
print(zookeeper.take_care_of(lion))
print(zookeeper.feed_animal(eagle))

# Generating a zoo report
print(zoo.generate_report())

# Removing an animal
print(zoo.remove_animal("Slyther"))

# Generating the report again
print(zoo.generate_report())

