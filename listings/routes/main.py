from flask import Blueprint, request, render_template, redirect, url_for
from ..database.db import db
from ..models.listing import Listing, Url_input
import webbrowser
import shortuuid

main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        my_params =  request.url
        print(my_params)
        listings = Listing.query.all()
        return render_template("index.html", listings=listings)
    else:
        print("hi ********************************")
        url = request.form["url"]
        long_url = Url_input.query.filter_by(url=url).first()
        if long_url:
            return redirect(f"http://{long_url}")
        else:
            shorten_url = shortuuid.ShortUUID().random(length=5)
            print(shorten_url)
            new_url = Url_input(url=url, shorten_url=  shorten_url )
            db.session.add(new_url)
            db.session.commit()
        return render_template("url.html", listing=new_url)

@main_routes.route('/', defaults={'path': ''})
@main_routes.route('/<path:path>')
def catch_all(path):
    print(path)
    found_url =  Url_input.query.filter_by(shorten_url=path).first()
    if found_url:
        print('catchall',found_url)
        long_url = found_url.url
        print('longerurl',long_url)
        return redirect(f"http://{long_url}")
        
    else:
        return render_template("index.html")

