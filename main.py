from journal import write_journal, view_journal
from mood import log_mood, view_mood_entries
from wellness import give_affirmation, stress_test


def main():
    while True:
        print("""
========== MindTrack CLI ==========

1. Write Journal Entry
2. View Journal Entries
3. Log Mood
4. View Mood Entries
5. Get Positive Affirmation
6. Take Stress Questionnaire
7. Exit

===================================
""")

        choice = input("Choose an option: ")

        if choice == "1":
            write_journal()
        elif choice == "2":
            view_journal()
        elif choice == "3":
            log_mood()
        elif choice == "4":
            view_mood_entries()
        elif choice == "5":
            give_affirmation()
        elif choice == "6":
            stress_test()
        elif choice == "7":
            print("\nGoodbye! Stay mindful 😊\n")
            break
        else:
            print("\nInvalid option. Try again.\n")


if __name__ == "__main__":
    main()
