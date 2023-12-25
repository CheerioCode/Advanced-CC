import csv

class Member:
    def __init__(self, name, address, phone_number):
        self._name = name
        self._address = address
        self._phone_number = phone_number

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @property
    def phone_number(self):
        return self._phone_number

    def __str__(self):
        return f"{self._name}, {self._address}. {self._phone_number}"