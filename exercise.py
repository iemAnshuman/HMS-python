import datetime

class ExerciseManager:
    def __init__(self):
        self.exercises = {}
        today = datetime.date.today()
        self.filename = f"exercise_{today.strftime('%Y_%m_%d')}.txt"
        self.load_data()

    def log_exercise(self, name, duration):
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        if date_str not in self.exercises:
            self.exercises[date_str] = []
        self.exercises[date_str].append((name, duration))
        self.save_data()
        
    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    date_str = parts[0]
                    exercises = parts[1:]
                    self.exercises[date_str] = [(exercises[i], int(exercises[i + 1])) for i in range(0, len(exercises), 2)]
        except FileNotFoundError:
            print("No existing data found. Creating a new database.")
            with open(self.filename, 'w') as file:
                pass
            print(f"{self.filename} created successfully")

    def list_data(self):
        print("Exercise timeline:\n")
        for date_str, exercise_list in self.exercises.items():
            print(f"{date_str}:")
            for exercise in exercise_list:
                print(f"  {exercise[0]} for {exercise[1]} minutes")

    def save_data(self):
        with open(self.filename, 'w') as file:
            for date_str, exercise_list in self.exercises.items():
                line = [date_str] + [item for sublist in exercise_list for item in sublist]
                file.write(','.join(map(str, line)) + '\n')

def main():
    manager = ExerciseManager()
    
    while(1):
        print("Menu:")
        print("0. Exit")
        print("1. Log Exercise")
        print("2. Exercise Timeline")

        choice = (input("Enter choice: "))

        if choice == '0':
            print("Exiting...")
            return
        elif choice == '1':
            name = input("Enter exercise name: ")
            duration = int(input("Enter duration in minutes: "))
            manager.log_exercise(name, duration)
            print("Exercise logged successfully.")
        elif choice == '2':
            manager.list_data()
        else:
            print("Invalid choice")

