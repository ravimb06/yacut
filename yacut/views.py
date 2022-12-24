from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from .utils import char_validator, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def add_urlmap_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if not short:
            short = get_unique_short_id()
        if not char_validator(short):
            flash('Введены недопустимые символы!')
            return render_template('index.html', form=form)
        if URLMap.query.filter_by(short=short).first():
            flash(f'Имя {short} уже занято!')
            return render_template('index.html', form=form)
        urlmap = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(urlmap)
        db.session.commit()
        full_link = url_for('add_urlmap_view', _external=True) + short
        return render_template('index.html', form=form, short=full_link)
    return render_template('index.html', form=form)


@app.route('/<short_id>')
def redirect_to_original_link(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        abort(404)
    return redirect(urlmap.original)
