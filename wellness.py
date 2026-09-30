import random

affirmations = [
    "You are doing your best, and that is enough.",
    "Small steps still move you forward.",
    "You are capable of amazing things.",
    "Your feelings are valid.",
    "Progress is progress, no matter how slow."
]


def give_affirmation():
    print("\n" + random.choice(affirmations) + "\n")


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

    for question in questions:
        while True:
            try:
                value = int(input(question + " → "))

                if 1 <= value <= 5:
                    score += value
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")

    print("\n====== Stress Test Result ======")

    if score <= 10:
        print("Low Stress — Keep maintaining balance.\n")
    elif score <= 18:
        print("Moderate Stress — Take breaks and practice self-care.\n")
    else:
        print("High Stress — Consider talking to someone or seeking support.\n")
