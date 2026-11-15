# Dictionary (dict) → Represents one ticket.
# List (list) → Holds multiple ticket dictionaries.
# JSON file → Stores the tickets permanently so they survive application restarts.

from ticket_manager import TicketManager
from reports import ReportManager

manager = TicketManager()
report_manager = ReportManager(manager.tickets)

while True:
    print("\n=================================\nIT SUPPORT TICKET SYSTEM\n=================================")
    print("1.Create Ticket")
    print("2.View All Tickets")
    print("3.Search Ticket")
    print("4.Assign Technician")
    print("5.Update Ticket Status")
    print("6.View Ticket History")
    print("7.Generate Reports")
    print("8.Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        print("\n========== CREATE TICKET ==========")

        employee_name = input("Enter employee name: ")
        title = input("Enter issue title: ")
        priority = input("Enter priority (Low/Medium/High): ")

        ticket = manager.create_ticket(employee_name, title, priority)

        print("\nTicket created successfully!")
        print("Ticket ID:", ticket["ticket_id"])
        print("Status:", ticket["status"])
        
    elif choice == "2":
        print("\n========== VIEW ALL TICKETS ==================")
        manager.view_all_tickets()
    elif choice == "3":
        ticket_id = int(input("Enter ticket id : "))
        manager.search_tickets(ticket_id)
    elif choice == "4":
        print("\n========= ASSIGN TECHNICIAN =============")
        ticketId = input("Enter ticket id : ").strip()
        technicianName = input("Enter technician name to be assigned : ").strip()

        if ticketId.isdigit() and technicianName:
            manager.assign_technician(int(ticketId),technicianName)
        else:
            print("Invalid Ticket ID or Technician Name.")
    elif choice == "5":
        print("\n========== UPDATE TICKET STATUS ==========")

        ticket_id = input("Enter Ticket ID: ").strip()
        new_status = input(
            "Enter New Status (In Progress/Resolved/Closed): "
        ).strip()

        if ticket_id.isdigit():
            manager.update_ticket_status(int(ticket_id), new_status)
        else:
            print("Invalid Ticket ID! Please enter a number.")
    elif choice == "6":
        print("\n========== VIEW TICKET STATUS ==========")
        ticket_id = input("Enter Ticket ID : ")
        if ticket_id.isdigit():
            manager.view_ticket_history(int(ticket_id))
        else:
            print("Invalid Ticket ID")
    elif choice == "7":
        report_manager.generate_report()
    elif choice == "8":
        print("Exit.Thank You!")
        break
    else:
        print("Invalid Choice.Please retry.")

 
#  main.py -->	main(), display_menu()
# ticket_manager.py ->>	create_ticket(), search_ticket(), update_status(), assign_technician()
# file_handler.py	-->> load_tickets(), save_tickets()
# reports.py -->	generate_summary(), tickets_by_priority()
# validators.py -->> validate_priority(), validate_status()
 