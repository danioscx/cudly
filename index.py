#!./pye/bin/python3

from flask import Flask

import os


apps = Flask(__name__)
apps.secret_key = os.urandom(20)


from bin import views
apps.register_blueprint(views)

if __name__ == "__main__":
    apps.run(debug=True)
