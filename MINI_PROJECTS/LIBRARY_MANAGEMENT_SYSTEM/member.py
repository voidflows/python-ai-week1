# Member: Rahul has an ID and a name. He doesn't manage the library.Represents one member and stores their details
# Library: The library registers Rahul, stores his information, and checks whether he's already registered.Registers members and manages the collection of members

class Member:
    def __init__(self, member_id, member_name):
        self.member_id = member_id.strip().upper()
        self.member_name = member_name.strip()

    def to_dict(self):
        return {
            "name": self.member_name
        }