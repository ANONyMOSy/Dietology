"""
Tha main file will process user input and process results for the entire program.
"""

__author__ = "James Kaddissi"
__version__ = "0.1.0"


class User:
    def __init__(self, name, age, gender, height, weight, target_weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height  # in inches
        self.weight = weight  # in lbs
        self.target_weight = target_weight  # in lbs
        self.daily_meals = []  # List to store daily meal plan

    # Existing getters and setters...

    # Method to calculate BMI
    def calculate_bmi(self):
        bmi = (self.weight / (self.height**2)) * 703
        return round(bmi, 2)

    # Method to categorize weight based on BMI
    def categorize_weight(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

    # Method to calculate maintenance calories
    def calculate_maintenance_calories(self):
        # Basic formula for BMR (Basal Metabolic Rate)
        if self.gender.lower() == 'male':
            bmr = 88.362 + (13.397 * self.weight * 0.453592) + (4.799 * self.height * 2.54) - (5.677 * self.age)
        else:
            bmr = 447.593 + (9.247 * self.weight * 0.453592) + (3.098 * self.height * 2.54) - (4.330 * self.age)
        # Assuming sedentary lifestyle for maintenance calories (BMR * 1.2)
        return round(bmr * 1.2)

    # Method to suggest calorie intake for weight loss (500 kcal/day deficit for example)
    def suggest_calorie_intake_for_loss(self, deficit=500):
        maintenance = self.calculate_maintenance_calories()
        return maintenance - deficit

    # Method to add food to the daily meal plan
    def add_food_to_meal_plan(self, food_name, calories):
        self.daily_meals.append((food_name, calories))

    # Method to display the meal plan
    def display_meal_plan(self):
        print(f"{self.name}'s Daily Meal Plan:")
        for food, cal in self.daily_meals:
            print(f"{food} - {cal} calories")



def main():
    # Gather user input for all the fields
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female/other): ")
    height = float(input("Enter your height in inches: "))
    weight = float(input("Enter your weight in pounds: "))
    target_weight = float(input("Enter your target weight in pounds: "))

    profile = User(name, age, gender, height, weight, target_weight)
J

    # Utilize each function of the class
    print(f"\nWelcome, {profile.name}!")
    print(f"Current BMI: {profile.calculate_bmi()} ({profile.categorize_weight()})")
    print(f"Your maintenance calories: {profile.calculate_maintenance_calories()} kcal/day")
    print(f"Suggested daily calorie intake for weight loss: {profile.suggest_calorie_intake_for_loss()} kcal/day")

    # Interact with the daily meal plan
    while True:
        food = input("\nEnter a food item to add to your meal plan (or type 'done' to finish): ")
        if food.lower() == 'done':
            break
        calories = int(input(f"Enter the number of calories in {food}: "))
        profile.add_food_to_meal_plan(food, calories)

    # Display the final meal plan
    profile.display_meal_plan()

if __name__ == "__main__":
    main()