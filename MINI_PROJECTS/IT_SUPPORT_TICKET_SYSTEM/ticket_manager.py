from file_handler import FileHandler
from datetime import datetime

class TicketManager:
    def __init__(self):
        #self.tickets = []
        self.file_handler = FileHandler()
        self.tickets = self.file_handler.load_tickets()

    def create_ticket(self,employee_name,title,priority):
        if not self.tickets: # checks whether the list is empty.
            ticket_id = 1001
        else:
            highest_id = 1000

            for ticket in self.tickets: # for loop examines every ticket dictionary.
                if(ticket["ticket_id"] > highest_id):
                    highest_id = ticket["ticket_id"]
            ticket_id = highest_id + 1

        data = {
            "ticket_id" : ticket_id,
            "employee_name" : employee_name,
            "title" : title,
            "priority" : priority,
            "status" : "Open", #Initially all the status should be open
            "assigned_to" : None,
            "history" : []
        }

        self.tickets.append(data)
        self.file_handler.save_tickets(self.tickets)
        return data

    def view_all_tickets(self):
        if not self.tickets:
            print("No Tickets currently available.")
        else:
            for ticket in self.tickets:
                print(f"Ticket ID : {ticket["ticket_id"]} | " 
                      f"Employee name : {ticket["employee_name"]} | "
                      f"Title : {ticket["title"]} | "
                      f"Priority : {ticket["priority"]} | "
                      f"Status : {ticket["status"]} |"
                      f"Assigned To : {ticket["assigned_to"]}")


    def search_tickets(self,ticket_id):
        found = False
        for ticket in self.tickets:
            if ticket["ticket_id"] == ticket_id:
                   print(f"Ticket ID : {ticket["ticket_id"]} | " 
                        f"Employee name : {ticket["employee_name"]} | "
                        f"Title : {ticket["title"]} | "
                        f"Priority : {ticket["priority"]} | "
                        f"Status : {ticket["status"]} | "
                        f"Assigned To : {ticket["assigned_to"]}")
                   found = True
                   break
        if not found:
            print(f"Respected {ticket_id} not found!!!")

    def assign_technician(self, ticket_id, technician_name):
        found = False
        for ticket in self.tickets:
            if(ticket["ticket_id"]) == ticket_id:
                ticket["assigned_to"] = technician_name
                history_record = {
                    "action" : "Technician Assigned",
                    "details" : f"Assigned to {technician_name}",
                    "timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                }
                ticket.setdefault("history", []).append(history_record)
                self.file_handler.save_tickets(self.tickets)
                print("Technician assigned successfully!!!")
                found = True
                break
        if not found:
            print(f"No such {ticket_id} found")

    def update_ticket_status(self, ticket_id, new_status):
        allowed_transitions = {
            "Open" : "In Progress",
            "In Progress" : "Resolved",
            "Resolved"  : "Closed"
        }
        found = False
        for ticket in self.tickets:
            if(ticket["ticket_id"]) == ticket_id:
                found =True
                current_status = ticket["status"]
                if allowed_transitions.get(current_status) == new_status:
                    ticket["status"] = new_status
                    history_record = {
                            "action" : "Technician Assigned",
                            "details" : f"{current_status} to {new_status}",
                            "timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
                                }
                    ticket.setdefault("history", []).append(history_record)
                    self.file_handler.save_tickets(self.tickets)
                    print("Ticket status updated successfully!")
                    print(f"Ticket ID: {ticket_id}")
                    print(f"Old Status: {current_status}")
                    print(f"New Status: {new_status}")
                else:
                    print("Invalid status transition!")
                    print(f"Current Status: {current_status}")

                    if current_status == "Closed":
                        print("This ticket is already closed.")
                    else:
                        print(
                            f"Allowed Next Status: "
                            f"{allowed_transitions.get(current_status)}"
                        )

                break
        if not found:
            print(f"Ticket ID {ticket_id} not found.")

    def view_ticket_history(self,ticket_id):
        for ticket in self.tickets:
            if (ticket["ticket_id"]) == ticket_id:
                history = ticket.get("history",[])
                if not history:
                    print("No history available for this ticket.")
                else:
                    for record in history:
                        print(f"Action : {record['action']}")
                        print(f"Details : {record['details']}")
                        print(f"Timestamp : {record['timestamp']}")
                        print("-----------------------------")
                return
        print(f"Ticket ID {ticket_id} not found.")




