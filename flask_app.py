#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('home.html', current_page='home_page')

@app.route("/portfolio")
def portfolio_page():
    return render_template('portfolio.html', current_page='portfolio_page')

@app.route("/contact")
def contact_page():
    return render_template('contact.html', current_page='contact_page')

if __name__ == "__main__":
    app.run(debug=True)