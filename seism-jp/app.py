from flask import Flask, render_template
from typing import Any


app = Flask(__name__)


@app.route("/")
def index() -> Any:
    # TODO ref database.
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
