import unittest
from test_phonebook_database import *

class PhonebookTest(unittest.TestCase):
    def test_ConnectivityToDb(self):
        self.assertIsNotNone(getdb())
                
    def test_haversine(self):
        self.assertEqual((haversine(51.50853, -0.12574, 51.50853, -0.12574)), 0)
        
    def test_userlocation(self):
#       input user postcode as "N3 1AA"
        self.assertEqual(search_by_location(), (-0.192566, 51.606477))       
        

    def test_query_db(self):
#       check business table exists, if it has been deleted we would return none. 
        self.assertIsNotNone(retrieve_business_cat((51.50853, -0.12574)))
        # lets also test that it returns a tuple, as this is the data type most of our other codes would be programmed to use.
        self.assertIsInstance(retrieve_business_cat((51.50853, -0.12574)),list)

        
if __name__ == "__main__":
    unittest.main()
else:
    print("not working")
    
