from project.student import Student
from unittest import main, TestCase


# te
class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Georgi", {"Python": ["Basics"]})
        self.student_no_courses = Student("Ivan")

    def test_initialisation_is_correct(self):
        self.assertEqual("Ivan", self.student_no_courses.name)
        self.assertEqual({}, self.student_no_courses.courses)
        self.assertEqual(["Basics"], self.student.courses["Python"])

    def test_enroll_for_existing_course_adding_notes(self):
        result = self.student.enroll("Python", ["note1", "note2"])

        self.assertEqual(["Basics", "note1", "note2"], self.student.courses["Python"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_for_non_existing_course_with_notes(self):
        result = self.student_no_courses.enroll("JavaScript", ["note"])
        result2 = self.student_no_courses.enroll("Ruby", ["note"], "Y")

        self.assertEqual(["note"], self.student_no_courses.courses["JavaScript"])
        self.assertEqual(["note"], self.student_no_courses.courses["Ruby"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual("Course and course notes have been added.", result2)

    def test_enroll_adding_non_existing_course(self):
        result = self.student_no_courses.enroll("JavaScript", "", "N")

        self.assertEqual("JavaScript", *self.student_no_courses.courses.keys())
        self.assertEqual([], self.student_no_courses.courses["JavaScript"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_for_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_no_courses.add_notes("C#", "note1")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_for_existing_course(self):
        result = self.student.add_notes("Python", "note1")

        self.assertEqual("note1", self.student.courses["Python"][-1])
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_no_courses.leave_course("C#")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_existing_courses(self):
        result = self.student.leave_course("Python")

        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)


if __name__ == '__main__':
    main()
