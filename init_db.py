from listings import db
from listings.models.listing import Listing

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()