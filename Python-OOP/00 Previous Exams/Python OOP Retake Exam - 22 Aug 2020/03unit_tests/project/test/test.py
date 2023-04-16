from project.student_report_card import StudentReportCard
from unittest import main, TestCase


class TestStudentReportCard(TestCase):

    def setUp(self) -> None:
        self.student01 = StudentReportCard("Name01", 12)
        self.student02 = StudentReportCard("Name02", 1)
        self.student02.grades_by_subject = {"math": [4.50, 5.50],
                                            "history": [3.50, 4.50],
                                            "english": [2.50, 3.50]}

    def test_initialisation_is_correct(self):
        self.assertEqual("Name01", self.student01.student_name)
        self.assertEqual(12, self.student01.school_year)
        self.assertEqual({}, self.student01.grades_by_subject)

    def test_student_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            test = StudentReportCard("", 5)

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_school_year_setter(self):
        invalid_years = [0, 13]
        for year in invalid_years:
            with self.assertRaises(ValueError) as ve:
                test = StudentReportCard("TestName", year)

            self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_add_grade(self):
        subjects_and_grades = {"math": [4.50, 5.50],
                               "history": [3.50, 4.50],
                               "english": [2.50, 3.50]}

        for subject, grades in subjects_and_grades.items():
            for grade in grades:
                self.student01.add_grade(subject, grade)

        self.assertEqual(subjects_and_grades, self.student01.grades_by_subject)

    def test_average_grade_by_subject(self):
        expected_result = f"math: 5.00\nhistory: 4.00\nenglish: 3.00"
        result = self.student02.average_grade_by_subject()

        self.assertEqual(expected_result, result)

    def test_average_grade_by_subject_non_existing_grades(self):
        self.assertEqual("", self.student01.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        result = self.student02.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 4.00", result)

    def test__repr__(self):
        expected_result = "Name: Name02\n" \
                          "Year: 1\n" \
                          "----------\n" \
                          "math: 5.00\nhistory: 4.00\nenglish: 3.00\n" \
                          "----------\n" \
                          "Average Grade: 4.00"
        result = self.student02.__repr__()

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
