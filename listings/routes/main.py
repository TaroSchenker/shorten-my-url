from flask import Blueprint, request, render_template
from ..database.db import db
from ..models.listing import Listing, Url_input


main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        listings = Listing.query.all()
        return render_template("index.html", listings=listings)
    else:


        url = request.form["title"]
        shorten_url = 'potato'
        new_url = Url_input(url=url, shorten_url=shorten_url)
        db.session.add(new_url)
        db.session.commit()
        urls = Url_input.query.all()
        return render_template("index.html", listings=urls)
        # body = request.form["body"]
        # email = request.form["email"]
        # new_listing = Listing(title=title, body=body, email=email)
        # db.session.add(new_listing)
        # db.session.commit()
        # listings = Listing.query.all()
        # return render_template("index.html", listings=listings)
