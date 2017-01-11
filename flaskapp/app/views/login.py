from flask import render_template

from app import app


def login():
    return render_template('dashboard/login.html')


def about():
    return render_template('dashboard/about.html')
