# import unittest library
import unittest
# import all functions from our functions file which we would like to test
#from functions import *


class TestPhonebook(unittest.TestCase):

    # let us test our database functions and ensure that they work the way we want them to
    def database_connection_tests(self):
        self.assertTrue(check_db())
        self.assertIsNotNone(connect_db())
        '''
        db_check = self.assertTrue(check_db())


        # we expect a database defined in the variable db_path in functions.py to exist. Let's test that
        if db_check:
            print("Database Exist.. Testing Connection ............")

            #if the database exist we would like to ensure we can establish a connection to it
            if self.assertIsNotNone(connect_db()):
                print("Connection Established......")
            else:
                print("Could Not Establish a connection to database")
        else:
            print("Dataabase does not exist")
'''

    def test_query_db(self):
        # after establishing a connection, let us ensure that we query our database given an sql input
        # we expect most of our queries to return something: look at the syntax of the try and except block in the 'query_db()' function
        # lets ensure we do not get none
        test_query = "SELECT * FROM business"
        self.assertIsNotNone(query_db(test_query))
        # lets also test that it returns a list, as this is the data type most of our other codes would be programmed to use
        self.assertIsInstance(query_db(test_query), list)

    def test_distance_functions(self):
        # let's also test that our distance function actually calculates the distance between two points
        # i have choosen to implement this test by using the coordinates of a randomly selected postcode, and testing the distance from itself. I expect the answer to be 0.0
        self.assertEqual(distance(51.517907,-0.113471,51.517907,-0.113471), 0.0)
        # lets also test the function returns a float

    def runall(self):

        self.database_connection_tests()
        self.test_distance_functions()


if __name__ == "__main__":
    unittest.main()
