from app import db
from flask import request, Response
from flask.views import MethodView

from . import *
import json
import app.util


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        # convert object to a dict
        d = {}
        # d['__class__'] = obj.__class__.__name__
        # d['__module__'] = obj.__module__
        d['id'] = obj.id
        d['username'] = obj.username
        d['email'] = obj.email
        return d


class ItemAPI(MethodView):
    def get(self, item_id):
        item_id = request.args.get('item_id', None)
        if item_id is not None:
            admin = User(item_id, 'admin@example.com')
            db.session.add(admin)
            db.session.commit()
            resp = Response(UserEncoder().encode(admin),
                            status=200, mimetype='application/json')
            return resp
        return Response('{}',
                        status=200, mimetype='application/json')


item_view = ItemAPI.as_view('item_api')
api.add_url_rule(
    '/items/', defaults={'item_id': None}, view_func=item_view, methods=['GET', ])
api.add_url_rule(
    '/items/', defaults={'item_id': None}, view_func=item_view, methods=['GET', ])
