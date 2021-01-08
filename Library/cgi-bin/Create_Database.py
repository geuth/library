import sqlite3
'''
This program creates a database, adds elementa to the database, reads the data, updates and deletes element from the database.
'''

#create a databases
db_name = 'series_db'

def create_db():
    '''
    This function connects to the database and then creates a new table if this one doesn't exist.
    The variable connection contains the connection to the database, the cursor contains the bounding between the connection and the cursor() and creates the table in the database. 
    The table contains column for: id (int), Title (text), Author (text), Year (int), Season (int), Episode (int), Status (int), Status (text), Genre (text).
    Once the table is created the modification are being commited in the database and the connection is closed.
    '''
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Series(id INTEGER PRIMARY KEY,Title TEXT, Author TEXT,Year INT, Season INT, Episode INT,Status TEXT, Genre TEXT)''')
    connection.commit()
    connection.close()

def add_row(tup_list):
    '''
    This function adds data to the database.
    The variable connection contains the connection to the database, the cursor contains the bounding between the connection and the cursor() and inserts data into the database. 
    The query inserts the values contained in the tuple tup_list that's received and stores them in the following order: Title, Author,Year, Season, Episode, Status, Genre.
    As the tuple should contains the elements in that order.
    Once the table is created the modification are being commited in the database and the connection is closed.
    If the connection to the database or the table doesn't exist, a message will be displayed about not finding the list.
    '''
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        
        cursor.execute('''INSERT INTO Series (Title, Author,Year, Season, Episode, Status, Genre) VALUES(?,?,?,?,?,?,?)''', tup_list)
        connection.commit()
        connection.close()
        
        return "Information saved"
    except:
        return "Problem encountered during saving! Please restart the saving!"
    
def read_data():
    '''
    This function reads the database elements.
    The variable connection contains the connection to the database, the cursor contains the bounding between the connection and the cursor() and gets all data from the database. 
    The variable serie will contains all value received by the cursor by using fetchall() and return it to the cgi script or program that calls it and then the connection will be closed.
    If the table doesn't exist, we return true and the displayed message in the HTML file will be different.
    If the connection to the database or the table doesn't exist, a message will be displayed about not finding the list.
    '''
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM Series ORDER BY id ASC")
        serie = cursor.fetchall()
        
        return serie

        connection.close()
    except:
        return True
        

def update(id, tup_list):
    '''
    This function updates a row of the database.The variable connection contains the connection to the database. A tuple with the variable name val is created with just the id.
    The cursor searches for this id in the table and stores the result in the variable serie_info. The variable serie_line will store this row.
    If the id doesn't exist, a message that the id to update was not found will be dispayed.
    Else the program creates a tuple with the parameter received and the program modifies the info of the row that has the desired id. Once it's done, the changes
    are being committed and the connection is closed. A message of updated series will be returned.
    If the connection to the database or the table doesn't exist, a message will be displayed about not finding the list.
    '''
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        
        val = (id,)
        serie_info = cursor.execute("SELECT * FROM Series WHERE id = ?", val)
        serie_line = cursor.fetchone()
        
        if serie_line == None:
            return ("Couldn't find series! Please check the list and try again!\n")
        
        else:
            cursor.execute('''UPDATE Series SET Title = ?, Author = ? ,Year = ?, Season = ?, Episode = ?,Status =?, Genre = ? WHERE id = ?''', tup_list)
            connection.commit()
            connection.close()
            return ("Serie  updated!")
        
    except:
        return ("List not found!")
   

def delete(id):
    '''
    This function deletes a row of the database.The variable connection contains the connection to the database. A tuple with the variable id that's received as a parameter
    is stored in the variable value_id. The cursor selects the row with the id stored in the tuple and then deletes it.
    Once it's done, the changes are being committed and the connection is closed.
    '''
    
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    
    value_id = (id,)
    
    cursor.execute("DELETE FROM Series WHERE id = ?", value_id)
    connection.commit()
    connection.close()
        
    
