import unittest
from models.rectangle import Rectangle


class testRectangleMethods(unittest.TestCase):

    def test_all(self):
        r1 = Rectangle(10, 2, 20, 30)

        # Check getter for height works
        self.assertEqual(r1.height, 2)

        # check setter for height works
        r1.height = 5
        self.assertEqual(r1.height, 5)

        # Check getter for width works
        self.assertEqual(r1.width, 10)

        # check setter for width works
        r1.width = 12
        self.assertEqual(r1.width, 12)

        # Check getter for x works
        self.assertEqual(r1.x, 20)

        # check setter for x works
        r1.x = 25
        self.assertEqual(r1.x, 25)

        # Check getter for y works
        self.assertEqual(r1.y, 30)

        # check setter for y works
        r1.y = 35
        self.assertEqual(r1.y, 35)

    def test_area(self):
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_height(self):
        r3 = Rectangle(10, 2)

        # check an exception is raised when trying to access
        # a private attribute
        with self.assertRaises(AttributeError):
            print(r3.__height)

        # check an exception is raised when height not an int
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r3.height = 'hi'

        # check an exception is raised when height is less than 0 or 0
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r3.height = 0

    def test_width(self):
        r2 = Rectangle(10, 2)

        # check an exception is raised when trying to access
        # a private attribute
        with self.assertRaises(AttributeError):
            print(r2.__width)

        # check an exception is raised when width not an int
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r2.width = 'hi'

        # check an exception is raised when width is less than 0 or 0
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r2.width = 0

    def test_x(self):
        # Check getter works
        r4 = Rectangle(10, 2)

        # check an exception is raised when trying to access
        # a private attribute
        with self.assertRaises(AttributeError):
            print(r4.__x)

        # check an exception is raised when x not an int
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r4.x = 'hi'

        # check an exception is raised when x is less than 0
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r4.x = -1

    def test_y(self):
        r5 = Rectangle(10, 2)

        # check an exception is raised when trying to access
        # a private attribute
        with self.assertRaises(AttributeError):
            print(r5.__y)

        # check an exception is raised when y not an int
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r5.y = 'hi'

        # check an exception is raised when y is less than 0
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r5.y = -1

    def test_update_args(self):
        # create instance
        r1 = Rectangle(10, 10, 10, 10)

        # test Id is updated
        r1.update(89)
        self.assertEqual(r1.id, 89)

        # test width is updated
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)

        # test height is updated
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)

        # test x is updated
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)

        # test y is updated
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

        # check ValueError is raised when update is sent with negative number
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r1.update(89, 2, 3, 4, -2)

        # check TypeError is raised when update is sent with non integer value
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r1.update(89, 'hi')

    def test_update_kwargs(self):
        # create instance
        r1 = Rectangle(10, 10, 10, 10)

        # test width is updated with args
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)

        # Test width is updated with kwargs
        r1.update(height=5)
        self.assertEqual(r1.height, 5)

        # test width and x are updated
        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        # test id, y, width and x are updated
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)

        # check ValueError is raised when update is called with negative number
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r1.update(y=-2)

        # check TypeError is raised when update is sent with non integer value
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r1.update(width='hi')

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 1)

        r1_dictionary = r1.to_dictionary()
        self.assertEqual(
            r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(
            r2_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        self.assertFalse(r1 == r2)
