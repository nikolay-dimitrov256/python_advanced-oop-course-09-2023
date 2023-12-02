from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student1 = Student('Nikolay', {'Python Advanced': ['n1', 'n2', 'n3'], 'Python OOP': ['n1']})
        self.student2 = Student('Nikolay')

    def test_correct_init(self):
        self.assertEqual('Nikolay', self.student1.name)
        self.assertEqual({'Python Advanced': ['n1', 'n2', 'n3'], 'Python OOP': ['n1']}, self.student1.courses)
        self.assertEqual('Nikolay', self.student2.name)
        self.assertEqual({}, self.student2.courses)

    def test_enroll_method_with_existing_course_expected_notes_update(self):
        expected = {'Python Advanced': ['n1', 'n2', 'n3'], 'Python OOP': ['n1', 'some note', 'some other note']}

        result = self.student1.enroll('Python OOP', ['some note', 'some other note'], add_course_notes='n')

        self.assertEqual('Course already added. Notes have been updated.', result)
        self.assertEqual(expected, self.student1.courses)

    def test_enroll_method_with_new_course_and_notes_empty_add_notes(self):
        expected_courses = {'C++ Basics': ['n1', 'n2', 'n3']}

        result = self.student2.enroll('C++ Basics', ['n1', 'n2', 'n3'])

        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual(expected_courses, self.student2.courses)

    def test_enroll_method_with_new_course_and_notes_add_notes_y(self):
        expected_courses = {'C++ Basics': ['n1', 'n2', 'n3']}

        result = self.student2.enroll('C++ Basics', ['n1', 'n2', 'n3'], add_course_notes='Y')

        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual(expected_courses, self.student2.courses)

    def test_enroll_method_with_new_course_and_no_notes(self):
        expected_courses = {'C++ Basics': []}

        result = self.student2.enroll('C++ Basics', ['n1', 'n2', 'n3'], add_course_notes='N')

        self.assertEqual(result, 'Course has been added.')
        self.assertEqual(expected_courses, self.student2.courses)

    def test_add_notes_method_in_existing_course(self):
        expected = {'Python Advanced': ['n1', 'n2', 'n3'], 'Python OOP': ['n1', 'some note']}

        result = self.student1.add_notes('Python OOP', 'some note')

        self.assertEqual('Notes have been updated', result)
        self.assertEqual(expected, self.student1.courses)

    def test_add_notes_method_in_unexisting_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student2.add_notes('C++ Basics', 'some note')

        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))
        self.assertEqual({}, self.student2.courses)

    def test_leave_course_method_with_existing_course(self):
        expected_courses = {'Python OOP': ['n1']}
        result = self.student1.leave_course('Python Advanced')

        self.assertEqual('Course has been removed', result)
        self.assertEqual(expected_courses, self.student1.courses)

    def test_leave_course_method_unexisting_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student2.leave_course('C++ Basics')

        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))
        self.assertEqual({}, self.student2.courses)


if __name__ == '__main__':
    main()
