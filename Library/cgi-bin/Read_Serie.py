#!/usr/bin/env python3
'''
This program displays all the value from the databse according to their ID.
'''
#import cgi in order to manipulate the html elements 
import cgi

#import Create_Database functions
from Create_Database import *

def main():
    '''
    This function creates an HTML and display all the values from the database by calling the function read_data() from Create_Database.
    The program stores the value into the variable data_list. If the returned value is True, it means there has been a problem with the database.
    Else the program will use a loop to display all data in a paragraph. 
    '''
    link = "../Index.html"
    link_book = "Read_Serie.py"
    link_add = "../AddOrUpdate.html"
    link_delete = "../Delete.html"
    
    print("Content-Type : text/html")
    print()
    print("<!doctype html>")
    print("<html>")
    print("<head>")
    print("<title>List Series</title>")
    print("<style>")
    print(" *{padding:0;margin:0;}")
    print("body{background-color:black;color:white;font-family: Arial, Helvetica, sans-serif;}")
    print("header{width: 100%;border-bottom: 16px solid #CFB53B;}")
    print("h1{color:white; padding:10px;font-weight:normal;}")
    print("#background_title{background-color: black;color: white;text-align: center;height: 120px;}")
    print("header h1{padding-top:40px;}")
    print("nav{text-align: left;padding-bottom: 10px;height: 25px;padding-top: 10px;margin-top:20px;}")
    print("nav li{display: inline;width: 100%;padding:15px;font-size: 20px;}")
    print("nav li a{color:white;text-decoration: none; background-color:grey; border-radius: 8px;padding:15px;}")
    print("nav li a:hover{color:rgb(52, 52, 70);text-shadow: 1px 1px rgb(100, 100, 100);}")
    print(".book_list{padding:20px;}")
    print("</style>")
    print("</head>")
    print("<header>")
    print("<div id='background_title'><h1>Create your list of favorite series</h1></div>")
    print("</header>")
    print("<div class='book_list'><h1>List Series</h1>")
    data_list = read_data()
    if data_list == True:
        print("<p>Database not found!</p>")
    else:
        for list_value in data_list:
            if "&" in list_value:
                list_value = list_value.replace("&", "&amp;")
            if "<" in list_value:
                list_value = list_value.replace("<", "&lt;")
            if "<" in list_value:
                list_value = list_value.replace(">", "&gt;")
            print("<p>{}</p>".format(list_value))
    print("<nav><ul><li><a href={}>Index</a></li>".format(link))
    print("<li><a href={}>Add/Update a Series</a></li>".format(link_add))
    print("<li><a href={}>Series list</a></li>".format(link_book))
    print("<li><a href={}>Delete Series</a></li>".format(link_delete))
    print("</nav>")
    print("</div></body></html>")
    
        
#Call the main function
if __name__ == '__main__': main()
