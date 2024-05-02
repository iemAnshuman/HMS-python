import datetime
import csv

class Tracker:
    def __init__(self):
        self.calories = {}
        today = datetime.date.today()
        self.filename = f"calories_{today.strftime('%Y_%m_%d')}.csv"
        self.load_data()

    def add_food(self, food, calories):
        """Add a food item and its calorie count to the dictionary and save to the CSV."""
        self.calories[food] = calories
        print(f"{food} added to the list")
        self.save_data()

    def remove_food(self, food):
        """Remove a food item from the dictionary if it exists and save the new data to the CSV."""
        if food in self.calories:
            del self.calories[food]
            print(f"{food} removed from the list")
            self.save_data()
        else:
            print(f"{food} is not in the list")

    def sum_calories(self):
        """Calculate and print the sum of all calorie values in the dictionary."""
        total = sum(self.calories.values())
        print(f"Total calories: {total}")

    def list_food(self):
        """Print all food items with their corresponding calorie count."""
        print("Foods in the list:")
        for food, calories in self.calories.items():
            print(f"{food} - {calories} calories")

    def load_data(self):
        """Load existing data from the CSV file, if available. Otherwise, create a new CSV file."""
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # making sure there's data to process
                        food, calories = row
                        self.calories[food] = int(calories)
        except FileNotFoundError:
            print("No existing data found. Creating a new database.")
            with open(self.filename, 'w', newline='') as file:
                pass
            print(f"{self.filename} created successfully")

    def save_data(self):
        """Save the current data in the dictionary to a CSV file."""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for food, calories in self.calories.items():
                writer.writerow([food, calories])

def get_numeric_input(prompt):
    """Request input from the user and convert it to an integer. Repeat until valid input is received."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def calorie():
    """Function to handle user interactions for managing the calorie tracker."""
    tracker = Tracker()
    while True:
        print("\nCalorie Tracker Menu: ")
        print("0. Exit")
        print("100. Back")
        print("1. Add food")
        print("2. Remove food")
        print("3. View total calories")
        print("4. View all foods")

        choice = get_numeric_input("Enter your choice: ")

        if choice == 1:
            food = input("Enter the food: ")
            calories = get_numeric_input("Enter the calories: ")
            tracker.add_food(food, calories)
        elif choice == 2:
            food = input("Enter the food to remove: ")
            tracker.remove_food(food)
        elif choice == 3:
            tracker.sum_calories()
        elif choice == 4:
            tracker.list_food()
        elif choice == 0:
            exit(0)
        elif choice == 100:
            break
        else:
            print("Please enter a valid choice.")
