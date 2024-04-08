import datetime

class PHQ9Assessment:
    def __init__(self):
        self.file_path = "PHQ_9_Complete.txt"
        self.questions = self.read_questions_from_file()
        self.responses = []

    def read_questions_from_file(self):
        questions = []
        with open(self.file_path, 'r') as file:
            # Skip header lines until reaching the questions
            for line in file:
                if line.strip().startswith("1."):
                    break
            questions.append(line.strip())  # Add the first question manually
            # Read the rest of the questions
            for line in file:
                if line.strip() and not line.strip().startswith("Please note:"):
                    # Aggregate multi-line questions and responses
                    if line.strip().startswith(tuple(str(i) for i in range(1, 10))):
                        questions.append(line.strip())
                    else:
                        questions[-1] += " " + line.strip()
                else:
                    break
        return questions

    def display_question_and_collect_response(self, question):
        print(question)
        response = input("Enter your response (0-3): ").strip()
        while not response.isdigit() or int(response) not in range(4):
            print("Invalid input. Please enter a number between 0 and 3.")
            response = input("Enter your response (0-3): ").strip()
        return int(response)

    def assess_depression_score(self, score):
        if score <= 4:
            return "Minimal depression"
        elif score <= 9:
            return "Mild depression"
        elif score <= 14:
            return "Moderate depression"
        elif score <= 19:
            return "Moderately severe depression"
        else:
            return "Severe depression"

    def conduct_assessment(self):
        total_score = 0
        print("PHQ-9 Depression Assessment\n")
        for question in self.questions:
            total_score += self.display_question_and_collect_response(question)
        assessment = self.assess_depression_score(total_score)
        print(f"\nYour total score is: {total_score}. Based on this score, your assessment is: {assessment}.\nPlease note, this is not a diagnostic tool. If you're concerned about your mental health, consider seeking professional advice.")

def main():
    phq9_assessment = PHQ9Assessment()
    phq9_assessment.conduct_assessment()


