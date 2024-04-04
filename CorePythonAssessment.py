import os
import datetime

def create_note(note_name,note_title, note_content):
    with open("notes.txt", "a") as note_file:
        note_file.write(f"{datetime.datetime.now()} -{note_name}- {note_title} - {note_content}\n")

def view_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as note_file:
            print("\nAll Notes:")
            for note in note_file.readlines():
                print(note.strip())
    else:
        print("\nNo notes found.")

def main():
    while True:
        print("\n Welcome to Python E-Note")
        print("1. Generate Note")
        print("2. View Notes")
        print("3. Exit")
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            note_name = input("Enter Python E-Note Generater Name :")
            note_title = input("Enter Python E-note Title : ")
            note_content =input("Enter E-Note Content : ")
            create_note(note_name,note_title, note_content)
            print("\nNote added successfully.")
        elif user_choice == "2":
            view_notes()
        elif user_choice == "3":
            print("\nExiting the application.")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
