from flask import Flask

from backend.API.auth import auth_api
from backend.API.cinema import cinema_api
from backend.API.movie import movie_api
from backend.API.showtime import showtime_api
from backend.API.combo import combo_api
from backend.API.order import order_api
from backend.API.ticket import ticket_api

app = Flask(__name__)

# register tất cả API
app.register_blueprint(auth_api, url_prefix="/api")
app.register_blueprint(cinema_api, url_prefix="/api")
app.register_blueprint(movie_api, url_prefix="/api")
app.register_blueprint(showtime_api, url_prefix="/api")
app.register_blueprint(combo_api, url_prefix="/api")
app.register_blueprint(order_api, url_prefix="/api")
app.register_blueprint(ticket_api, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
