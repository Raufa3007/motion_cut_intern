quiz_data = [
    {
        "question": "What is the largest lake in the world?",
        "options": ["A) Caspian Sea", "B) Baikal", "C) Lake Superior", "D) Ontario"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote the novel “War and Peace”?",
        "options": ["A) Anton Chekhov", "B) Fyodor Dostoevsky", "C) Leo Tolstoy", "D) Ivan Turgenev"],
        "answer": "C"
    }
]

# Function to ask questions and check answers
def ask_question(question_data):
    print("\n" + question_data["question"])
    for option in question_data["options"]:
        print(option)
    
    # Get user input
    answer = input("Please enter the letter of your answer: ").upper()
    while answer not in ["A", "B", "C", "D"]:
        print("Invalid choice. Please enter A, B, C, or D.")
        answer = input("Please enter the letter of your answer: ").upper()

    # Check if the answer is correct
    if answer == question_data["answer"]:
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is {question_data['answer']}.")
        return False

# Main function to run the quiz
def run_quiz():
    print("Welcome to the Quiz Game!")
    score = 0

    # Loop through each question
    for question_data in quiz_data:
        if ask_question(question_data):
            score += 1
    
    # Display final score
    print("\nQuiz Completed!")
    print(f"Your final score is: {score} out of {len(quiz_data)}")
    percentage = (score / len(quiz_data)) * 100
    print(f"That's {percentage:.2f}%!")

# Run the quiz
run_quiz()
