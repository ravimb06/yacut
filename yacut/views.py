from random import randrange, choice
from string import ascii_letters
import re

from flask import flash, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id():
    rand_string = ''.join(
        choice(ascii_letters) + str(randrange(9)) for i in range(3)
    )
    return rand_string


@app.route('/', methods=['GET', 'POST'])
def add_urlmap_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.short.data
        if not short:
            short = get_unique_short_id()
        if not re.match("""^[a-zA-Z0-9]+$""", short):
            flash('Введены недопустимые символы!')
            return render_template('index.html', form=form)
        if URLMap.query.filter_by(short=short).first():
            flash(f'Имя {short} уже занято!')
            return render_template('index.html', form=form)
        urlmap = URLMap(
            original=form.original.data,
            short=form.short.data,
        )
        db.session.add(urlmap)
        db.session.commit()
        full_link = url_for('add_urlmap_view', _external=True) + short
        return render_template('index.html', form=form, short=full_link)
    return render_template('index.html', form=form)
