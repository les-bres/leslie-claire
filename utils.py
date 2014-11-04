from flask import Flask, flash, render_template, request, redirect, url_for, session, escape
from pymongo import MongoClient
import re

client = MongoClient('localhost', 27017)
db = client.proj
users = db.users

def add_user(username,password,name,email):
    user = {
        'username' : username,
        'password' : password,
        'email' : email,
        'name' : name
    }
    return users.insert(user)
    
def emailconfirmation(email):
    if re.match("[a-z]+@[a-z]+\.[a-z]+",email):
        return True
    else:
        return False













