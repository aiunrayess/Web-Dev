
from models import Animal, Dog, Cat


def print_section(title):
    print(f"\n{'='*50}")
    print(f"  {title}")
    print(f"{'='*50}")


def main():

    print_section("Creating Animals")

    generic_animal = Animal(name="Unknown", age=3, species="Reptile")
    dog1 = Dog(name="Rex", age=5, breed="German Shepherd")
    dog2 = Dog(name="Buddy", age=2, breed="Golden Retriever")
    cat1 = Cat(name="Whiskers", age=4, indoor=True)
    cat2 = Cat(name="Shadow", age=7, indoor=False)

    print(generic_animal)
    print(dog1)
    print(dog2)
    print(cat1)
    print(cat2)

    print_section("Iterating Over All Animals")

    animals = [generic_animal, dog1, dog2, cat1, cat2]

    for animal in animals:
        print(animal.describe())

    print_section("Polymorphism — speak() method")

    for animal in animals:
        print(animal.speak())

    print_section("Dog-Specific Methods")

    print(dog1.learn_trick("Sit"))
    print(dog1.learn_trick("Shake hands"))
    print(dog1.learn_trick("Roll over"))
    print(dog1.show_tricks())

    print()
    print(dog2.learn_trick("Fetch"))
    print(dog2.show_tricks())

    print_section("Cat-Specific Methods")

    print(cat1.lifestyle())
    print(cat1.lose_life())
    print(cat1.lose_life())
    print(f"{cat1.name} now has {cat1.lives_remaining} lives remaining.\n")

    print(cat2.lifestyle())
    print(cat2.lose_life())

    print_section("String Representations (__str__)")

    for animal in animals:
        print(str(animal))


if __name__ == "__main__":
    main()
