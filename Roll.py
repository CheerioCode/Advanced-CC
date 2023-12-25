class Roll:
    def __init__(self, members, date):
        self.members = {member: False for member in members}
        self.date = date

    def mark_attendance(self, member, present=True):
        if member in self.members:
            self.members[member] = present

    def save_members(self):
        if self.date:
            Roll.write_members(f"roll_{self.date}.csv", self.members)


    def get_attendance(self):
        return [member for member, present in self.members.items() if present]

    def get_absentees(self):
        return [member for member, present in self.members.items() if not present]

    def get_all_members_attendance(self):
        return {member: "Present" if present else "Absent" for member, present in self.members.items()}


