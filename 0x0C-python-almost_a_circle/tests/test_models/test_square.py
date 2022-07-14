import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquareMethods(unittest.TestCase):

    def test_square(self):
        s1 = Square(5)

        # check width and height are the same
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

        # check area method works as intended
        self.assertEqual(s1.area(), 25)

        # check an error is raised when trying to
        # intialize with a non integer val
        with self.assertRaises(TypeError, msg="height must be an integer"):
            s1.height = 'hi'

        with self.assertRaises(TypeError, msg="height must be an integer"):
            s2 = Square("hello")

        # teset getter
        s1.size = 8
        self.assertEqual(s1.height, 8)

        # test size.setter
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s1.size = "hello"
        with self.assertRaises(ValueError, msg="width must be > 0"):
            s1.size = -5

    def test_update_args(self):
        # create instance
        s1 = Square(5)

        # test Id is updated
        s1.update(89, 2)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.id, 89)

        # test width is updated
        s1.update(89, 2)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.size, 2)

        # test x is updated
        s1.update(89, 2, 3)
        self.assertEqual(s1.x, 3)

        # test y is updated
        s1.update(89, 2, 4, 5)
        self.assertEqual(s1.y, 5)

        # check ValueError is raised when update is sent with negative number
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            s1.update(89, 2, 4, -2)

        # check TypeError is raised when update is sent with non integer value
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s1.update(89, 'hi')

    def test_update_kwargs(self):
        # create instance
        s1 = Square(5)

        # test size is updated with args
        s1.update(89, 2)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.id, 89)

        # Test width is updated with kwargs
        s1.update(size=5)
        self.assertEqual(s1.height, 5)

        # test width and x are updated
        s1.update(size=1, x=2)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.x, 2)

        # test id, y, width and x are updated
        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.x, 3)

        # check ValueError is raised when update is called with negative number
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            s1.update(y=-2)

        # check TypeError is raised when update is sent with non integer value
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s1.update(size='hi')

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 1)

        s1_dictionary = s1.to_dictionary()
        self.assertEqual(
            s1_dictionary, {'x': 2, 'y': 1, 'id': 1, 'size': 10})

        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(
            s2_dictionary, {'x': 2, 'y': 1, 'id': 1, 'size': 10})
        self.assertFalse(s1 == s2)
