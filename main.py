import json
import os

FILE_NAME = "tickets.json"


# LOAD TICKETS
def load_tickets():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


# SAVE TICKETS
def save_tickets():
    with open(FILE_NAME, "w") as file:
        json.dump(tickets, file, indent=4)


tickets = load_tickets()


# GENERATE TICKET ID
def generate_ticket_id():
    if not tickets:
        return "TKT001"

    numbers = []

    for ticket in tickets:
        number = int(ticket["ticket_id"][3:])
        numbers.append(number)

    next_number = max(numbers) + 1

    return f"TKT{next_number:03d}"


# CREATE TICKET
def create_ticket():
    print("\n--- CREATE NEW TICKET ---")

    employee_name = input("Enter Employee Name: ").strip()

    if not employee_name.strip():
      print("Employee Name cannot be empty!")
      return
    
    if len(employee_name) < 3:
      print("Employee Name must contain at least 3 characters!")
      return
    
    issue = input("Enter Issue Description: ").strip()

    if not issue.strip():
      print("Issue Description cannot be empty!")
      return
    1
    category = input("Enter Category (Hardware/Software/Network): ").strip()
    category=category.capitalize()

    if category not in ["Hardware", "Software", "Network"]:
      print("Invalid Category!")
      return

    priority = input("Enter Priority (Low/Medium/High): ").strip()
    priority=priority.capitalize()

    if priority not in ["Low", "Medium", "High"]:
      print("Invalid Priority!")
      return

    ticket_id = generate_ticket_id()

    ticket = {
        "ticket_id": ticket_id,
        "employee": employee_name,
        "issue": issue,
        "category": category,
        "priority": priority,
        "status": "Pending"
    }

    tickets.append(ticket)
    save_tickets()

    print("\nTicket Created Successfully!")
    print("Ticket ID:", ticket_id)


# VIEW TICKETS
def view_tickets():
    print("\n--- ALL TICKETS ---")

    if not tickets:
        print("No tickets available.")
        return

    for ticket in tickets:
        print("-" * 40)
        print("Ticket ID:", ticket["ticket_id"])
        print("Employee:", ticket["employee"])
        print("Issue:", ticket["issue"])
        print("Category:", ticket["category"])
        print("Priority:", ticket["priority"])
        print("Status:", ticket["status"])


# SEARCH TICKET
def search_ticket():
    print("\n--- SEARCH TICKET ---")

    ticket_id = input("Enter Ticket ID: ")

    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:
            print("\nTicket Found!")
            print("Ticket ID:", ticket["ticket_id"])
            print("Employee:", ticket["employee"])
            print("Issue:", ticket["issue"])
            print("Category:", ticket["category"])
            print("Priority:", ticket["priority"])
            print("Status:", ticket["status"])
            return

    print("Ticket Not Found.")


# UPDATE STATUS
def update_status():
    print("\n--- UPDATE TICKET STATUS ---")

    ticket_id = input("Enter Ticket ID: ")

    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:

            print("1. Pending")
            print("2. In Progress")
            print("3. Resolved")

            choice = input("Select New Status: ")

            if choice == "1":
                ticket["status"] = "Pending"
            elif choice == "2":
                ticket["status"] = "In Progress"
            elif choice == "3":
                ticket["status"] = "Resolved"
            else:
                print("Invalid Choice.")
                return

            save_tickets()
            print("Status Updated Successfully!")
            return

    print("Ticket Not Found.")


# UPDATE PRIORITY
def update_priority():
    print("\n--- UPDATE PRIORITY ---")

    ticket_id = input("Enter Ticket ID: ")

    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:

            print("1. Low")
            print("2. Medium")
            print("3. High")

            choice = input("Select New Priority: ")

            if choice == "1":
                ticket["priority"] = "Low"
            elif choice == "2":
                ticket["priority"] = "Medium"
            elif choice == "3":
                ticket["priority"] = "High"
            else:
                print("Invalid Choice.")
                return

            save_tickets()
            print("Priority Updated Successfully!")
            return

    print("Ticket Not Found.")
# DELETE TICKET
def delete_ticket():
    print("\n--- DELETE TICKET ---")

    ticket_id = input("Enter Ticket ID: ")

    for ticket in tickets:
        if ticket["ticket_id"] == ticket_id:

            confirmation = input(
                "Are you sure you want to delete? (yes/no): "
            )

            if confirmation.lower() == "yes":
                tickets.remove(ticket)
                save_tickets()
                print("Ticket Deleted Successfully!")
            else:
                print("Deletion Cancelled.")

            return

    print("Ticket Not Found.")


# CATEGORY REPORT
def category_report():
    print("\n--- CATEGORY REPORT ---")

    if not tickets:
        print("No tickets available.")
        return

    categories = {}

    for ticket in tickets:
        category = ticket["category"]

        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    for category, count in categories.items():
        print(category, ":", count)


# SUMMARY REPORT
def summary_report():
    print("\n--- SUMMARY REPORT ---")

    total = len(tickets)

    pending = 0
    in_progress = 0
    resolved = 0

    high = 0
    medium = 0
    low = 0

    for ticket in tickets:

        if ticket["status"] == "Pending":
            pending += 1
        elif ticket["status"] == "In Progress":
            in_progress += 1
        elif ticket["status"] == "Resolved":
            resolved += 1

        if ticket["priority"] == "High":
            high += 1
        elif ticket["priority"] == "Medium":
            medium += 1
        elif ticket["priority"] == "Low":
            low += 1

    print("Total Tickets:", total)
    print("Pending Tickets:", pending)
    print("In Progress Tickets:", in_progress)
    print("Resolved Tickets:", resolved)

    print("\nPriority Summary")
    print("High Priority:", high)
    print("Medium Priority:", medium)
    print("Low Priority:", low)

def delete_all_tickets():
    print("\n--- DELETE ALL TICKETS ---")

    if not tickets:
        print("No tickets available to delete.")
        return

    confirmation = input("Delete ALL tickets? (yes/no): ")

    if confirmation.lower() == "yes":
        tickets.clear()
        save_tickets()
        print("All Tickets Deleted Successfully!")
    else:
        print("Deletion Cancelled.")


# MAIN PROGRAM
def main():

    while True:

        print("\n" + "=" * 50)
        print("SMART COMPLAINT & ISSUE TRACKING SYSTEM")
        print("=" * 50)

        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Search Ticket")
        print("4. Update Ticket Status")
        print("5. Update Ticket Priority")
        print("6. Delete Ticket")
        print("7. Category Report")
        print("8. Summary Report")
        print("9. Exit")
        print("10 Delete All Tickets")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            create_ticket()

        elif choice == "2":
            view_tickets()

        elif choice == "3":
            search_ticket()

        elif choice == "4":
            update_status()

        elif choice == "5":
            update_priority()

        elif choice == "6":
            delete_ticket()

        elif choice == "7":
            category_report()

        elif choice == "8":
            summary_report()

        elif choice == "9":
            print("Thank You for Using the System!")
            break
        elif choice== "10":
            delete_all_tickets()

        else:
            print("Invalid Choice. Please Try Again.")


if __name__ == "__main__":
    main()


