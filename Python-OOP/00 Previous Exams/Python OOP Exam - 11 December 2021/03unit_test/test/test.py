from project.team import Team
from unittest import main, TestCase


class TestTeam(TestCase):

    def setUp(self):
        self.team = Team("Suzuki")
        self.team2 = Team("Yamaha")

    def test_initialisation(self):
        self.assertEqual("Suzuki", self.team.name)

    def test_name_setter_for_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            test = Team("1Sliven")

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member_is_valid(self):
        members = {"Member01": 20, "Member02": 30, "Member03": 18}
        existing_member = {"Member01": 20}
        result = self.team.add_member(**members)
        expected_result = "Successfully added: Member01, Member02, Member03"
        self.assertEqual(expected_result, result)
        self.team.add_member(**existing_member)
        self.assertEqual(members, self.team.members)

    def test_remove_member_for_existing_member(self):
        members = {"Member01": 20, "Member02": 30, "Member03": 18}
        self.team.add_member(**members)

        result = self.team.remove_member("Member02")
        self.assertEqual("Member Member02 removed", result)
        self.assertEqual({"Member01": 20, "Member03": 18}, self.team.members)

    def test_remove_member_for_non_existing_member(self):
        result = self.team.remove_member("Member")
        self.assertEqual("Member with name Member does not exist", result)

    def test__gt__(self):
        members01 = {"Member01": 20, "Member02": 30, "Member03": 18}
        members02 = {"Member09": 20, "Member10": 30}
        self.team.add_member(**members01)
        self.team2.add_member(**members02)

        self.assertEqual(True, self.team > self.team2)
        self.assertEqual(False, self.team2 > self.team)

    def test__len__(self):
        members = {"Member01": 20, "Member02": 30, "Member03": 18}
        self.team.add_member(**members)
        self.assertEqual(3, len(self.team))

    def test__add__(self):
        members01 = {"Member01": 20, "Member02": 30, "Member03": 18}
        members02 = {"Member07": 20, "Member10": 30}
        self.team.add_member(**members01)
        self.team2.add_member(**members02)

        test_team = self.team.__add__(self.team2)
        test_members = {"Member01": 20, "Member02": 30, "Member03": 18, "Member07": 20, "Member10": 30}

        self.assertEqual("SuzukiYamaha", test_team.name)
        self.assertEqual(test_members, test_team.members)

    def test__str__(self):
        members = {"Member01": 20, "Member02": 30, "Member03": 20, "Member04": 30, "Member05": 60}
        self.team.add_member(**members)

        expected_result = f"Team name: Suzuki\n" \
                          f"Member: Member05 - 60-years old\n" \
                          f"Member: Member02 - 30-years old\n" \
                          f"Member: Member04 - 30-years old\n" \
                          f"Member: Member01 - 20-years old\n" \
                          f"Member: Member03 - 20-years old"

        self.assertEqual(expected_result, str(self.team))


if __name__ == '__main__':
    main()
