from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db

main = Blueprint('main', __name__)

@main.route('/')
def main_root():
    return render_template("main.html")

@main.route('/home')
def main_home():
    return render_template("main.html")
