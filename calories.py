import datetime

class Tracker:
    def __init__(self):
        self.calories = {}
        today = datetime.date.today()
        self.filename = f"calories_{today.strftime('%Y_%m_%d')}.txt"
        self.load_data()

    def add_food(self, food, calories):
        self.calories[food] = calories
        print(f"{food} added to the list")
        self.save_data()

    def remove_food(self, food):
        if food in self.calories:
            del self.calories[food]
            print(f"{food} removed from the list")
            self.save_data()
        else:
            print(f"{food} is not in the list")
        
    def sum_calories(self):
        total = sum(self.calories.values())
        print(f"Total calories: {total}")

    def list_food(self):
        print("Foods in the list:")
        for food, calories in self.calories.items():
            print(f"{food} - {calories} calories")
        
    def load_data(self):
        try: 
            with open(self.filename, 'r') as file:
                for line in file:
                    food, calories = line.strip().split(',')
                    self.calories[food] = int(calories)
        except FileNotFoundError:
            print("No existing data found. Creating a new database.")
            with open(self.filename, 'w') as file:
                pass
            print(f"{self.filename} created successfully")

    def save_data(self):
        with open(self.filename, 'w') as file:
            for food, calories in self.calories.items():
                file.write(f"{food},{calories}\n")

def get_numeric_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calorie():
    tracker = Tracker()
    while True:
        print("\nCalorie Tracker Menu: ")
        print("1. Add food")
        print("2. Remove food")
        print("3. View total calories")
        print("4. View all foods")
        print("5. Exit")

        choice2 = get_numeric_input("Enter your choice: ")

        if choice2 == '1':
            food = input("Enter the food: ")
            calories = get_numeric_input("Enter the calories: ")
            tracker.add_food(food, calories)
        elif choice2 == '2':
            food = input("Enter the food to remove: ")
            tracker.remove_food(food)
        elif choice2 == '3':
            tracker.sum_calories()
        elif choice2 == '4':
            tracker.list_food()
        elif choice2 == '5':
            return
        else:
            print("Please enter a valid choice.")
  