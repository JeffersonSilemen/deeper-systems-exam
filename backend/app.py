from flask import Flask
from flask_cors import CORS
from routes import routes
from parser import import_data

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes)

import_data("constants/udata.json")


if __name__ == "__main__":
    app.run(debug=False)