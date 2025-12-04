from flask import Flask
from flask_cors import CORS
from backend.API.auth import customer_api
from backend.API.book import book_api
from backend.API.cinema import cinema_api
from backend.API.combo import combo_api
from backend.API.hall import hall_api
from backend.API.movie import movie_api
from backend.API.payment import payment_api
from backend.API.showtime import showtime_api
from backend.API.order import order_api
from backend.API.ticket import ticket_api

app = Flask(__name__)

# register tất cả API
app.register_blueprint(customer_api, url_prefix="/api")
app.register_blueprint(hall_api, url_prefix="/api")
app.register_blueprint(book_api, url_prefix="/api")
app.register_blueprint(cinema_api, url_prefix="/api")
app.register_blueprint(movie_api, url_prefix="/api")
app.register_blueprint(showtime_api, url_prefix="/api")
app.register_blueprint(combo_api, url_prefix="/api")
app.register_blueprint(order_api, url_prefix="/api")
app.register_blueprint(ticket_api, url_prefix="/api")
app.register_blueprint(payment_api, url_prefix="/api")
CORS(
    app,
    resources={r"/api/*": {"origins": "*"}},
    supports_credentials=True,
)
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
