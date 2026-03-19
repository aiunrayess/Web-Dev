
class Animal:
    """Base class representing a generic animal."""

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        return f"{self.name} makes a generic animal sound."

    def describe(self):
        return f"I am a {self.species} named {self.name}, {self.age} year(s) old."

    def __str__(self):
        return f"Animal(name={self.name}, age={self.age}, species={self.species})"


class Dog(Animal):
    """Child class representing a Dog, inherits from Animal."""

    def __init__(self, name, age, breed):
        super().__init__(name, age, species="Dog")
        self.breed = breed
        self.tricks = []

    def speak(self):
        return f"{self.name} says: Woof! Woof!"

    def learn_trick(self, trick):
        """Unique method: teach the dog a trick."""
        self.tricks.append(trick)
        return f"{self.name} learned a new trick: {trick}!"

    def show_tricks(self):
        if self.tricks:
            return f"{self.name}'s tricks: {', '.join(self.tricks)}"
        return f"{self.name} hasn't learned any tricks yet."

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"


class Cat(Animal):
    """Child class representing a Cat, inherits from Animal."""

    def __init__(self, name, age, indoor):
        super().__init__(name, age, species="Cat")
        self.indoor = indoor   
        self.lives_remaining = 9

    def speak(self):
        return f"{self.name} says: Meow~ Purrrr..."

    def lose_life(self):
        """Unique method: cats have 9 lives."""
        if self.lives_remaining > 0:
            self.lives_remaining -= 1
            return f"{self.name} lost a life! Lives remaining: {self.lives_remaining}"
        return f"{self.name} has no lives left!"

    def lifestyle(self):
        kind = "indoor" if self.indoor else "outdoor"
        return f"{self.name} is an {kind} cat."

    def __str__(self):
        lifestyle = "indoor" if self.indoor else "outdoor"
        return f"Cat(name={self.name}, age={self.age}, lifestyle={lifestyle})"
