# List to store all my study sessions
study_sessions = []

# Directing me to see session details and handle invalid duration inputs
def add_session():
    print("\n--- Add a new study session ---")
    subject = input("Enter subject name: ")
    topic = input("Enter topic covered: ")
    date = input("Enter date or day (e.g., Monday or 31/08): ")

    while True:
        try:
            duration = int(input("Enter duration in minutes: "))
            if duration > 0:
                break
            else:
                print("Duration must be greater than 0. Try again.")
        except ValueError:
            print("Invalid input! Please enter a whole number (e.g., 45).")

    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration
    }

    study_sessions.append(session)
    print("session successfully added!")


# Looping through the list and displays all recorded sessions 
def view_sessions():
    print("\n--- All Study Sessions ---")
    if not study_sessions:
        print("No sessions recorded yet.")
    else:
        for session in study_sessions:
            print(f"Subject: {session['subject']} | Topic: {session['topic']} | Date: {session['date']} | Duration: {session['duration']} mins")


# This helps me to search for a specific subject using case-insensitive string matching
def search_sessions():
    print("\n--- Search Sessions ---")
    search_term = input("Enter the subject to search for: ")
    found = False

    for session in study_sessions:
        if session['subject'].lower() == search_term.lower():
            print(f"Topic: {session['topic']} | Date: {session['date']} | Duration: {session['duration']} mins")
            found = True

    if not found:
        print(f"No sessions found for '{search_term}'.")


# I use this to calculate the total number of sessions and tally the total study time
def view_statistics():
    print("\n--- Study Statistics ---")
    if not study_sessions:
        print("No sessions to calculate yet.")
        return
    
    total_time = 0
    for session in study_sessions:
        total_time += session['duration']

    print(f"Total sessions completed: {len(study_sessions)}")
    print(f"Total time studied: {total_time} minutes")



# This is my main menu loop that directs me to different features
def main():
    print("Welcome to the Smart Study Planner!")


    while True:
        print("\n--- Main Menu ---")
        print("1. Add a study session")
        print("2. View all sessions")
        print("3. Search Sessions by Subject")
        print("4. View statistics")
        print("5. Save and exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_session()
        elif choice == "2":
            view_sessions()
        elif choice == "3":
            search_sessions()
        elif choice == "4":
            view_statistics()
        elif choice == "5":
            print("Saving and exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5")

#This is the entry point of my program
if __name__ == "__main__":
    main()