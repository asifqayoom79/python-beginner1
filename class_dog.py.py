#Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color
class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def special_ability(self):
        print(f"{self.name} can jump really high!")

    def temperament(self):
        print(f"{self.name} is known for its energetic and playful temperament.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def special_ability(self):
        print(f"{self.name} can jump really high!")

    def temperament(self):
        print(f"{self.name} is known for its calm and friendly temperament.")


# dog
name = input("Enter the dog's name: ")
age = int(input("Enter the dog's age: "))
coat_color = input("Enter the dog's coat color: ")
dog = Dog(name, age, coat_color)

dog.description()
dog.get_info()


# Jack Russel Terrier
name = input("Enter the Jack Russell Terrier's name: ")
age = int(input("Enter the Jack Russell Terrier's age: "))
coat_color = input("Enter the Jack Russell Terrier's coat color: ")

jack_russell = JackRussellTerrier(name, age, coat_color)

jack_russell.description()
jack_russell.get_info()
jack_russell.special_ability()
jack_russell.temperament()


# Bulldog
name = input("Enter the Bulldog's name: ")
age = int(input("Enter the Bulldog's age: "))
coat_color = input("Enter the Bulldog's coat color: ")

bulldog = Bulldog(name, age, coat_color)

bulldog.description()
bulldog.get_info()
bulldog.special_ability()
bulldog.temperament()
