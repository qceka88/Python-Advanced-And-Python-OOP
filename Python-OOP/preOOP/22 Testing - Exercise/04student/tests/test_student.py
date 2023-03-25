
from project.student import Student
from unittest import main, TestCase


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("TestName", {"python": ["first note"]})
        self.student_no_courses = Student("TestName")

    def test_initialisation_is_correct(self):
        self.assertEqual("TestName", self.student.name)
        self.assertEqual(["first note"], self.student.courses["python"])
        self.assertEqual({}, self.student_no_courses.courses)

    def test_enroll_method_for_existing_course_notes_input(self):
        result = self.student.enroll("python", ["second note", "third note"])

        self.assertEqual(["first note", "second note", "third note"], self.student.courses["python"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_method_for_adding_course_notes(self):
        result = self.student.enroll("JS", "Y")

        self.assertEqual("Y", self.student.courses["JS"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_method_for_creating_course(self):
        result = self.student_no_courses.enroll("C#", "", "N")

        self.assertEqual("C#", *self.student_no_courses.courses.keys())
        self.assertEqual([], self.student_no_courses.courses["C#"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_method_for_invalid_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("C#", "test note")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_method_for_adding_notes(self):
        result = self.student.add_notes("python", "test note")

        self.assertEqual("test note", self.student.courses["python"][-1])
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_method_for_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_no_courses.leave_course("python")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_method_for_removing_existing_course(self):
        result = self.student.leave_course("python")

        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)


if __name__ == '__main__':
    main()
