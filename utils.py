import re

# one method that uses all other checking methods
def confirmation(username,password,email,name):  
    answer = "good"
    if username_confirmation(username) == False:
        answer = "invalid"
    if password_confirmation(password) == False:
        answer = "invalid"
    if email_confirmation(email) == False:
        answer = "invalid"
    if name_confirmation(name) == False:
        answer = "invalid"
    return answer

def username_confirmation(username):
    if re.match("((\w)|(\d)|[\.-_]){6,15}"):
        return "valid"
    else:
        return "Sorry, this is not a valid username. Please only use letters, periods, underscores, and hyphens in your username. Usernames must be between 6 and 15 characters."


def password_confirmation(password):
    if re.match("([a-z]|\d+){6,15}"):
        return "valid"
    else:
        return "Sorry, this is not a valid password. Please use only lowercase letters and numbers in your password. Passwords must be between 6 and 15 characters." 

def email_confirmation(email):
    if re.match("[a-z]+@[a-z]+\.[a-z]+",email):
        return "valid"
    else:
        return "Sorry, this is not a valid email. Please make sure you enter a real email."

def name_confirmation(name):
    if re.match("(\w|\s){6,15}"):
        return "valid"
    else:
        return "Sorry, this is not a valid username. Please use only letters and spaces in your username. Usernames must be between 6 and 15 characters."

import re

# one method that uses all other checking methods
def confirmation(username, password,email,name):    
    if email_confirmation(email) == False:
        return "invalid email"
    else:
        return "good"


def email_confirmation(email):
    if re.match("[a-z]+@[a-z]+\.[a-z]+",email):
        return True
    else:
        return False













