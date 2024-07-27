""" 
Data abstraction is one of the most essential concepts of Python OOPs
which is used to hide irrelevant details from the user
and show the details that are relevant to the users

For example, the readers of geeksforgeeks only know that a writer can write an 
article on geeksforgeeks, and when it gets published readers can read the 
articles but the reader is not aware of the background process of publishing the article.

An Abstract class can contain the both method normal and abstract method.
An Abstract cannot be instantiated; we cannot create objects for the abstract class.
"""
# Import required modules
from abc import ABC, abstractmethod


# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Create abstract method
    @abstractmethod
    def printDetails(self):
        pass

    # Create concrete method
    def accelerate(self):
        print("Speed up ...")

    def break_applied(self):
        print("Car stopped")


# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self):
        print("Not having this feature")


# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self):
        print("Available")


# Create an instance of the Hatchback class
car1 = Hatchback("Maruti", "Alto", "2022")

# Call methods
car1.printDetails()
car1.accelerate()
car1.sunroof()
