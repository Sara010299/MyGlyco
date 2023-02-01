# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:41:40 2022

@author: sarak
"""

from flask import Flask
app= Flask(__name__)


from flask_swagger_ui import get_swaggerui_blueprint

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger2.json'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

# python app.py

from app import views