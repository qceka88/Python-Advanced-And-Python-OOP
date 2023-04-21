from project.robot import Robot
from unittest import main, TestCase


class TestRobot(TestCase):

    def setUp(self) -> None:
        self.robot = Robot("A35", "Education", 5, 0.0)
        self.robot02 = Robot("B35", "Military", 10, 50.5)

    def test__class__attributes(self):
        expected_result01 = ['Military', 'Education', 'Entertainment', 'Humanoids']
        expected_result02 = 1.5

        result01 = self.robot.ALLOWED_CATEGORIES
        result02 = self.robot.PRICE_INCREMENT

        self.assertEqual(expected_result01, result01)
        self.assertEqual(expected_result02, result02)

    def test_initialisation_is_correct(self):
        self.assertEqual("A35", self.robot.robot_id)
        self.assertEqual("Education", self.robot.category)
        self.assertEqual(0.0, self.robot.price)
        self.assertEqual(50.5, self.robot02.price)

    def test_category_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            test = Robot("test", "Not valid", 5, 5.5)

        expected_result = "Category should be one of " \
                          "'['Military', 'Education', 'Entertainment', 'Humanoids']'"

        self.assertEqual(expected_result, str(ve.exception))

    def test_price_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            test = Robot("test", "Entertainment", 5, -0.5)

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_method_for_existing_part(self):
        self.robot.upgrade("test", 1.5)
        result = self.robot.upgrade("test", 1.5)

        self.assertEqual("Robot A35 was not upgraded.", result)

    def test_upgrade_method_for_adding_parts(self):
        components_data = [("test01", 10), ("test02", 20), ("test03", 30), ("test04", 40)]

        for component, price in components_data:
            expected_result = f'Robot A35 was upgraded with {component}.'
            result = self.robot.upgrade(component, price)

            self.assertEqual(expected_result, result)

        expected_result02 = ["test01", "test02", "test03", "test04"]
        result02 = self.robot.hardware_upgrades
        self.assertEqual(expected_result02, result02)
        self.assertEqual(150, self.robot.price)

    def test_update_for_insufficient_capacity(self):
        result = self.robot.update(1.5, 10)
        self.assertEqual("Robot A35 was not updated.", result)

    def test_update_for_older_version(self):
        self.robot.software_updates = [1.5, 2.5, 3.5, 4.5]
        result = self.robot.update(3.1, 5)

        self.assertEqual("Robot A35 was not updated.", result)

    def test_update_for_valid_data(self):
        updates_data = [(1.5, 1), (2.5, 1), (3.5, 1), (4.5, 1)]

        for version, volume in updates_data:
            expected_result = f'Robot A35 was updated to version {version}.'
            result = self.robot.update(version, volume)

            self.assertEqual(expected_result, result)

        self.assertEqual(1, self.robot.available_capacity)
        self.assertEqual([1.5, 2.5, 3.5, 4.5], self.robot.software_updates)

    def test__gt__method_other_is_expensive(self):
        expected_result = f'Robot with ID A35 is cheaper than Robot with ID B35.'
        # result = self.robot.__gt__(self.robot02)

        result = self.robot > self.robot02
        self.assertEqual(expected_result, result)

    def test__gt__method_for_equality(self):
        self.robot.price = 50.5

        expected_result = f'Robot with ID A35 costs equal to Robot with ID B35.'
        result = self.robot > self.robot02

        self.assertEqual(expected_result, result)

    def test__gt_method_other_is_cheaper(self):
        expected_result = 'Robot with ID B35 is more expensive than Robot with ID A35.'
        result = self.robot02 > self.robot

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
