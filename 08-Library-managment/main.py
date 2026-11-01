from model import Book, Magazine, ReferenceBook, StudentMember, ResearchStudent, FacultyMember, NotifiedMember
from library_service import LibraryManager
from storage import save_library, load_library


def main():
    library = LibraryManager()

    try:
        load_library(library)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("Data loading error:", error)
        return

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Register Item")
        print("2. Register Member")
        print("3. Borrow Item")
        print("4. Return Item")
        print("5. View Reports")
        print("6. Update Library Name")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("1. Book")
            print("2. Magazine")
            print("3. Reference Book")

            item_choice = input("Select item type: ")
            item_id = input("Enter Item ID: ")
            title = input("Enter Title: ")

            if item_choice == "1":
                item = Book(item_id, title)
            elif item_choice == "2":
                item = Magazine(item_id, title)
            elif item_choice == "3":
                item = ReferenceBook(item_id, title)
            else:
                print("Invalid item type.")
                continue

            try:
                library.register_item(item)
                save_library(library)
                print("Item registered successfully.")
            except ValueError as error:
                print(error)

        elif choice == "2":
            print("1. Student")
            print("2. Research Student")
            print("3. Faculty")
            print("4. Notified Member")

            member_choice = input("Select member type: ")
            member_id = input("Enter Member ID: ")
            name = input("Enter Name: ")

            if member_choice == "1":
                member = StudentMember(member_id, name)
            elif member_choice == "2":
                member = ResearchStudent(member_id, name)
            elif member_choice == "3":
                member = FacultyMember(member_id, name)
            elif member_choice == "4":
                member = NotifiedMember(member_id, name)
            else:
                print("Invalid member type.")
                continue

            try:
                library.register_member(member)
                save_library(library)
                print("Member registered successfully.")
            except ValueError as error:
                print(error)

        elif choice == "3":
            member_id = input("Enter Member ID: ")
            item_id = input("Enter Item ID: ")

            try:
                due_date = library.borrow_item(member_id, item_id)
                save_library(library)
                print("Borrow successful.")
                print("Due Date:", due_date)
            except ValueError as error:
                print("Borrowing failed:", error)

        elif choice == "4":
            item_id = input("Enter Item ID: ")

            try:
                days, fine = library.return_item(item_id)
                save_library(library)
                print("Item returned successfully.")
                print("Overdue Days:", days)
                print("Fine:", fine)
            except ValueError as error:
                print("Return failed:", error)

        elif choice == "5":
            library.display_reports()

        elif choice == "6":
            name = input("Enter new library name: ")
            LibraryManager.set_library_name(name)
            print("Library name updated.")

        elif choice == "7":
            save_library(library)
            print("Library data saved.")
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()