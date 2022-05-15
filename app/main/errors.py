from flask import render_template

from . import main


@main.errohandler(404)
def f4f(error):
    return render_template('404.html'), 404