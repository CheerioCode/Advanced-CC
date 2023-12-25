from unittest import TestCase
from Roll import Roll

class TestRollMethods(TestCase):
    def setUp(self):
        members = ["Lee", "Steve Rogers", "Dylan", "Bruce Banner"]
        date = "2023-12-21"
        self.roll = Roll(members, date)

    def test_mark_attendance(self):
        self.roll.mark_attendance("Lee", True)
        self.assertTrue(self.roll.members["Lee"])

    def test_get_attendance(self):
        self.roll.mark_attendance("Lee", True)
        self.roll.mark_attendance("Steve Rogers", True)
        attendance = self.roll.get_attendance()
        self.assertEqual(attendance, ["Lee", "Steve Rogers"])

    def test_get_absentees(self):
        self.roll.mark_attendance("Lee", True)
        self.roll.mark_attendance("Steve Rogers", True)
        absentees = self.roll.get_absentees()
        self.assertEqual(absentees, ["Dylan", "Bruce Banner"])

    def test_get_all_members_attendance(self):
        self.roll.mark_attendance("Lee", True)
        self.roll.mark_attendance("Steve Rogers", False)
        all_attendance = self.roll.get_all_members_attendance()
        expected_result = {
            "Lee": "Present",
            "Steve Rogers": "Absent",
            "Dylan": "Absent",
            "Bruce Banner": "Absent"
        }
        self.assertEqual(all_attendance, expected_result)