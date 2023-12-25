from Club import Club
from Roll import Roll

def display_menu():
    print("1. List all members")
    print("2. Add a member")
    print("3. Remove a member")
    print("4. Update a member's name")
    print("5. Update a member's address")
    print("6. Update a member's phone number")
    print("7. Mark attendance")
    print("8. List all members and their attendance on a given date")
    print("9. List all members absent on a given date")
    print("10. List all members present on a given date")
    print("0. Exit")oi


def list_all_members(club):
    for member in club.members:
        print(member)


def mark_attendance(club):
    date = input("Enter the date (YYYY-MM-DD): ")
    name = input("Enter the member's name: ")
    if Roll is not None:
        present = input("Is the member present? (y/n): ").lower() == 'y'
        Roll.mark_attendance(name, date, present)
        print(f"Attendance marked for {name} on {date}.")
        Roll.save_rolls()
    else:
        print(f"No roll found for {date}.")

def list_attendance_on_date(club):
    date = input("Enter the date (YYYY-MM-DD): ")
    attendance = Roll.get_attendance(date)
    print(f"Attendance on {date}: {', '.join(attendance)}")


def list_absent_on_date(club):
    date = input("Enter the date (YYYY-MM-DD): ")
    absentees = Roll.get_absentees(date)
    print(f"Absent members on {date}: {', '.join(absentees)}")


def list_present_on_date(club):
    date = input("Enter the date (YYYY-MM-DD): ")
    present_members = Roll.get_attendance(date)
    print(f"Present members on {date}: {', '.join(present_members)}")


def main():
    club_name = 'Club'
    filename = 'members.csv'

    if filename:
        club = Club.from_file(club_name, filename)
    else:
        members = []
        club = Club(club_name, members)

    while True:
        display_menu()
        choice = input("Enter your choice (0-10): ")

        if choice == '0':
            print("Exiting the program. Goodbye!")
            break
        elif choice == '1':
            list_all_members(club)
        elif choice == '2':
            name = input("Enter the member's name: ")
            address = input("Enter the member's address: ")
            phone_number = input("Enter the member's phone number: ")
            club.add_member(name, address, phone_number)
        elif choice == '3':
            name = input("Enter the member's name to remove: ")
            club.remove_member(name)
        elif choice == '4':
            name = input("Enter the member's current name: ")
            new_name = input("Enter the new name: ")
            club.update_member_name(name, new_name)
        elif choice == '5':
            name = input("Enter the member's name: ")
            new_address = input("Enter the new address: ")
            club.update_member_address(name, new_address)
        elif choice == '6':
            name = input("Enter the member's name: ")
            new_phone_number = input("Enter the new phone number: ")
            club.update_member_number(name, new_phone_number)
        elif choice == '7':
            mark_attendance(club)
        elif choice == '8':
            list_attendance_on_date(club)
        elif choice == '9':
            list_absent_on_date(club)
        elif choice == '10':
            list_present_on_date(club)
        else:
            print("Invalid choice. Please enter a number between 0 and 10.")


if __name__ == "__main__":
    main()