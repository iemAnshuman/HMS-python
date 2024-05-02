import datetime
import csv
import time

class WaterManager:
    def __init__(self):
        self.amount = {}
        today = datetime.date.today()
        self.filename = f"water_{today.strftime('%Y_%m_%d')}.csv"
        self.load_data()

    def log_water_intake(self, amount):
        """Log water intake amount for the current date and save to the CSV."""
        time_log = time.localtime()
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_log)

        self.amount[formatted_time] = amount
        self.save_data()
        
    def load_data(self):
        """Load existing water intake data from the CSV file, if available. Otherwise, create a new CSV file."""
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Check to ensure row is not empty
                        formatted_time, amount = row
                        self.amount[formatted_time] = float(amount)
        except FileNotFoundError:
            print("No existing data found. Creating a new database.")
            with open(self.filename, 'w', newline='') as file:
                pass  # File is created on opening with 'w'
            print(f"{self.filename} created successfully")

    def list_data(self):
        """Print a formatted list of all water intake records."""
        print("Water drinking timeline:\n")
        for formatted_time, amount in self.amount.items():
            print(f"{formatted_time}: {amount} ltrs")

    def save_data(self):
        """Save all current water intake data to a CSV file."""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for formatted_time, amount in self.amount.items():
                writer.writerow([formatted_time, amount])

def main():
    manager = WaterManager()

    while True:
        print("Menu:")
        print("0. Exit")
        print("00. Back")
        print("1. Input water amount")
        print("2. Timeline")

        choice = input("Enter choice: ")

        if choice == '0':
            print("Exiting...")
            exit(0)
        elif choice == '00':
            break
        elif choice == '1':
            ltrs = float(input("Enter water amount in litres: "))
            manager.log_water_intake(ltrs)
            print("Water intake logged successfully.")
        elif choice == '2':
            manager.list_data()
        else:
            print("Invalid choice")

 

