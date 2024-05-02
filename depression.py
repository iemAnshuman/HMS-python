import datetime

class PHQ9Assessment:
    def __init__(self):
        self.file_path = "PHQ_9_Complete.txt"
        self.questions = self.read_questions_from_file()
        self.responses = []

    def read_questions_from_file(self):
        questions = []
        with open(self.file_path, 'r') as file:
            collecting = False
            for line in file:
                if "1." in line:  # Start collecting questions from this point
                    collecting = True
                if collecting:
                    if line.strip() and not line.strip().startswith("Please note:"):
                        if line[0].isdigit() and line[1] == '.':
                            # New question starts
                            questions.append(line.strip())
                        else:
                            # Continuation of the current question
                            questions[-1] += " " + line.strip().replace('\n', ' ')
                    else:
                        break  # Stop reading if "Please note:" is encountered or empty line
        return questions

    def display_question_and_collect_response(self, question):
        print(question)
        response = input("Enter your response (0-3): ").strip()
        while not response.isdigit() or int(response) not in range(4):
            print("Invalid input. Please enter a number between 0 and 3.")
            response = input("Enter your response (0-3): ").strip()
        self.responses.append(int(response))  # Store responses to analyze later
        return int(response)

    def assess_depression_score(self):
        score = sum(self.responses)  # Calculate the total score based on responses
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
        print("PHQ-9 Depression Assessment\n")
        for question in self.questions:
            self.display_question_and_collect_response(question)
        assessment = self.assess_depression_score()
        print(f"\nYour total score is: {sum(self.responses)}. Based on this score, your assessment is: {assessment}.\nPlease note, this is not a diagnostic tool. If you're concerned about your mental health, consider seeking professional advice.")

def main():
    phq9_assessment = PHQ9Assessment()
    phq9_assessment.conduct_assessment()





