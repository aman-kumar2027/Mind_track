import csv
import datetime
import random
# FILE PATHS
JOURNAL_FILE = "journal.txt"
MOOD_FILE = "mood.csv"
# JOURNAL FUNCTIONS
# ==========================

def write_journal():
    entry = input("\nWrite your journal entry:\n> ")
    date = datetime.date.today().strftime("%Y-%m-%d")
    
    with open(JOURNAL_FILE, "a") as file:
        file.write(f"{date} - {entry}\n")
    
    print("\n✔ Entry saved!\n")


def view_journal():
    print("\n====== Journal Entries ======\n")
    try:
        with open(JOURNAL_FILE, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No entries found yet.\n")
# MOOD TRACKER FUNCTIONS
def log_mood():
    mood = input("\nHow do you feel today? (happy/sad/anxious/neutral/angry): ").lower()
    date = datetime.date.today().strftime("%Y-%m-%d")

    with open(MOOD_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

    print("\n✔ Mood saved!\n")


def view_mood_entries():
    print("\n====== Mood Log ======\n")
    try:
        with open(MOOD_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]} → {row[1]}")
    except FileNotFoundError:
        print("No mood entries found.\n")
# POSITIVE AFFIRMATIONS
affirmations = [
    "You are doing your best, and that is enough.",
    "Small steps still move you forward.",
    "You are capable of amazing things.",
    "Your feelings are valid.",
    "Progress is progress, no matter how slow."
]

def give_affirmation():
    print("\n💛 " + random.choice(affirmations) + "\n")
# STRESS TEST
def stress_test():
    print("\nAnswer on a scale of 1 (Never) to 5 (Always)\n")

    questions = [
        "I feel overwhelmed by tasks.",
        "I find it hard to relax.",
        "I feel anxious about the future.",
        "I have trouble sleeping due to stress.",
        "Small problems irritate me easily."
    ]

    score = 0
    for q in questions:
        value = int(input(q + " → "))
        score += value

    print("\n===== Stress Test Result =====")

    if score <= 10:
        print("🟢 Low Stress — You're doing great! Keep maintaining balance.\n")
    elif score <= 18:
        print("🟡 Moderate Stress — Take breaks & practice self-care.\n")
    else:
        print("🔴 High Stress — Consider talking to someone or seeking support.\n")
# MAIN MENU
def main():
    while True:
        print("""
===== MindTrack CLI =====

1. Write Journal Entry
2. View Journal Entries
3. Log Mood
4. View Mood Entries
5. Get Positive Affirmation
6. Take Stress Questionnaire
7. Exit
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
            print("\nGoodbye! Stay mindful 💛\n")
            break

        else:
            print("\nInvalid option. Try again.\n")


if __name__ == "__main__":
    main()
