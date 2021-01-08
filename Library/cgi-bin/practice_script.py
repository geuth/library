'''
This program tests all methods for the database: creation, adding a row, deleting a row, updating a row and reading a row.
'''

#import Create_Database functions
from Create_Database import *

def test():
    '''
    This function tests all functions and displays it in the shell.
    '''
    #calls the function create_db() from Create_Database
    create_db()

    #call the function read_data() to read the element of the database
    data_list = read_data()
    if data_list == True:
        print("Database doesn't exist")
    else:
        for value in data_list:
            print("{}".format(value))

    #create another tuple and add it to the database by calling add_row() with the tuple as a parameter
    tuple_list = ("SpongeBob SquarePants","Stephen Hillenburg", 1999, 12, 265, "ongoing","musical")
    add_row(tuple_list)

    #read the data in the database by calling the read_data() function
    print("Read data")
    data_list = read_data()
    if data_list == True:
        print("Database doesn't exist")
    else:
        for value in data_list:
            print("{}".format(value))

    #create another tuple and add it to the database by calling add_row() with the tuple as a parameter
    tuple_list2 = ("Lucifer","Shirpley", 2005, 5, 75, "ongoing","mystery")
    add_row(tuple_list2)

    #print data after adding a second row
    print("Data after adding second row")
    for value in read_data():
        print("{}".format(value))

    #update second row by passing the id we want to update and the tuple that contains the new information
    tup_list = ("Pokemon", "Junichi Masuda", 1997, 23, 1131,"ongoing", "adventure",2)
    update(2, tup_list)

    #print data to see if the data was modified
    data_list = read_data()
    if data_list == True:
        print("Database doesn't exist")
    else:
        for value in data_list:
            print("{}".format(value))
    #create a tuple with the number which will represent the id of the row we want to delete

    #call the function by passing the data and print data deleted
    delete(1)
    print("data deleted")

    #read the data from the database
    data_list = read_data()
    if data_list == True:
        print("Database doesn't exist")
    else:
        for value in data_list:
            print("{}".format(value))
test()
