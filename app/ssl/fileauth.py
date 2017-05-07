from flask import request, Response
from flask.views import MethodView

from . import *
import json

class FileauthAPI(MethodView):
    def get(self, item_id):
        item_id = request.args.get('item_id', None)
        
        return Response('{}',
                        status=200, mimetype='application/json')


fileauth_view = FileauthAPI.as_view('fileauth_api')
api.add_url_rule(
    '/fileauth.txt', view_func=item_view, methods=['GET', ])
