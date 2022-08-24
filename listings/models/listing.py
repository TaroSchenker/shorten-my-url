from ..database.db import db

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(500))
    email = db.Column(db.String(500))

class Url_input(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(250))
    shorten_url = db.Column(db.String(200))

    def get_all():
        all_urls = Url_input.query.all()
        return all_urls

    def get_main_url(shorten_url):
        result = Url_input.query.filter_by(shorten_url=shorten_url).first()
        # print('this is the result in the model', result)
        if not result:
            print('i abort')
            # abort(404, message="Video not found")
        return result

        

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
