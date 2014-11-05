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













