from flask import Flask
from flask_bcrypt import Bcrypt

import os

app = Flask(__name__)
bcrypt = Bcrypt(app)
allow_file = set(['txt', 'jpg', 'png', 'jpeg', 'gif'])
path_folder = os.getcwd() + "/assets/media/user_upload"