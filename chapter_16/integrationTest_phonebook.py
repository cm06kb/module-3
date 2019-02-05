
#----------------chapter 16 - integration testing------------------------------

from test_phonebook_database import *


class TestEngine():
    def __init__(self):
        self.pb = Phonebook()

    def test_check_db(self):
        self.checked = self.pb.check_db()
        return self.checked
    
    def test_connect_db(self):
        if self.checked:
            self.connected = self.pb.connect_db()
            if connected:
                self.connected = True
                return self.connected
            else:
                self.connected = False
                return self.connected
        else:
            print("Databasedoes not exist")
    
    def test_query_db(self):
        query = "SELECT * FROM business;"
        results = self.pb.query_db(query)
        if results:
            self.queried = True
        else:
            self.query = False
    
    def run_tests(self):
        self.test_check_db()
        self.test_connect_db()
        self.test_query_db()

if __name__ == "__main__":
    newTest = TestEngine()
    newTest.run_tests()
    