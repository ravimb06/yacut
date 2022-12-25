from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, Regexp


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Введите исходную ссылку',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Regexp('^[a-zA-Z0-9]+$', message='Недопустимые символы'),
            Length(1, 16),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
