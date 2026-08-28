# Create an animal management system for a shelter demonstrating the pillars of OOP
# through implementing different classes.

# Import the ABC module to create an abstract base class.
from abc import ABC, abstractmethod

# Initialize a list of accepted animal types.
accepted_animal_types = ["dog", "cat"]

# Create an abstract base class Animal encapsulating common attributes and behaviors.
class Animal(ABC):
    def __init__(self, name, age, species):
        self.__name = name        # Private attribute
        self.__age = age          # Private attribute
        self._species = species   # Protected attribute

    # Accessor method for name
    def get_name(self):
        return self.__name

    # Mutator method for name
    def set_name(self, name):
        self.__name = name

    # Accessor method for age
    def get_age(self):
        return self.__age

    # Mutator method for age
    def set_age(self, age):
        # Validate user input to ensure age is a non-negative integer less than 20.
        if 0 <= age <= 20:
            self.__age = age

    # Only a get method here since the species is set when the animal is created and should not be changed.
    def get_species(self):
        return self._species
    
    # Create a method to display the animal's information.
    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Species: {self._species}")

    # Create a method to update the animal's age.
    def update_age(self, new_age):

        # Conditional to ensure age is within the correct range.
        if str(new_age).isdigit() and 0 <= int(new_age) <= 20:
            self.set_age(int(new_age))
            print(f"{self.__name}'s age has been updated to {self.__age}.")
        else:
            print("Invalid age. Age must be a non-negative integer less than 20.")

    # Require all subclasses to implement its own speak behavior.
    @abstractmethod
    def speak(self):
        pass

# Create a Dog class that inherits the Animal class.
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.__breed = breed

    # Accessor method for breed
    def get_breed(self):
        return self.__breed

    # Mutator method for breed
    def set_breed(self, breed):
        # Validate user input to ensure breed is not empty.
        if breed.strip() != "":
            self.__breed = breed

    # Declare a bark() method.
    def bark(self):
        print(f"{self.get_name()} says Woof!")

    # Override the speak() method to provide the dog's specific behavior.
    def speak(self):
        self.bark()

    # Display the dog's information, including its breed.
    def display_info(self):
        super().display_info()
        print(f"Breed: {self.__breed}")

# Create a Cat class that inherits the Animal class.
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Cat")
        self.__color = color

    # Accessor method for color
    def get_color(self):
        return self.__color

    # Mutator method for color
    def set_color(self, color):
        # Validate user input to ensure color is not empty.
        if color.strip() != "":
            self.__color = color

    # Declare a meow() method.
    def meow(self):
        print(f"{self.get_name()} says Meow!")

    # Override the speak() method to provide the cat's specific behavior.
    def speak(self):
        self.meow()

    # Display the cat's information, including its color.
    def display_info(self):
        super().display_info()
        print(f"Color: {self.__color}")

# Create an abstract AnimalShelter class with methods to add or remove animals from the shelter.
class AnimalShelter(ABC):
    # Define an abstract method to add an animal to the shelter.
    @abstractmethod
    def add_animal(self, animal):
        pass

    # Define an abstract method to remove an animal from the shelter.
    @abstractmethod
    def remove_animal(self, animal):
        pass

    # Define an abstract method to display all animals in the shelter.
    @abstractmethod
    def display_animals(self):
        pass

# Create a concrete Shelter class that inherits from the AnimalShelter class and implements the abstract methods.
class Shelter(AnimalShelter):

    # Implement the constructor to initialize the animal_list.
    def __init__(self):
        self.__animal_list = []

    # Implement abstract method to add an animal to the shelter.
    def add_animal(self, animal):
        self.__animal_list.append(animal)
        print(f"{animal.get_name()} has been added to the shelter.")

    # Implement abstract method to remove an animal from the shelter.
    def remove_animal(self, animal_name):

        # Loop through the animal_list to find the animal to be removed. If found, remove it and print a confirmation message. If not found, print a message indicating that the animal was not found.
        for animal in self.__animal_list:

            # Confirm if the animal is found.
            if animal.get_name().lower() == animal_name.lower():
                # Remove the animal from the shelter and print a confirmation message.
                self.__animal_list.remove(animal)
                print(f"{animal.get_name()} has been removed from the shelter.")

                return
        # Otherwise display a message the animal is not in the shelter.
        print(f"No animal with the name of {animal_name} is found in the shelter.")

    # Implement abstract method to display all animals in the shelter.
    def display_animals(self):

        # Conditional to handle if there are no animals in the shelter.
        if not self.__animal_list:
            print("No animals in the shelter.")
        else:
            # Loop through the animal_list and display each animal's information.
            for animal in self.__animal_list:
                animal.display_info()

                # Demonstrate polymorphism by calling the speak() method for each animal in the shelter.
                animal.speak()
                print()

# Create a shelter variable to store the shelter object.
shelter = Shelter()

# Create a while True loop to display a menu enabling a user to add, delete, or display shelter animals.
while True:
    print("\n   Animal Shelter Management System   ")
    print("-----------------------------------------")
    print("1. Add an Animal")
    print("2. Delete an Animal")
    print("3. Display All Animals")
    print("4. Exit")

    # Store the user's selection
    selection = input("\nEnter your choice (1-4): ")

    # Process user selection of 1.
    if selection == "1":

        # Reprompt the user to enter the animal's type until a valid input is received.
        while True:
            # Prompt the user to enter the animal's type.
            animal_type = input("\nEnter animal type (Dog/Cat): ").strip().lower()

            # Validate the input
            if animal_type == "":
                print("\nAnimal type cannot be empty. Please enter 'Dog' or 'Cat'.")
            elif animal_type not in accepted_animal_types:
                print("\nInvalid animal type. Please enter 'Dog' or 'Cat'.")
            else:
                break

        # Reprompt the user to enter the animal's name until a valid input is received.
        while True:
            # Prompt the user to enter the animal's name.
            name = input("\nEnter animal name: ")

            # Validate the input
            if name == "":
                print("Animal name cannot be empty. Please enter a valid name.")
            else:
                break

        # Reprompt the user to enter the animal's age until a valid input is received.
        while True:
            # Prompt the user to enter the animal's age removing any leading or trailing whitespace.
            age = input("\nEnter animal age: ").strip()

            # Validate the input
            if age == "":
                print("Animal age cannot be empty. Please enter a valid age.")
            elif not age.isdigit():
                print("Invalid age. Please enter a non-negative integer.")
            elif int(age) > 20:
                print("Invalid age. Please enter an integer between 0 and 20.")
            else:
                age = int(age)
                break

        # Store animal data based on the animal type and reprompt if input is invalid.
        if animal_type == "dog":

            # Reprompt the user to enter the dog's breed until a valid input is received.
            while True:
                # Prompt the user to enter the dog's breed removing any leading or trailing whitespace.
                breed = input("Enter dog breed: ").strip()

                # Validate the input
                if breed == "":
                    print("Dog breed cannot be empty. Please enter a valid breed.")
                else:
                    break

            # Store the dog data in new_animal to be appended to the animal_list.
            new_animal = Dog(name, age, breed)

        # The only other option is cat, so we can use an else statement to handle that case.
        else:
            # Reprompt the user to enter the cat's color until a valid input is received.
            while True:
                # Prompt the user to enter the cat's color removing any leading or trailing whitespace. 
                color = input("Enter cat color: ")

                # Validate the input
                if color == "":
                    print("Cat color cannot be empty. Please enter a valid color.")
                else:
                    break

            # Store the cat data in new_animal to be appended to the animal_list.
            new_animal = Cat(name, age, color)

        # Append new_animal to the animal_list and print a confirmation message.
        shelter.add_animal(new_animal)

    # Process user selection of 2.
    elif selection == "2":

        #Reprompt if invalid input is received.
        while True:

            # Prompt user to enter name of animal to remove from the animal_list and remove it if it exists, otherwise print a message indicating that the animal was not found.
            name_to_remove = input("Enter the name of the animal to remove: ").strip()

            # Validate the input
            if name_to_remove == "":
                print("Animal name cannot be empty. Please enter a valid name.")
            else:
                break

        # Call the remove_animal() method to remove the animal from the shelter.
        shelter.remove_animal(name_to_remove)

    # Process user selection of 3.
    elif selection == "3":

        # Call the display_animals() method to display all animals in the shelter.
        shelter.display_animals()

    # Process user selection of 4.
    elif selection == "4":
        print("Exiting the Animal Shelter Management System. Goodbye!")
        break
    # Display a message if the user enters an invalid selection.
    else:
        print("Invalid choice. Please try again.")

# REFERENCES:
#
# 1. GeeksforGeeks. (2026, June 5). "Python Classes and Objects". 
#    https://www.geeksforgeeks.org/python/python-classes-and-objects/
# 2. GeeksforGeeks. (2025, September 3). "Abstract Classes in Python".
#    https://www.geeksforgeeks.org/python/abstract-classes-in-python/
# 3. GeeksforGeeks. (2026, June 5). "Polymorphism in Python".
#    https://www.geeksforgeeks.org/python/polymorphism-in-python/
# 4.