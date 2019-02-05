def create_table(table_name, column_name):
  """
  input: table name and column names
  output: table.
  creates a table within phonebook database.
  """
  column_names = ", ".join(column_name)
  db = getdb()
  c = db[0]
  conn = db[1]
  query_string = "CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, column_names)
     
  c.execute(query_string)
 
  conn.commit()
 


def add_data_to_table(table_name, data_for_table, column_name):
    """
    input: data for table.
    output:data into table.
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