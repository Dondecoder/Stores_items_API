So in the previous readme we learned how to build a Flask-Restful API and test it. Rather than creating our in network database
we will use sqlite as our database and connect it to our app. 

Using sqlite3 database:
    Import:
        import sqlite3

    Next you have to connect the database so you can use it. Connect the 
    database to a file that you create using:
        connection = sqlite3.connect('data.db')


    Next you have to create a cursor variable. It is responsible for executing
    queries a saving to a database 
        cursor = connection.cursor()

    To create a table similar to the users table in the previous read me. 
    You have to create a query. For example:
        create_table = "CREATE TABLE users(id int, username text, password text)"
        P.S in the query that you create state the name of the table you are
        creating such as users and the paramaters it will have
    
    to add to the database use:
        cursor.execute(create_table)

    then you can create a user variable which is a tuple of info
    it will sate the id, username, and passord:
        user = (1, 'jose', 'asdf')

    in order to add to sqlite3 database you need to create a query. So:
        insert_query = "INSERT INTO users VALUES (?,?,?)

    next step save to the datatabase using:
        cursor.execute(insert_query, user)
        ^Sidebar..in the cursor.execute function we need to include the 
        sqlite3 string and the iterable data for example the user tuple

    to add multiple users we first need to create a table:
        users = [
            (2,'rolf','asdf')
            (3, 'anne','xyz)
        ]

    then to add it to the database we use the executemany function:
        cursor.executemany(insert_query, users)

    It's good common practice to use:
        connection.commit() to make sure the datatabase has everything saved
        connection.close() to make sure database will not receive any more data
        ^ sidebar ... if you are adding anything to the database please make 
        sure to delete the data.db file before running the program again
    
    
    Optional things you can add to check that your sqlite3 database has update 
    correctly. You can create a variable called:
        select_query ="SELECT * FROM users"
        ^ sidebar you do not need to use the asteriks you can use any paramater
        such as "SELECT id FROM users" or "SELECT username FROM users"
        then use a simple for loop such as:
        for row in cursor.execute(select_query):
        print (row)

To make things alot easier when using the post method you can use the parser method along with the sqlite3 database. Using the parser
method allows you to set paramaters for json request from the user. In the user.py file we created a UserRegister class that is a Resource.
We used the Resource paramater for the class. In order to do that we imported the Resource method from flask_restful. We then created a
post method in the UserRegister class. The post method in this class allows us to post a username and password to the database (which is
sqlite3). We then connected the post method to sqlite3 by creating a connection variable, cursor variable, and a query. We then imported 
reqparse from flask_restful so we can use the parser method. We used the parser method for username and password in the UserRegister class. 
then we used a classmethod for the post method in UserRegister class so we don't hard code the UserRegister class in the post method.
In the query we will retrieve the username and password from the data variable created by the parser method. After creating this class
we added it to the Api. we imported the UserRegister class from the user file and added the resource to the app.py by using 
api.add_resource(UserRegister, '/register'). This created the register endpoint for us to Register new users and post it to the database.

Understanding the concept of if __name__ == '__main__':
    This simply means that whenever you run a file, Python associates a name with the file you are running, which is called __main__. 
    if __name__ == '__main__' is important to add to your file because when you are importing that specific file, there are certain 
    element of that file that you do not want to run when importing to another file. For example in the app.py file we run the flask app
    by using app.run. If we were to import, the app.py file into another file without including the if __name__ == '__main__' it would 
    continue running the app.run portion of the app.py file (when files are imported the import function runs the file). To prevent 
    the app.run from running continously we can simply use if __name__ == '__main__'. This way the only time app.run will run is when we
    run the app.py file and app.run won't run if we import app.py to another file. Please see last line of app.py for reference.  