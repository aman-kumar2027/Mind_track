import datetime

JOURNAL_FILE = "journal.txt"


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
