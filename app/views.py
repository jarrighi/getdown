from app import app#, db, models
from flask import render_template, redirect, url_for, request

@app.route("/hi")
def say_hi():
  return "Hello!\n"

@app.route("/")
def index():
  return render_template("index.html")