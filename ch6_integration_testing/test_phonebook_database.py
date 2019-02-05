import sqlite3
import json
import requests
from math import radians, cos, sin, asin, sqrt
from create_db_phonebook_project import *

person_data_list = json.loads(open('./person_data.json').read())
business_data_list = json.loads(open('./business.json').read())



def getdb():
    """check we can connect to db.
    
    Long details
    
    Args:
        first_arge: descriotpon
        second_arg: description
        
    Return:
        an array with distancase
    """
    try:
        conn = sqlite3.connect('phonebook_project.db')
        c = conn.cursor()
        return c, conn
    except:        
        return False
    

def search_by_person(): 
    user_location_coordinates = search_by_location()
    
    merge_tables, person_name = retrieve_person_name(user_location_coordinates)
    
    person_filtered_list_with_distance=calculate_distance_of_person_from_inputed_location(merge_tables, person_name, user_location_coordinates) 
    
    sort_business_by_distance_from_user(person_filtered_list_with_distance, person_name)
    
def search_by_business_name(): 
    user_location_coordinates = search_by_location()
    print(retrieve_business_name(user_location_coordinates))

    merge_tables, business_name_search = retrieve_business_name(user_location_coordinates)
    
    business_type_filtered_list_with_distance = calculate_distance_of_business_from_user(merge_tables, business_name_search, user_location_coordinates) 
    
    sort_business_by_distance_from_user(business_type_filtered_list_with_distance, business_name_search)
    
def search_by_business_cat(): 
    user_location_coordinates = search_by_location()
    
    merge_tables, business_cat_search  = retrieve_business_cat(user_location_coordinates) 
    
    business_type_filtered_list_with_distance = calculate_distance_of_business_from_user(merge_tables, business_cat_search, user_location_coordinates) 
    
    sort_business_by_distance_from_user(business_type_filtered_list_with_distance, business_cat_search)
    
    
    
def search_by_location():
    """
    input: user location
    output: users coordinates
    """
    user_location = input("Enter city/town or postcode").title()
#    try:
#        if len(user_location) 
   
    endpoint = "https://api.opencagedata.com/geocode/v1/json?q={}&key=9f1c77b5b7df45a490c16449641a9b6f".format(user_location)
    payload = {"q": "{}".format(user_location), "countrycode":"gb", "appid": "9f1c77b5b7df45a490c16449641a9b6f"}
    response = requests.get(endpoint, params=payload)
    user_location = response.json()
    x1 = user_location['results'][0]['geometry']['lng']
    y1 = user_location['results'][0]['geometry']['lat']
    user_location_coordinates = (x1,y1)
    return user_location_coordinates

    
def retrieve_business_cat(user_location_coordinates):
    """
        input: user coorindates
        output:         
    """
    try:
        business_cat_search = input("Enter Type of Business ").title()  
    
        db = getdb()
        c = db[0]
       
        c.execute("SELECT  * FROM business INNER JOIN coordinates ON (business.postcode = coordinates.postcode) WHERE business_category =?",  (business_cat_search,))
        merge_tables = c.fetchall()
        return (merge_tables, business_cat_search)
    
    except:
        return None

def retrieve_business_name(user_location_coordinates):
    """
        input: user coorindates
        output:         
    """
    try:
        business_name_search = input("Enter Business name ")  
    
        db = getdb()
        c = db[0]
       
        c.execute("SELECT  * FROM business INNER JOIN coordinates ON (business.postcode = coordinates.postcode) WHERE business_name =?",  (business_name_search,))
        merge_tables = c.fetchall()
        print(merge_tables)
        return (merge_tables, business_name_search)
    
    except:
        return None

def retrieve_person_name(user_location_coordinates):
    """
        input: user coorindates
        output:         
    """
    try:
        person_name_search = input("Enter person's last name ").title()  
    
        db = getdb()
        c = db[0]
       
        c.execute("SELECT  * FROM person INNER JOIN coordinates ON (person.postcode = coordinates.postcode) WHERE last_name =?",  (person_name_search,))
        merge_tables = c.fetchall()
        return (merge_tables, person_name_search)
    
    except:
        print("hello")
        return None
            
            
#    calculate_distance_of_business_from_user(merge_tables, user_location_coordinates, business_cat_search)  
    
def dynamic_coordinates_data_entry():
     """
         adds unique postcodes from person and business table into coordinates table.
         input: postcodes from person and business table (minus duplicates)
         output: postcodes in  coordinate table.
         
     """
     postcode_list = []
     for item in person_data_list:
         postcode_list.append(item["postcode"])
     
     for item in business_data_list:
         postcode_list.append(item["postcode"])


     unique_postcode_list = set(postcode_list)

     endpoint = "https://api.postcodes.io/postcodes/"
     coor_dict = []
     
     for item in unique_postcode_list:
        payload = item
        
        
        postcode_response = requests.get(endpoint + payload)
        data_postcode = postcode_response.json()
        
        if data_postcode["status"] == 200:
            longitude_val = data_postcode['result']['longitude']
            latitude_val = data_postcode['result']['latitude']
            dic_1 = {"postcode": payload, "longitude": longitude_val, "latitude": latitude_val} 
            coor_dict.append(dic_1)
            return "coordinates", coor_dict, ["postcode", "longitude", "latitude"]
        
        else: 
            pass
            
            



dynamic_coordinates_data_entry()
    
def calculate_distance_of_business_from_user(merge_tables, business_name_search, user_location_coordinates):
    """
        checks whether users search returned any results
        if results are returned, calculates distance of user from each result.
    """
    business_type_filtered_list = []
    for row in merge_tables:
        business_type_filtered_list.append(row)
        
    if business_type_filtered_list==[] :
        print("business name not found")
        
    else:

        business_type_filtered_list_with_distance = []
        for item in business_type_filtered_list:
            distance = int(haversine(user_location_coordinates[0],user_location_coordinates[1], item[9], item[10]))
            x = list(item)
            x.append(distance)
            business_type_filtered_list_with_distance.append(x)
    return business_type_filtered_list_with_distance

def calculate_distance_of_person_from_inputed_location(merge_tables, person_name, user_location_coordinates):
    """
        checks whether users search returned any results
        if results are returned, calculates distance of user from each result.
    """
    person_filtered_list = []
    for row in merge_tables:
        person_filtered_list.append(row)
        
    if person_filtered_list==[] :
        print("No person with this name has been found")
    else:

        person_filtered_list_with_distance = []
        for item in person_filtered_list:
            distance = int(haversine(user_location_coordinates[0],user_location_coordinates[1], item[9], item[10]))
            x = list(item)
            x.append(distance)
            person_filtered_list_with_distance.append(x)
    return person_filtered_list_with_distance
 

def calculate_distance_of_person_from_inputed_location(merge_tables, person_name, user_location_coordinates):
    """
        checks whether users search returned any results
        if results are returned, calculates distance of user from each result.
    """
    person_filtered_list = []
    for row in merge_tables:
        person_filtered_list.append(row)
        
    if person_filtered_list==[] :
        print("No person with this name has been found")
    else:

        person_filtered_list_with_distance = []
        for item in person_filtered_list:
            distance = int(haversine(user_location_coordinates[0],user_location_coordinates[1], item[9], item[10]))
            x = list(item)
            x.append(distance)
            person_filtered_list_with_distance.append(x)
    return person_filtered_list_with_distance
 
       
def sort_business_by_distance_from_user(business_type_filtered_list_with_distance, business_cat_search):
        """
            sorts business by distance from user and only returns those within a 60km radius.
        """
        order_by_distance = (sorted(business_type_filtered_list_with_distance, key=lambda s:s[11]))
        
        business_to_return_to_user = []
        for item in order_by_distance:
            if item[11]<=60:
                business_to_return_to_user.append(item)
            else:
                pass
        
        if business_to_return_to_user==[] :
            print("There are no {} in a 60km radius of your location".format(business_cat_search))
        else:
            print(business_to_return_to_user)
        
      

        
         

##how to calc distance - from stack overflow:
        

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    
    return int(c * r)



    
search_by_person()
search_by_business_name()
search_by_business_cat()

#def retrieve_business_name():
#    """
#        input business name
#        output all bbusiness form db with business name.
#    """
#    business_name_search = input("Enter Name of Business ").title()
#    db = getdb()
#    c = db[0]    
#    query = "SELECT * FROM business WHERE business_name =? ",  (business_name_search,)
#    c.execute(query)
#    business_name_filtered_list = []
#    for row in db.fetchall():
#        business_name_filtered_list.append(row)
#    if business_name_filtered_list==[] :
#        print("business name not found")
#    else:
#        print(business_name_filtered_list)  
#retrieve_business_name()    
    
#search_by_business()
    

