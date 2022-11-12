from flask import request, render_template, flash, redirect, url_for
from app import app
from .forms import RegisterForm


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # get info on the app the was requested
            app_requested = request.form['button']
            print(app_requested)
            # redirect to the appropriate app
            return redirect(url_for(app_requested))
        except Exception as e:
            flash("Try again! An error occured")

    return render_template('index.html',
                           title='Simple template example')


@app.route('/form')
def form():
    user = {'name': 'Sam Wilson'}
    form = RegisterForm()
    return render_template('form.html',
                           title='Form page',
                           form=form)
