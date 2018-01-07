#!/usr/local/bin/python3
"""doggies.py Objective 14"""
class dog:
        def __init__(self, name, breed):
                        self.name = name
                        self.breed = breed

        def __str__(self):
                        return "{0}:{1}".format(self.name, self.breed)

if __name__ == "__main__":
        promptName = "Enter Dog Name:"
        promptBreed = "Enter Breed of Dog:"
        dog_count = 0
        DOGS = []
        while True:
                dog_name = input(promptName)
                dog_breed = ""  # force input if new breed
                if dog_name == "":
                        break
                if dog_name != "":
                        while dog_breed == "":
                                dog_breed = input(promptBreed)
                DOGS.append(dog(dog_name,dog_breed))
                print("DOGS")
                for i, dawg in enumerate(DOGS):
                        print("{0}. {1}".format(i,dawg))
                print("*" * 40)
