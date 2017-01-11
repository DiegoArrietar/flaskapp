from flask import render_template
from app.views.login import login, about
from app import app

app.add_url_rule('/login', view_func=login)
app.add_url_rule('/about', view_func=about)

