from flask import render_template
from .. import app


@app.get("/")
def main():
    return render_template("main.html")