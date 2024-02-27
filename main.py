from flask import Flask
from api import routes
from config import Db

app = Flask(__name__)
Db.Base.metadata.create_all(Db.engine)
routes.init_api_routes(app)

if __name__ == '__main__':
    app.run(debug=True)