import os
from datetime import datetime
FILE_NAME = "journal.txt"
def add_entry():
    entry = input("\nWrite your journal entry:\n")
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d | %H:%M")

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"[{date_time}]\n")
        file.write(entry + "\n")
        file.write("-" * 40 + "\n")

    print("\n Journal entry saved successfully!")


def view_entries():
    if not os.path.exists(FILE_NAME):
        print("\n No journal found.")
        return

    print("\n All Journal Entries:\n")
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        print(file.read())


def search_by_date():
    if not os.path.exists(FILE_NAME):
        print("\n No journal found.")
        return

    search_date = input("\nEnter date (YYYY-MM-DD): ")
    found = False

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("[") and search_date in line:
                print("\n Entry Found:\n")
                print(line.strip())
                print(next(file).strip())
                found = True

    if not found:
        print("\n No entry found for this date.")


def main_menu():
    while True:
        print("\n====== DAILY JOURNAL SYSTEM ======")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Search Entry by Date")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_by_date()
        elif choice == "4":
            print("\n👋 Exiting Journal System. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Try again.")


main_menu()
