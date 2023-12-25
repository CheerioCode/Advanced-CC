import csv
from Member import Member

class Club:
    def __init__(self, club_name, members, filename=None):
        self._club_name = club_name
        self._members = members
        self._filename = filename

    @property
    def club_name(self):
        return self._club_name

    @club_name.setter
    def club_name(self, club_name):
        self._club_name = club_name

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, members):
        self._members = members

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    def __str__(self):
        return f"{self._club_name}, {self._members}. {self._filename}"

    @classmethod
    def from_file(cls, club_name, filename):
        members = cls.load_members(filename)
        return cls(club_name, members, filename)

    def save_members(self):
        if self.filename:
            Club.write_members(self.filename, self.members)

    def update_member_address(self, name, address):
        member = self.find_member(name)
        if member is not None:
            member._address = address
            self.save_members()

    def update_member_name(self, name, new_name):
        member = self.find_member(name)
        if member is not None:
            member._name = new_name
            self.save_members()

    def update_member_number(self, name, new_phone_number):
        member = self.find_member(name)
        if member is not None:
            member._phone_number = new_phone_number
            self.save_members()

    @staticmethod
    def load_members(filename):
        members = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 3:
                    members.append(Member(row[0], row[1], row[2]))
        return members

    @staticmethod
    def write_members(filename, members):
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            for member in members:
                writer.writerow([member.name, member.address, member.phone_number])

    def add_member(self, name, address, phone_number):
        self.members.append(Member(name, address, phone_number))
        self.save_members()

    def remove_member(self, name):
        member = self.find_member(name)
        if member is not None:
            self.members.remove(member)
            self.save_members()

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None