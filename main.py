

import json
import os
from datetime import datetime

FILE_NAME = "practice_data.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


def save_data(records):
    with open(FILE_NAME, "w") as file:
        json.dump(records, file, indent=4)


def add_practice(records):
    print("\n--- Add DSA Practice ---")

    topic = input("Enter topic: ").strip()
    question = input("Enter question name: ").strip()
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ").strip()
    result = input("Did you solve it correctly? (yes/no): ").strip().lower()

    try:
        minutes = int(input("Time taken in minutes: "))

        if minutes <= 0:
            print("Time must be greater than zero.")
            return

    except ValueError:
        print("Please enter time as a whole number.")
        return

    if not topic or not question:
        print("Topic and question name cannot be empty.")
        return

    if result not in ("yes", "no"):
        print("Please enter yes or no.")
        return

    record = {
    "topic": topic,
    "question": question,
    "difficulty": difficulty,
    "correct": result == "yes",
    "minutes": minutes,
    "date": datetime.now().strftime("%Y-%m-%d")
}
    records.append(record)
    save_data(records)

    print("Practice record saved successfully!")


def show_summary(records):
    if not records:
        print("\nNo practice records found. Add some practice first.")
        return

    topics = {}

    for record in records:
        topic = record["topic"]

        if topic not in topics:
            topics[topic] = {
                "attempts": 0,
                "correct": 0
            }

        topics[topic]["attempts"] += 1

        if record["correct"]:
            topics[topic]["correct"] += 1

    print("\n--- YOUR LEARNING SUMMARY ---")
    print(f"Total questions attempted: {len(records)}")

    for topic, data in topics.items():
        attempts = data["attempts"]
        correct = data["correct"]
        accuracy = (correct / attempts) * 100

        print(f"\nTopic: {topic}")
        print(f"Questions attempted: {attempts}")
        print(f"Correct answers: {correct}")
        print(f"Accuracy: {accuracy:.2f}%")
    weakest_topic = min(
        topics,
        key=lambda topic: topics[topic]["correct"] / topics[topic]["attempts"]
    )

    weakest_accuracy = (
        topics[weakest_topic]["correct"]
        / topics[weakest_topic]["attempts"]
    ) * 100

    print(f"\nTopic needing most practice: {weakest_topic}")
    print(f"Accuracy: {weakest_accuracy:.2f}%")


def main():
    records = load_data()

    while True:
        print("\n===== AI PERSONAL LEARNING TWIN =====")
        print("1. Add practice")
        print("2. View learning summary")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_practice(records)

        elif choice == "2":
            show_summary(records)

        elif choice == "3":
            print("Your learning data has been saved. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()