from flask import request, Response
from flask.views import MethodView

from . import *
import json
import urllib.request

class GithubAPI(MethodView):
    def get(self):
        page = request.args.get('page', '1')
        per_page = request.args.get('per_page', '10')

        #url = 'https://api.github.com/search/repositories?q=stars:">10"+pushed:>2017-05-05&sort=stars&order=desc&page=1&per_page=5'
        #url = 'https://api.github.com/search/repositories?q=stars:">10"+created:>2017-05-05&sort=stars&order=desc&page=1&per_page=5'
        url = 'https://api.github.com/search/repositories?q=stars:">10"&sort=stars&order=desc&page=%s&per_page=%s' % (page,per_page)
        response = urllib.request.urlopen(url).read().decode('utf-8')
        data = json.loads(response)
        print(data['total_count'])
        resp_data = {}
        total = int( data['total_count'])
        total = total if total < 1000 else 1000
        resp_data['total'] = str(total)
        resp_data['total_page'] = self.total_page(int(per_page), total)
        resp_data['last_page'] = True if page == resp_data['total_page'] else False
        resp_data['repositories']=[]

        for repo in data['items']:
            repo_data = {}
            repo_data['name'] = repo['full_name']
            repo_data['description'] = repo['description']
            repo_data['stars'] = str(repo['stargazers_count'])
            repo_data['avatar'] = repo['owner']['avatar_url']
            resp_data['repositories'].append(repo_data)

        return Response(json.dumps(resp_data),
                        status=200, mimetype='application/json')
    
    def total_page(self, per_page, total):
        return str((total//per_page) + (0 if total%per_page == 0 else 1))



github_view = GithubAPI.as_view('github_api')
api.add_url_rule(
    '/repositories/', view_func=github_view, methods=['GET', ])