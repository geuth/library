#!/usr/bin/env python3
'''
This program get the value entered in the Delete.html file in order to delete the row that contains this id number.
'''
#import cgi in order to manipulate the html elements 
import cgi

#import Create_Database functions
from Create_Database import *

def main():
    '''
    The program creates an html page. 
    This function gets the data from the variable form that stores the field input from the HTML form and
    gets the value entered in the input with the value "id_delete" and the program stores it in the variable id_series.
    If the value received is null, the program will display that no value was entered.
    If the value is not a digit, a message that tells the user that the value wasn't a digit is being displayed on the html page.
    If the value is an integer, the form call the function delete() from Create_Database and then deletes the row with the entered id.
    '''
    form = cgi.FieldStorage()
    id_series = form.getfirst('id_delete')
    
    link = "../Index.html"
    link_book = "Read_Serie.py"
    link_add = "../AddOrUpdate.html"
    link_delete = "../Delete.html"
    
    print("Content-Type : text/html")
    print()
    print("<!doctype html>")
    print("<html>")
    print("<head>")
    print("<title>Delete Series</title>")
    #css styling for the html content
    print("<style>")
    print(" *{padding:0;margin:0;}")
    print("body{background-color:black; font-family: Arial, Helvetica, sans-serif;}")
    print("header{width: 100%; border-bottom: 16px solid #CFB53B;}")
    print("h1{color:white; padding:10px; font-weight:normal;}")
    print("#background_title{background-color: black;color: white;text-align: center;height: 120px;}")
    print("header h1{padding-top:40px;}")
    print("nav{text-align: left;padding-bottom: 10px;height: 25px;padding-top: 10px;}")
    print("nav li{display: inline;width: 100%;padding:15px;font-size: 20px;}")
    print("nav li a{color:white;text-decoration: none; background-color:grey; border-radius: 8px;padding:15px;}")
    print("nav li a:hover{color:rgb(52, 52, 70);")
    print("text-shadow: 1px 1px rgb(100, 100, 100);}")
    print(".error{color:white; padding:15px;}")
    print(".info_css{color:white; padding:15px;}")
    print(".info_css h1{font-size:40px; font-weight:normal;}")
    print("</style>")
    print("</head>")
    print("<header>")
    print("<div id='background_title'><h1>Create your list of favorite series</h1></div>")
    print("</header>")
    
    if id_series == None:
        print("<div class='error'><h1>No ID entered!</h1></div>")
        #create a navigation
        print("<nav><ul><li><a href={}>Index</a></li>".format(link))
        print("<li><a href={}>Add/Update a Series</a></li>".format(link_add))
        print("<li><a href={}>Series list</a></li>".format(link_book))
        print("<li><a href={}>Delete Series</a></li><".format(link_delete))
        print("</nav>")
        print("</body></html>")
                
    else:
        try:
            id_series = int(id_series)
            delete(id_series)
            print("<div class='info_css'><h1>Information with id {} deleted.</h1>".format(id_series))
            print("<nav><ul><li><a href={}>Index</a></li>".format(link))
            print("<li><a href={}>Add/Update a Series</a></li>".format(link_add))
            print("<li><a href={}>Series list</a></li>".format(link_book))
            print("<li><a href={}>Delete Series</a></li>".format(link_delete))
            print("</nav>")
            print("</body></html>")
         
        except:
            print("<div class='error'>")
            print("<h1>ID entered wasn't an integer! {}</h1></div>".format(id_series))
            print("<nav><ul><li><a href={}>Index</a></li>".format(link))
            print("<li><a href={}>Add/Update a Series</a></li>".format(link_add))
            print("<li><a href={}>Series list</a></li>".format(link_book))
            print("<li><a href={}>Delete Series</a></li><".format(link_delete))
            print("</nav>")
            print("</body></html>")
        

#we call the main function
if __name__ == '__main__': main()

