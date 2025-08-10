from flask import Flask
from flask import render_template

app = Flask(__name__)

projects = [
    {
        "name": "Portfolio app with Flask",
        "thumb": "img/portfolio.jpg",
        "hero": "img/portfolio.jpg",
        "categories": ["python", "web", "flask"],
        "slug": "portfolio",
        "prod": "https://google.com"
    },
    {
        "name": "Portfolio app with Python Flask",
        "thumb": "img/portfolio.jpg",
        "hero": "img/portfolio.jpg",
        "categories": ["python", "web", "flask"],
        "slug": "portfolio",
        "prod": "https://google.com"
    },
    {
        "name": "Portfolio app with Python Flask",
        "thumb": "img/portfolio.jpg",
        "hero": "img/portfolio.jpg",
        "categories": ["python", "web", "flask"],
        "slug": "portfolio",
        "prod": "https://google.com"
    }
]


@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

