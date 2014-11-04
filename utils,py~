from flask import Flask, flash, render_template, request, redirect, url_for, session, escape
from pymongo import MongoClient
import re

client = MongoClient('localhost', 27017)
db = client.proj
users = db.users

def add_user(username,password,name,email):
    

def emailconfirmation(email):
    if re.match("[a-z]+@[a-z]+\.[a-z]+",email):
        return True
    else:
        return False
















def create_user(username, password, name):
        '''Adds user to the database, returns their mongo _id'''
        user = {
                'username' : username,
                'password' : password,
                'name' : name
        }
	return users.insert(user)

def find_user(username):
        user = users.find_one({'username': username})
        return user

# update_dict must be in the form {field_to_update : new_val}
def update_user(username, update_dict):
        db.users.update({'username' : username}, {'$set' : update_dict}, upsert=False)
        return True
        # End MongoDB

def authenticate(username, password):
    user = find_user(username)
    # No such user
    if user == None:
        return False
    # Username/Password combo don't match
    elif str(user['username']) != username or str(user['password']) != password:
        return False
    # We good
    else:
        return True
