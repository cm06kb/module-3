from sqlite3 import connect
from os.path import exists
from math import sin, cos, sqrt, atan2, radians

# this is a global variable
db_path = "/Users/crypteye/Desktop/Phonebook/database/Phonebook.db"

################################################database functions
# this function checks if the database exist


def check_db():
    if exists(db_path):
        return True
    else:
        return False

# this functions establishes a connection to the database and returns a database cursor


def connect_db():
    try:
        connection = connect(db_path)
        cursor = connection.cursor()
        return (connection, cursor)
    except:
        return None

# this function executes a query on our database and returns the results in a list


def query_db(query):
    try:
        connection, cursor = connect_db()
        results = cursor.execute(query).fetchall()
        connection.close()
        return results
    except:
        return None

# (think about modifying this function to also deal with queries that have parameters)
################################################end database functions




################################################just handy functions
# this function calculates the distance between two points given their longitudes and latitudes


def distance(lat1,long1,lat2,long2):

    R = 6373.0 # approximate radius of earth in km

    dlon, dlat = radians(long2) - radians(long1), radians(lat2) - radians(lat1)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    a=abs(a)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    hdist = R * c
    return hdist

# thiis function takes in a postcode and calculate sthe distance between it and all postcodes in the database.
# returns all postcodes sorted in ascending order of the parsed postcode


def get_nearest_neighbors(postcode):
    # get all postcodes in database
    query = "SELECT postcode, latitude, longitude FROM postcodes"
    results = query_db(query)

    # get longitude and latitude of given postcode
    test = [i for i in results if i[0].lower().strip() == postcode.lower().strip()]
    if len(test) > 0:

        # select latitude and longitudes of matched postcode
        coords1 = (test[0][1],test[0][2])

        distances = [distance(test[0][1],test[0][2],i[1], i[2]) for i in results]
        results = [results[i]+(distances[i],) for i in range(len(distances))]
        results.sort(key=lambda x: x[-1])

        return results
    else:
        print("No Postcode Match fOUND")

# ############################################### endjust handy functions


# this function gets all businesses from the database sorted alphebateically


def get_businesses():
    try:
        connection, cursor = connect_db()
        query = "SELECT business_name, business_category, address_line_2 from business order by business_name;"
        results = query_db(query)
        return results
    except:
        return None

# this function gets all people in the database (your turn)


def get_people():
    try:
        # connect to database, define and execute a query, store result sin a variable results and return it
        # dont forget to close your connection.
        return 0
    except:
        # return something that tells you that your code has not worked as you intended
        return 0

# this function gets all business locations in your database


def get_business_locations():
    try:
        connection, cursor = connect_db()
        query = "SELECT address_line_3, address_line_2 from business order by address_line_3, address_line_2;"
        results = query_db(query)
        return list(set(results))
    except:
        return None

# this function gets all people in the database (your turn)


def get_people_locations():
    try:
        # connect to database, define and execute a query, store results in a variable results and return it
        # BUT here we want only unique combinations of (address_line_3, address_line_2),
        # dont forget to close your connection.
        return 0
    except:
        # return something that tells you that your code has not worked as you intended
        return 0


def find_business(location=None, category=None):

    if location:
        print("hello")
    elif category:
        print("hello")
    elif location and category:
        print("hello")


print(check_db())

# what is the total number of potential customers available to all computer businesses in England?
