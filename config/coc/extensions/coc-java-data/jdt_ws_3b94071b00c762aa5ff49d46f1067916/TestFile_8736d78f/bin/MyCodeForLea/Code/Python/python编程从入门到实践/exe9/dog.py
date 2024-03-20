class Dog:
    """A Simple Attempt to Simulate a Dog"""
    def __init__(self,name,age):
        """initialize name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """ Simulate the puppy squatting down upon receiving the command"""
        print(f"{self.name.title()} is now sitting")

    def roll_over(self):
        print(f"{self.name.title()} rolled over!")

my_dog = Dog('willie',6)
your_dog = Dog('Lucy',3)
my_dog.sit()
my_dog.roll_over()
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

print(f"\nYour dog's name is {your_dog.name}")
your_dog.sit()
