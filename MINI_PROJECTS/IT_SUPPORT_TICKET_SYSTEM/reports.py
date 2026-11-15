class ReportManager:
    def __init__(self,tickets):
        self.tickets = tickets

    
    def generate_report(self):

        if not self.tickets:
            print("No tickets available.")
            return

        status_counts = { # Status counting
            "Open": 0,
            "In Progress": 0,
            "Resolved": 0,
            "Closed": 0
        }

        priority_counts = { # Priority counting
            "High": 0,
            "Medium": 0,
            "Low": 0
        }

        technician_counts = {} # Technician counting

        for ticket in self.tickets:

            # Count tickets by status
            status = ticket["status"]

            if status in status_counts:
                status_counts[status] += 1

            # Count tickets by priority
            priority = ticket["priority"]

            if priority in priority_counts:
                priority_counts[priority] += 1

            # Count tickets by technician
            technician = ticket.get("assigned_to")

            if not technician:
                technician = "Unassigned"

            if technician in technician_counts:
                technician_counts[technician] += 1
            else:
                technician_counts[technician] = 1

        print("\n========== TICKET REPORT ==========")

        print("Total Tickets:", len(self.tickets))

        print("\n--- Tickets by Status ---")
        for status, count in status_counts.items():
            print(status, ":", count)

        print("\n--- Tickets by Priority ---")
        for priority, count in priority_counts.items():
            print(priority, ":", count)

        print("\n--- Technician Workload ---")
        for technician, count in technician_counts.items():
            print(technician, ":", count)
