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
        url = request.form["url"]
        long_url = Url_input.query.filter_by(url=url).first()
        if long_url:
            webbrowser.open_new_tab(f"http://www.{long_url.url}")
            return render_template("index.html", listings=listings)
        else:
            shorten_url = shortuuid.ShortUUID().random(length=5)
            print(shorten_url)
            new_url = Url_input(url=url, shorten_url=  shorten_url )
            db.session.add(new_url)
            db.session.commit()


        # urls = Url_input.query.all()
        return render_template("url.html", listing=new_url)
        # body = request.form["body"]
        # email = request.form["email"]
        # new_listing = Listing(title=title, body=body, email=email)
        # db.session.add(new_listing)
        # db.session.commit()
        # listings = Listing.query.all()
        # return render_template("index.html", listings=listings)
@main_routes.route('/', defaults={'path': ''})
@main_routes.route('/<path:path>')
def catch_all(path):
    print(path)
    found_url =  Url_input.query.filter_by(shorten_url=path).first()
    if found_url:
        print('catchall',found_url)
        long_url = found_url.url
        print('longerurl',long_url)
        # return 'You want path: %s' % long_url
        webbrowser.open_new_tab(f"http://www.{long_url}")
        return render_template("index.html")
    else:
        return render_template("index.html")

