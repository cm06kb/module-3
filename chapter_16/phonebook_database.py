import sqlite3
import json
import requests
from math import radians, cos, sin, asin, sqrt


person_data_list = json.loads(open('./person_data.json').read())
business_data_list = json.loads(open('./business.json').read())
conn = sqlite3.connect('phonebook_project.db')
c = conn.cursor()

create_table("person", ["first_name TEXT", "last_name TEXT", "address_line_1 TEXT", "address_line_2 TEXT", "address_line_3 TEXT", "postcode TEXT", "country TEXT", "telephone_number TEXT"])
create_table("business", ["business_name TEXT", "address_line_1 TEXT", "address_line_2 TEXT", "address_line_3 TEXT", "postcode TEXT", "country TEXT", "telephone_number TEXT", "business_category TEXT"])
create_table("coordinates", ["postcode TEXT", "longitude INT", "latitude INT"])


def create_table(table_name, column_name):
  """
  creates a table within phonebook database.
  """
  column_names = ", ".join(column_name)
 
  query_string = "CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, column_names)
     
  c.execute(query_string)
 
  conn.commit()
 
create_table("person", ["first_name TEXT", "last_name TEXT", "address_line_1 TEXT", "address_line_2 TEXT", "address_line_3 TEXT", "postcode TEXT", "country TEXT", "telephone_number TEXT"])
create_table("business", ["business_name TEXT", "address_line_1 TEXT", "address_line_2 TEXT", "address_line_3 TEXT", "postcode TEXT", "country TEXT", "telephone_number TEXT", "business_category TEXT"])
create_table("coordinates", ["postcode TEXT", "longitude INT", "latitude INT"])



def add_data_to_table(table_name, data_for_table, column_name):
    """
    adds data to tables.
    """
    question_mark = []
    for n in range(len(column_name)):
        question_mark.append("?")
    question_mark = ", ".join(question_mark)
    column_names = ", ".join(column_name)
    
    for item in data_for_table:
        column_name_list = []
        for thing in column_name:
            thing = item[thing]
            column_name_list.append(thing)
        add_data = 'INSERT INTO {} ({}) VALUES({})'.format(table_name, column_names, question_mark)
        c.execute(add_data, column_name_list)
        conn.commit()


#add_data_to_table("person", person_data_list, ["first_name", "last_name", "address_line_1", "address_line_2", "address_line_3", "postcode", "country", "telephone_number"])
#add_data_to_table("business", business_data_list, ["business_name", "address_line_1", "address_line_2", "address_line_3", "postcode", "country", "telephone_number", "business_category"])



def dynamic_coordinates_data_entry():
     """
         adds unique postcodes from person and business table into coordinates table.
         
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
        else:
            pass
        
     add_data_to_table("coordinates", coor_dict, ["postcode", "longitude", "latitude"])



def retrieve_business_cat(user_location_coordinates):
    """
        Joins business and coordinate table based on user input.
        
    """

    business_cat_search = input("Enter Type of Business ").title()    
    print(type(c))

    c.execute("SELECT  * FROM business INNER JOIN coordinates ON (business.postcode = coordinates.postcode) WHERE business_category =?",  (business_cat_search,))
    
    merge_tables = c.fetchall()
    calculate_distance_of_business_from_user(merge_tables, user_location_coordinates, business_cat_search)    
    
def calculate_distance_of_business_from_user(merge_tables, user_location_coordinates, business_cat_search):
    """
        checks whether users search returned any results
        if results are returned, calculates distance of user from each result.
    """
    business_type_filtered_list = []
    for row in merge_tables:
        business_type_filtered_list.append(row)
        
    if business_type_filtered_list==[] :
        print("business type not found")
    else:

        business_type_filtered_list_with_distance = []
        for item in business_type_filtered_list:
            distance = int(haversine(user_location_coordinates[0],user_location_coordinates[1], item[9], item[10]))
            x = list(item)
            x.append(distance)
            business_type_filtered_list_with_distance.append(x)
        sort_business_by_distance_from_user(business_type_filtered_list_with_distance, business_cat_search)
 
       
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
    return c * r


def search_by_location():
    """
       takes users location and fetches the location coordinates from postcodes.io 
    """
    user_location = input("Enter city/town or postcode").title()
    endpoint = "https://api.opencagedata.com/geocode/v1/json?q={}&key=9f1c77b5b7df45a490c16449641a9b6f".format(user_location)
    payload = {"q": "{}".format(user_location), "countrycode":"gb", "appid": "9f1c77b5b7df45a490c16449641a9b6f"}
    response = requests.get(endpoint, params=payload)
    print(response.url)
    user_location = response.json()
    x1 = user_location['results'][0]['geometry']['lng']
    y1 = user_location['results'][0]['geometry']['lat']
    user_location_coordinates = (x1,y1)
    retrieve_business_cat(user_location_coordinates)    
    
    

#def retrieve_business_name():
#    business_name_search = input("Enter Name of Business ").title()
#    c.execute('SELECT * FROM business WHERE business_name =? ' ,  (business_name_search,))
#    business_name_filtered_list = []
#    for row in c.fetchall():
#        business_name_filtered_list.append(row)
#    if business_name_filtered_list==[] :
#        print("business name not found")
#    else:
#        print(business_name_filtered_list)  
#retrieve_business_name()    
    
user_location_coordinates = search_by_location()
    

