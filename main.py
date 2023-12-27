"""
Tha main file will process user input and process results for the entire program.
"""

__author__ = "James Kaddissi"
__version__ = "0.1.0"


class User:
    def __init__(self, name, age, gender, height, weight, target_weight):
        # This class is used to store a profile for the user. Any relevant user data is stored here
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height  # in in
        self.weight = weight  # in lbs
        self.target_weight = target_weight  # in lbs

    # Getter for Name
    @property
    def name(self):
        return self._name

    # Setter for Name
    @name.setter
    def name(self, value):
        # You can add validation if needed
        self._name = value

    # Getter for Age
    @property
    def age(self):
        return self._age

    # Setter for Age
    @age.setter
    def age(self, value):
        # Add validation to ensure age is a positive integer
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            raise ValueError("Please enter a valid age.")

    # Getter for Gender
    @property
    def gender(self):
        return self._gender

    # Setter for Gender
    @gender.setter
    def gender(self, value):
        # Add validation for gender
        if value.lower() in ['male', 'female', 'other']:
            self._gender = value
        else:
            raise ValueError("Please enter 'male', 'female', or 'other' for gender.")

    # Getter for Height
    @property
    def height(self):
        return self._height

    # Setter for Height
    @height.setter
    def height(self, value):
        # Add validation to ensure height is a positive number
        if isinstance(value, (int, float)) and value > 0:
            self._height = value
        else:
            raise ValueError("Please enter a valid height in inches.")

    # Getter for Weight
    @property
    def weight(self):
        return self._weight

    # Setter for Weight
    @weight.setter
    def weight(self, value):
        # Add validation to ensure weight is a positive number
        if isinstance(value, (int, float)) and value > 0:
            self._weight = value
        else:
            raise ValueError("Please enter a valid weight in pounds.")

    # Getter for Target Weight
    @property
    def target_weight(self):
        return self._target_weight

    # Setter for Target Weight
    @target_weight.setter
    def target_weight(self, value):
        # Add validation to ensure target weight is a positive number
        if isinstance(value, (int, float)) and value > 0:
            self._target_weight = value
        else:
            raise ValueError("Please enter a valid target weight in pounds.")


    def __str__(self):
        # string function
        return f"{self.name}'s Diet Profile"



def main():
    person = User(name='John Doe', age=30, gender='Male', height=70, weight=190, target_weight=170)
    print(person.name)
    print(person.target_weight)

if __name__ == "__main__":
    main()