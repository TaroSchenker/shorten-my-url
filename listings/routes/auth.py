from flask import Blueprint, request, render_template

auth_routes = Blueprint("Auth", __name__)

@auth_routes.get('/login')
def login():
    return "this could be a login page"
