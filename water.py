import datetime

class waterManager:
    def __init__(self):
        self.amount = {}
        today = datetime.date.today()
        self.filename = f"water_{today.strftime('%Y_%m_%d')}.txt"
        self.load_data()

    def log_water_intake(self, amount):
        date_str = datetime.now().strftime("%Y-%m-%d")
        self.amount[date_str] = amount
        self.save_data()
        
    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    date_str, amount = line.strip().split(',')
                    self.amount[date_str] = int(amount)
        except FileNotFoundError:
            print("No existing data found. Creating a new database.")
            with open(self.filename, 'w') as file:
                pass
            print(f"{self.filename} created successfully")

    def list_data(self):
        print("Water drinking timline:\n")
        for date_str, amount in self.amount.items():
            print(f"{date_str}: {amount}ltrs")

    def save_data(self):
        with open(self.filename, 'w') as file:
            for date_str, amount in self.amount.items():
                file.write(f"{date_str},{amount}\n")

def main():
    manager = waterManager()

    while(1):
        print("Menu:")
        print("0. Exit")
        print("1. input water amount")
        print("2. timeline")

        choice = (input("Enter choice: "))

        if(choice == '0'):
            print("Exiting...")
            return
        elif(choice == '1'):
            ltrs = float(input("Enter water amount in litres: "))
            manager.log_water_intake(ltrs)
            print("Water intake logged successfully.")
        elif(choice == '2'):
            manager.list_data()
        else:
            print("Invalid choice")
        

   

