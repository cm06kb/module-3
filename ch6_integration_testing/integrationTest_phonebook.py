
#----------------chapter 16 - integration testing------------------------------

from test_phonebook_database import *

def search_by_person(): 
    checked = getdb()
    if checked:
        user_location_coordinates = search_by_location()
        if user_location_coordinates:
            merge_tables, person_name =    
            if merge_tables and person_name:
                person_filtered_list_with_distance=calculate_distance_of_person_from_inputed_location(merge_tables, person_name, user_location_coordinates) 
                if person_filtered_list_with_distance:
                    sort_business_by_distance_from_user(person_filtered_list_with_distance, person_name)
                else:
                            print("calculate_distance_of_person_from_inputed_location function failed")
            else:
                    print("retrieve_person_name function failed")
        else:
            print("search location function failed.")
    else:
        print("cannot connect")

   
search_by_person()   





#class TestEngine():
#    def __init__(self):
#        self.pb = Phonebook()
#
#    def test_check_db(self):
#        self.checked = self.pb.getdb()
#        return self.checked
#    
#    def test_connect_db(self):
#        if self.checked:
#            self.connected = self.pb.connect_db()
#            if connected:
#                self.connected = True
#                return self.connected
#            else:
#                self.connected = False
#                return self.connected
#        else:
#            return False
#            print("Databasedoes not exist")
#    
#    def test_query_db(self):
#        if self.connected:
#            query = "SELECT * FROM business;"
#            results = self.pb.query_db(query)
#            if results:
#                self.queried = True
#            else:
#                self.query = False
#        else:
#            print("Connection Test Failed...")
#    
#    def run_tests(self):
#        self.test_check_db()
#        self.test_connect_db()
#        self.test_query_db()

#if __name__ == "__main__":
#    newTest = TestEngine()
#    newTest.run_tests()
    