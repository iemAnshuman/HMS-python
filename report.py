# made through help

import os
import datetime
from glob import glob

class WeeklyReportGenerator:
    def __init__(self, base_path):
        self.base_path = base_path
        self.week_data = {
            'calories': {},
            'water': {},
            'exercise': {}
        }

    def load_weekly_data(self):
        # Load data for the past 7 days
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=6)

        for single_date in (start_date + datetime.timedelta(n) for n in range(7)):
            date_str = single_date.strftime('%Y_%m_%d')
            self.load_daily_data('calories', f"calories_{date_str}.txt")
            self.load_daily_data('water', f"water_{date_str}.txt")
            self.load_daily_data('exercise', f"exercise_{date_str}.txt")

    def load_daily_data(self, data_type, filename):
        filepath = os.path.join(self.base_path, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if data_type == 'calories':
                        # Assuming the file structure: food,calories
                        self.week_data[data_type][parts[0]] = self.week_data[data_type].get(parts[0], 0) + int(parts[1])
                    elif data_type == 'water':
                        # Assuming the file structure: date_str,amount
                        date_str = parts[0]
                        self.week_data[data_type][date_str] = self.week_data[data_type].get(date_str, 0) + float(parts[1])
                    elif data_type == 'exercise':
                        # Assuming the file structure: date_str,exercise_name,duration
                        date_str, exercise_name, duration = parts[0], parts[1], int(parts[2])
                        if date_str not in self.week_data[data_type]:
                            self.week_data[data_type][date_str] = []
                        self.week_data[data_type][date_str].append((exercise_name, duration))

    def generate_report(self):
        # Calculate averages and totals
        total_water = sum(self.week_data['water'].values())
        avg_water = total_water / len(self.week_data['water']) if self.week_data['water'] else 0

        total_calories = sum(self.week_data['calories'].values())
        avg_calories = total_calories / len(self.week_data['calories']) if self.week_data['calories'] else 0

        exercise_summary = {}
        for daily_exercises in self.week_data['exercise'].values():
            for name, duration in daily_exercises:
                exercise_summary[name] = exercise_summary.get(name, 0) + duration

        # Print the report
        print(f"Weekly Water Intake: {total_water}L (Avg: {avg_water:.2f}L/day)")
        print(f"Weekly Calorie Intake: {total_calories} (Avg: {avg_calories:.2f}/day)")
        print("Weekly Exercise Summary:")
        for name, total_duration in exercise_summary.items():
            print(f"  {name}: {total_duration} minutes")

