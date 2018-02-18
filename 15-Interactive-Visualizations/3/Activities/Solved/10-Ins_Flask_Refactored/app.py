# import necessary libraries
import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)

from models import Pet

# @app.before_first_request
# def setup():
#     # Recreate database each time for demo
#     # db.drop_all()
#     db.create_all()


from views import *

if __name__ == "__main__":
    app.run()
