from flask import Flask, session, render_template, redirect
import sqlite3

app = Flask(__name__)

def home_page():
    return render_template("home_page.html")

if __name__ = "__main__":
    app.debug = True
    app.run()