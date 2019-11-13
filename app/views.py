from flask import Flask, render_template,  url_for, request
from app import app
from randomuser import RandomUser


@app.route('/')
def index():
    title = "Pseudo Tinder"
    subtitle = "Here you can find someone to have fun with "
    return render_template('index.html', title=title, subtitle=subtitle)

@app.route('/randomusers')
def randos():
    title = "Pseudo Tinder"
    user_list = RandomUser.generate_users(50)
    subtitle = "Accessing the Random User API"  
    return render_template('randomusers.html', title=title,  subtitle=subtitle, user_list=user_list)

