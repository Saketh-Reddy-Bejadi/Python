participants = []
survey_questions = [
    "How satisfied are you with the product?",
    "How likely are you to recommend the product?",
    "How would you rate the customer service?",
    "How user-friendly is the website?",
    "How satisfied are you with the delivery process?",
]

def take_survey():
    name = input("Enter participant name (or 'q' to quit): ")
    if name == "q":
        return

    participant = {"name": name, "responses": []}

    for i, question in enumerate(survey_questions):
        print(f"{i + 1}. {question}")
        response = int(input("Enter your review (1-5): "))
        participant["responses"].append(response)

    participants.append(participant)
    print("Survey completed successfully!")

def display_results():
    if not participants:
        print("No participants found!")
        return

    print("Survey Results:")
    for i, participant in enumerate(participants):
        print(f"\nParticipant {i + 1}: {participant['name']}")
        print("Responses:")
        for j, response in enumerate(participant["responses"]):
            question = survey_questions[j]
            print(f"{j + 1}. {question}")
            print(f"   Response: {response}")

def add_question():
    question = input("Enter the new question: ")
    survey_questions.append(question)
    print("Question added successfully!")

def delete_question():
    display_questions()
    question_number = int(input("Enter the question number to delete: ")) - 1
    if 0 <= question_number < len(survey_questions):
        deleted_question = survey_questions.pop(question_number)
        print(f"Question '{deleted_question}' deleted successfully!")
    else:
        print("Invalid question number!")

def edit_question():
    display_questions()
    question_number = int(input("Enter the question number to edit: ")) - 1
    if 0 <= question_number < len(survey_questions):
        new_question = input("Enter the new question: ")
        survey_questions[question_number] = new_question
        print("Question edited successfully!")
    else:
        print("Invalid question number!")

def display_questions():
    print("Survey Questions:")
    for i, question in enumerate(survey_questions):
        print(f"{i + 1}. {question}")

def save_data():
    if not participants:
        print("No participants found!")
        return

    filename = input("Enter the filename to save the data: ")
    with open(filename, "w") as file:
        for participant in participants:
            file.write(f"Participant Name: {participant['name']}\n")
            file.write("Responses:\n")
            for i, response in enumerate(participant["responses"]):
                question = survey_questions[i]
                file.write(f"{i + 1}. {question}\n")
                file.write(f"   Response: {response}\n")
            file.write("\n")
    print("Data saved successfully!")

def load_data():
    filename = input("Enter the filename to load the data: ")
    try:
        with open(filename, "r") as file:
            data = file.read()
        print(data)
    except FileNotFoundError:
        print("File not found!")

def display_menu():
    print("1. Take Survey")
    print("2. Display Results")
    print("3. Add Question")
    print("4. Delete Question")
    print("5. Edit Question")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        take_survey()
    elif choice == "2":
        display_results()
    elif choice == "3":
        add_question()
    elif choice == "4":
        delete_question()
    elif choice == "5":
        edit_question()
    elif choice == "6":
        save_data()
    elif choice == "7":
        load_data()
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
