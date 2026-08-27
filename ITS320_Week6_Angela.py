# Create an animal management system for a shelter demonstrating the pillars of OOP
# through implementing different classes.

# Initialize a list of accepted animal types.
accepted_animal_types = ["dog", "cat"]

# Create an empty list to store animal objects.
animal_list = []

# Create a base class Animal with name, age, and species attributes.
class Animal():
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
        if str(new_age).isdigit() and 0 <= int(new_age) < 20:
            self.set_age(int(new_age))
            print(f"{self.__name}'s age has been updated to {self.__age}.")
        else:
            print("Invalid age. Age must be a non-negative integer less than 20.")

# Create a Dog class that inherits the Animal class.
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.breed = breed

    # Declare a bark() method.
    def bark(self):
        print(f"{self._Animal__name} says Woof!")

# Create a Cat class that inherits the Animal class.
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Cat")
        self.color = color

    # Declare a meow() method.
    def meow(self):
        print(f"{self._Animal__name} says Meow!")

# Create a while True loop to display a menu enabling a user to add, delete, or display shelter animals.
while True:
    print("\n   Animal Shelter Management System   ")
    print("-----------------------------------------")
    print("1. Add an Animal")
    print("2. Delete an Animal")
    print("3. Display All Animals")
    print("4. Exit")

    # Store the user's selection
    selection = input("Enter your choice (1-4): ")

    # Process user selection of 1.
    if selection == "1":

        # Reprompt the user to enter the animal's type until a valid input is received.
        while True:
            # Prompt the user to enter the animal's type.
            animal_type = input("Enter animal type (Dog/Cat): ").strip().lower()

            # Validate the input
            if animal_type == "":
                print("Animal type cannot be empty. Please enter 'Dog' or 'Cat'.")
            elif animal_type not in accepted_animal_types:
                print("Invalid animal type. Please enter 'Dog' or 'Cat'.")
            else:
                break

        # Reprompt the user to enter the animal's name until a valid input is received.
        while True:
            # Prompt the user to enter the animal's name.
            name = input("Enter animal name: ")

            # Validate the input
            if name == "":
                print("Animal name cannot be empty. Please enter a valid name.")
            else:
                break

        # Reprompt the user to enter the animal's age until a valid input is received.
        while True:
            # Prompt the user to enter the animal's age removing any leading or trailing whitespace.
            age = int(input("Enter animal age: ")).strip()

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
        animal_list.append(new_animal)
        print(f"{new_animal.name} has been added to the shelter.")

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

            # Loop through the animal_list to find the animal name to be removed. Convert to lowercase to ensure case insensitivity.
            for animal in animal_list:

                # Logic to handle if the name is found.
                if animal.name.lower() == name_to_remove.lower():
                    animal_list.remove(animal)
                    print(f"{animal.name} has been removed from the shelter.")
                    break
                else:
                    print(f"No animal found with the name {name_to_remove}.")

    # Process user selection of 3.
    elif selection == "3":

        # Display a message if the animal_list is empty.
        if not animal_list:
            print("No animals in the shelter.")
        else:
            # Loop through the animal_list and call the display_info() method for each animal.
            for animal in animal_list:
                animal.display_info()

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
# 2. 