Installation
    Step 1:
        To create a virtual environment and name it:
            1. pip3.10 install virtualenv 
            2. virtualenv {input name you want of virtual environment} --python= python{python version}
            3. in the terminal input ./{name of virtual environment}/Scripts/activate.ps1
    
    Step 2: 
        After activating virtualenv:
            install Flask Restful you would use pip install Flask-RESTful
            authenticating you should install Flask-JWT. so imput pip install Flask-JWT
    
    Step 3:
        Go into view --> Command Palette --> then python select interpreter --> find --> go to venv/Scripts/pyton.exe

Imports
    then from flask import Flask, app, request 
    then from flask_restful import Resource, Api, reqparse
    from flask_jwt import JWT, jwt_required 

Status Code     Status code Error 404 Means not found. 
    Status Code Error 200 means ok this is the most popular
    Status Code 400 means Bad Request 
    Creating has its own http status code which is 201
    Use the popular status codes when using the request

Error Prevention
       debug = True will allow you to get better error messages if your app has a bug. This is used when you running the app and you want better error messages
       Line 97


Steps
    app = Flask(__name__) <--- this is always needed
    api = Api(app) <-- this is needed to run the Api class


    When postman makes a request to our Api it will be from the request variable imported from flask

    when not using a database you can go ahead and create a list

    The post method has to have the same paramaters as the get method because when we access item/item name it will be the same name in the 
    paramater

    We return info in json format which is a object or a dictionary see line 56 and 62

    In lines 68 - 70 we are creating an item variable = that has a dictionary contatining name and price. Because this is a post method it
    is saving or posting the item in the database. In this case the database is the items array/list. So after creating an item dictionary
    we append it to the items list and then we return the list and use status code 201 because we added to the database. 

    When using list comprehension make sure to use an iterable item such as dictionaries and list. Tupples are not iterable and your code will not work in a list 
    comprehension 

    Lines 89 - 91 allow you to create an ItemList class with a resource paramater. Then we create a get method that will return all the items when you call it. 
    After creating this class the only way for it to run is that you have to add it to the api. To add things to the api we would use:
        
        api.add_resource(classname (ex: ItemList), endpoint (ex: '/items')) --> See line 95 for reference

        Then you add the extension so you can access the class. 

    JWT stands for JSON Web Token and it is a code use for authentication. It is away of encoding data that's a web token. Ex: if i want to send a private message I can
    encode it and no one will be able to view it unless they have a special encyption key to decode it.  

    line 8 app.secretkey is used to assign a secret key to your app

    # Quick mention valid JSON needs to be in double quotes not single quotes. In order for something to pass as valid JSON you have to use double quotes. Ex: "price" vs 
    'price'. "price" is valid JSON. 'price' is not and won't work

    create a jwt variable and allow the token to be used with your security.py file and your app.py. see lines 3 and 11 in app.py
    the jwt variable allows you to create an /auth endpoint in the url. when we call the auth endpoint we send it a user name and a password. The user class in 
    the user.py class needs an id, username and password paramater see user.py lines 1 - 5. We use the User class in the security.py file.     
    
    jwt_required allows you to require a jwt token for certain request such as the get request. Please see line 3 and 47. 

    using the jwt_required enpoint means that we need a jwt token to access a specific item from the server. Simply put if we want to use the get request to request a 
    single item then we need a token. We can post items, we can use the get request to see the items list, but for us to receive the data on a specific item we need a 
    jwt token. 
    
    Please see postman and get requst for the item. in order for us to access the data of a specific item we have to input the token for that item in the headers of the 
    get /item/<name> then we will have access to that data. to access the data in the get item endpoint you have to go into headers input Authorization then under value 
    input JWT (jwt token). just cut and paste the token after inputting JWT. To a server that what's logged in means. Can you prove that you are who you say you are. 
    You can do that with the jwt token

    for the delete function that is inside the item resource it will need a name function. In line 70 when creating the items variable to use the filter function you have
    to give it a function to pass and the iterable item for example filter(lambda x: x['name'] != name, items). the lambda function is the function, the items list is the 
    iterable. please see line 70. inorder to use the items variable and use the items iterable you have to tell python that the items variable being used in the items 
    variable is the items list. You tell python this by using the global function to tell python you are refering to the items iterable which is a global variable. 
    Please see line 69. then you tell the delete function to return a message in JSON format saying the item has been deleted. When you use postman after it deletes the 
    item it returns the message back in JSON format please see line 76 - 79.

    in line 65 -79
    For the put request here is what's happening. The first thing we are doing is requesting json data by creating a data variable. Next thing we are doing is creating 
    an item variable that filters the name in items list and looks for items that equal the name that was inputed in the endpoint. then we are saying if the items list 
    does not have an item that has the same name as the name in the endpoint then we create an item where the 'name' = the name in the put endpoint and the price equal 
    to the price we inputed in postman. we then append that item to the item list. If the item is already in there the put request will update the item's price in the 
    items list and return the new price and name of the item. 

    update: we add a parser function to the put method. The parser function allows you to add filtering to your JSON request that you are asking from the user.
    the parser function uses the reqparse method which was imported in line 2. this method allows you to create paramaters for user JSON request. In line 67
    in the parser we add an argument which allows you to create paramaters for what you are giving the user the ability to do. They can add a price, the
    type of the price paramater is a float, it is required, and to help the user not forget to add it you create a prompt saying this field cannot be left blank. 

    update: we moved the parser argument to the top of the class so we can have it for general use in case we need to call it in different methods. We moved the parser 
    method from line 42 - 46 so we can use it in any method/function in the class. This avoids haven't to duplicate the parser method in each instance of a method. For 
    example if we move the parser method to the top of the class we can call that method as a class method and refer to the parser method by stating Item.parser.parse_args().
    We pick up the parser method from the item class rather than adding self to the parser method. 

Using Postman:

    When you use postman to check the post request for the /auth endpoint. This means posting/saving the authorization username and password to the database. The system
    is suppose to return a jwt token which allows you to have access to the data as if you were to input your username and password. For example if your username: bob
    and your password was asdf and it matched the username in the /auth endpoint and authentication method in the securities.py then the system would return a token to
    you. That token can be used to access data that needs an encryption key to access to the server which was the username and password. check postman and auth endpoint
    when using the auth enpoint in postman you have to also input the correct username and password in json format under the headers in order to receive a token. 
