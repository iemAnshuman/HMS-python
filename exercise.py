import datetime
import csv

class ExerciseManager:
    def __init__(self):
        self.exercises = {}
        today = datetime.date.today()
        self.filename = f"exercise_{today.strftime('%Y_%m_%d')}.csv"
        self.load_data()

    def log_exercise(self, name, duration):
        """Log an exercise with its duration and the current date, then save to the CSV."""
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        if date_str not in self.exercises:
            self.exercises[date_str] = []
        self.exercises[date_str].append((name, duration))
        self.save_data()
        
    def load_data(self):
        """Load existing exercise data from the CSV file, if available. Otherwise, create a new CSV file."""
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        date_str = row[0]
                        it = iter(row[1:])
                        self.exercises[date_str] = [(name, int(duration)) for name, duration in zip(it, it)]
        except FileNotFoundError:
            print("No existing data found. Creating a new database.")
            with open(self.filename, 'w', newline='') as file:
                pass
            print(f"{self.filename} created successfully")

    def list_data(self):
        """Print a formatted list of all logged exercises grouped by date."""
        print("Exercise timeline:\n")
        for date_str, exercise_list in self.exercises.items():
            print(f"{date_str}:")
            for exercise in exercise_list:
                print(f"  {exercise[0]} for {exercise[1]} minutes")

    def save_data(self):
        """Save all current exercise data to a CSV file."""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for date_str, exercise_list in self.exercises.items():
                line = [date_str] + [item for sublist in exercise_list for item in sublist]
                writer.writerow(line)

def main():
    manager = ExerciseManager()
    
    while True:
        print("Menu:")
        print("0. Exit")
        print("00. Back")
        print("1. Log Exercise")
        print("2. Exercise Timeline")

        choice = input("Enter choice: ")

        if choice == '0':
            print("Exiting...")
            exit(0)
        elif choice == '00':
            break
        elif choice == '1':
            name = input("Enter exercise name: ")
            duration = int(input("Enter duration in minutes: "))
            manager.log_exercise(name, duration)
            print("Exercise logged successfully.")
        elif choice == '2':
            manager.list_data()
        else:
            print("Invalid choice")

