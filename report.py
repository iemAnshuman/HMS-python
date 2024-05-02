import calories
import exercise
import water
import mental_health
import log

# Function to collect all data
def collect_all_data():
    calorie_data = calories.get_calorie_data()
    exercise_data = exercise.get_exercise_data()
    water_data = water.get_water_data()
    mental_health_data = mental_health.get_mental_health_data()
    log_data = log.get_log_data()
    return {
        "calorie": calorie_data,
        "exercise": exercise_data,
        "water": water_data,
        "mental_health": mental_health_data,
        "log": log_data
    }

# Analysis function to calculate averages
def calculate_averages(data):
    averages = {}
    for key, value in data.items():
        if value:  # Ensure there is data to average
            average = sum(value) / len(value)
            averages[key] = average
    return averages

# Main report function
def generate_report():
    data = collect_all_data()
    averages = calculate_averages(data)
    report = "Health Management System Report\n"
    report += "--------------------------------\n"
    for category, avg in averages.items():
        report += f"Average {category} data: {avg:.2f}\n"
    
    # Add more detailed analyses as needed
    report += "\nDetailed Analysis:\n"
    report += f"Total water intake: {sum(data['water']):.2f} liters\n"
    report += f"Total calories consumed: {sum(data['calorie']):.2f} calories\n"
    report += f"Total exercise done: {sum(data['exercise']):.2f} minutes\n"
    report += "Mental health status: Good" if any(data['mental_health']) else "Mental health status: Needs attention"
    
    return report

# Example usage
if __name__ == "__main__":
    full_report = generate_report()
    print(full_report)