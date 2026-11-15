import json
from pathlib import Path

class FileHandler:
    def __init__(self):
        self.file_path = Path(__file__).resolve().parent / "data" / "tickets.json"

        # # Create the data directory if it doesn't exist
        self.file_path.parent.mkdir(parents=True,exist_ok=True)

        # Create an empty JSON file if it doesn't exist
        if not self.file_path.exists():
            self.save_tickets([])

    def save_tickets(self,tickets): # our TicketManager already maintains:self.tickets = [],So instead of maintaining another ticket list inside FileHandler, we'll pass the list to its save method.

        with open(self.file_path,"w",encoding="utf-8") as file:
            json.dump(tickets,file,indent=4)

    def load_tickets(self):
        with open(self.file_path,"r",encoding="utf-8") as file:
            tickets = json.load(file)
            return tickets