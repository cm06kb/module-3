
import pysqlite3

def getdb():
    
    conn = pysqlite3.connect("db/phonebook5.db")
    cursor = conn.cursor()
    return cursor

def finBusinessn(businessName, businessType, location):
    """
    returns all businessName, businessType and location is True
    
    """

def getbusinesses()@
    """
    connects to the database
    """
    db = getdb()
#    specify query
    query = select business
    