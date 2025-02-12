#!/usr/bin/env python3
class Dog:
    def __init__(self, name, breed="Mutt"):  # Default breed is "Any"
        self.name = name
        self.breed = breed

# Creating Dog objects with names
fido = Dog("Fido")  
snoopy = Dog("Snoopy")

# Changing the breed
fido.breed = "Dalmatian"
snoopy.breed = "Beagle"

print(f"{fido.name} is a {fido.breed}.")  # Output: Fido is a Dalmatian.
print(f"{snoopy.name} is a {snoopy.breed}.")  # Output: Snoopy is a Beagle.


