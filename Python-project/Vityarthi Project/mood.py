import csv
import datetime

MOOD_FILE = "mood.csv"


def log_mood():
    mood = input(
        "\nHow do you feel today? "
        "(happy/sad/anxious/neutral/angry): "
    ).lower()

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
