#!/usr/bin/env python3
'''
This program gets the value entered in the library.html file in order to save or update a series. All values will be saved into a database.
'''
#import cgi in order to manipulate the html elements 
import cgi
#import Create_Database functions
from Create_Database import *

def main():
    '''
    This function will first call the create_db function from Create_Database and have a database and table created.
    This function then gets the data from the variable form that stores the field input from the HTML form and
    gets the value entered in the input in the variable id_series, title, author, year, season, episode, status, genre. They will all hold values that
    represent their content from the HTML file.Then, this program creates content for a HTML page.
    If any field was empty, a message telling the user that a field wasn't filled in is displayed
    If the field that contains the id is not empty, the program will update a row from the database and call the update() method from the Create_Database program.
    Else, the program creates a new row for the data as the program call the add_row() function from the Create_Database and a message will be returned and
    displayed in the HTML page.
    If there is an error of database during the saving or update process, a message will be displayed.
    '''
    create_db()

    form = cgi.FieldStorage()
    id_serie = form.getfirst('id_series')
    title = form.getfirst('title')
    author = form.getfirst('author')
    year = form.getfirst('year')
    season = form.getfirst('season')
    episode = form.getfirst('episodes')
    status = form.getfirst('status')
    genre = form.getfirst('genre')
    
    link = "../Index.html"
    link_book = "Read_Serie.py"
    link_add = "../AddOrUpdate.html"
    link_delete = "../Delete.html"
    
    print("Content-Type : text/html")
    print()
    print("<!doctype html>")
    print("<html>")
    print("<head>")
    print("<title>Save Series</title>")
    #css styling for the html content
    print("<style>")
    print(" *{padding:0;margin:0;}")
    print("body{background-color:black; font-family: Arial, Helvetica, sans-serif;}")
    print("header{width: 100%; border-bottom: 16px solid #CFB53B;}")
    print("h1{color:white; padding:10px; font-weight:normal;}")
    print("p{padding:10px; font-size:16px;}")
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
   
    
    if title == None or author == None or year == None or episode == None or not genre or status == None or season == None:
        print("<div class='error'><h1>Failed to save series!</h1>")
        print("<p>All fields must be populated!</p></div>")
        print("<div class='info_css'><h1>{}</h1>".format(title))
        print("<p>Author: {}</p>".format(author))
        print("<p>Year: {}</p>".format(year))
        print("<p>Season: {}</p>".format(season))
        print("<p>Number of episodes: {}</p>".format(episode))
        print("<p>Status: {}</p>".format(status))
        print("<p>Genre: {}</p></div>".format(genre))
        #create a navigation
        print("<nav><ul><li><a href={}>Index</a></li>".format(link))
        print("<li><a href={}>Add/Update a Series</a></li>".format(link_add))
        print("<li><a href={}>Series list</a></li>".format(link_book))
        print("<li><a href={}>Delete Series</a></li>".format(link_delete))
        print("</nav>")
        print("</body></html>")
        
    elif id_serie != None:
        try:
            year = int(year)
            season = int(season)
            episode = int(episode)
            id_serie = int(id_serie)
            
            tup_list = (title,author, year, season, episode, status, genre,id_serie)
            
            print("<div class='error'>")
            print("<h1>{}</h1>".format(update(id_serie,tup_list)))
            print("<div class='info_css'><p>Serie Id {}.</p>".format(id_serie))
            print("<nav><ul><li><a href={}>Index</a></li>".format(link))
            print("<li><a href={}>Add/Update a Series</a></li>".format(link_add))
            print("<li><a href={}>Series list</a></li>".format(link_book))
            print("<li><a href={}>Delete Series</a></li>".format(link_delete))
            print("</nav>")
            print("</body></html>")
            
        except:
            print("<div class='error'>")
            print("<h1>Serie not updated! <br/>Wrong format, please enter a digit-integer for the following elements: episode, season or year or id!</h1></div>")
            print("<div class='info_css'><h1>{}</h1>".format(id_serie))
            print("<p>Title: {}</p>".format(title))
            print("<p>Author: {}</p>".format(author))
            print("<p>Year: {}</p>".format(year))
            print("<p>Season: {}</p>".format(season))
            print("<p>Number of episodes: {}</p>".format(episode))
            print("<p>Status: {}</p>".format(status))
            print("<p>Genre: {}</p></div>".format(genre))
            print("<nav><ul><li><a href={}>Index</a></li>".format(link))
            print("<li><a href={}>Add/Update a Series</a></li>".format(link_add))
            print("<li><a href={}>Series list</a></li>".format(link_book))
            print("<li><a href={}>Delete Series</a></li>".format(link_delete))
            print("</nav>")
            print("</body></html>")
                
    else:
        try:
            year = int(year)
            season = int(season)
            episode = int(episode)
            
            serie_tup = (title,author, year, season, episode, status, genre)
            
        
            print("<div class='info_css'><h1>{}<br/>{}</h1>".format(add_row(serie_tup),title))
            print("<p>Author: {}</p>".format(author))
            print("<p>Year: {}</p>".format(year))
            print("<p>Season: {}</p>".format(season))
            print("<p>Number of episodes: {}</p>".format(episode))
            print("<p>Status: {}</p>".format(status))
            print("<p>Genre: {}</p></div>".format(genre))
            print("<nav><ul><li><a href={}>Index</a></li>".format(link))
            print("<li><a href={}>Add/Update a Series</a></li>".format(link_add))
            print("<li><a href={}>Series list</a></li>".format(link_book))
            print("<li><a href={}>Delete Series</a></li>".format(link_delete))
            print("</nav>")
            print("</body></html>")
         
        except:
            print("<div class='error'>")
            print("<h1>Failed to save series! <br/>Wrong format, episode, season or year must be whole numbers!</h1></div>")
            print("<div class='info_css'><h1>{}</h1>".format(title))
            print("<p>Author: {}</p>".format(author))
            print("<p>Year: {}</p>".format(year))
            print("<p>Season: {}</p>".format(season))
            print("<p>Number of episodes: {}</p>".format(episode))
            print("<p>Status: {}</p>".format(status))
            print("<p>Genre: {}</p></div>".format(genre))
            print("<nav><ul><li><a href={}>Index</a></li>".format(link))
            print("<li><a href={}>Add/Update a Series</a></li>".format(link_add))
            print("<li><a href={}>Series list</a></li>".format(link_book))
            print("<li><a href={}>Delete Series</a></li>".format(link_delete))
            print("</nav>")
            print("</body></html>")
        

#The main function is called
if __name__ == '__main__': main()

