
"""Manage hostel residents and update their shared curfew time."""
class Resident:
    """Represent a student living in a university hostel."""
    hostel_name = "Rainbow Hall"
    curfew = "10:00 PM"
    def __init__(self, name, room):
        """Initialize a resident with a name and room number."""
        self.name = name
        self.room = room
    def display_details(self):
        """Display the resident's information."""
        print(
            f"{self.name} | Room {self.room} | "
            f"{self.hostel_name} | Curfew {self.curfew}"
        )
    def display_curfew(self):
        """Display the resident's current curfew."""
        print(f"{self.name} | Curfew {self.curfew}")
# Take resident information from the user.
residents = []
for i in range(3):
    print(f"\nEnter details for resident {i + 1}:")
    name = input("Enter name: ")
    while True:
        try:
            room = int(input("Enter room number: "))
            break
        except ValueError:
            print("Please enter a valid room number.")
    resident = Resident(name, room)
    residents.append(resident)
# Display all resident details.
print("\n--- Resident Details ---")
for resident in residents:
    resident.display_details()
# Update curfew for all residents using one line.
new_curfew = input("\nEnter new curfew time: ")
Resident.curfew = new_curfew
print("\n--- curfew updated ---")
for resident in residents:
    resident.display_curfew()