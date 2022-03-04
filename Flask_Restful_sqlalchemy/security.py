from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username) # find a user by username the .get method is another way of accessing a dictionary 
    # the added benefit of using .get method in comparison with [] is that you can set a default value such as None. Also the square 
    # bracket would be username_mapping["username"].   
    if user and user.password == password:
        return user 

def identity(payload):  # payload is the content of the JWT token 
    user_id = payload['identity'] # takes the userid from the payload 
    return UserModel.find_by_id(user_id) # this extracts the specific user from this payload. We can retrieve user id by these 
    # functions without requiring some iteration. 
