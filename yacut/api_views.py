from flask import jsonify  

from . import app
from .models import URLMap


# Явно разрешить метод GET
@app.route('/api/id/<int:id>/', methods=['GET'])  
def get_urlmap(id):
    # Получить объект по id или выбросить ошибку
    urlmap = URLMap.query.get_or_404(id)
    # Конвертировать данные в JSON и вернуть объект и код ответа API
    return jsonify({'urlmap': urlmap}), 200 