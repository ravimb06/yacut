from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import char_validator, get_unique_short_id


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_url(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': urlmap.to_dict()['original']}), 200


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    data = request.get_json()
    if 'short' not in data:
        data['short'] = get_unique_short_id()
    if not char_validator(data['short']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if 'original' not in data:
        raise InvalidAPIUsage('В запросе отсутствует оригинальная ссылка')
    if URLMap.query.filter_by(short=data['short']).first() is not None:
        raise InvalidAPIUsage('Такая короткая ссылка уже существует!')
    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify({'urlmap': urlmap.to_dict()}), 201
