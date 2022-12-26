from datetime import datetime

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            short_link='http://localhost/' + self.short,
            url=self.original
        )

    def from_dict(self, data):
        columns_dict = {'original': 'url', 'short': 'custom_id'}
        for field in columns_dict.items():
            if field[1] in data:
                setattr(self, field[0], data[field[1]])
