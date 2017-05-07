from flask import render_template,request,Response
from app.forms import PkForm

from . import main

@main.route('/')
def index():
    pk_form = PkForm()
    return render_template('index.html',form=pk_form)
	
@main.route('/pk',methods=['GET', 'POST'])
def pk():
    pk_form = PkForm(request.form)
    if pk_form.validate_on_submit():
        pk1_name = request.form.get('pk1')
        pk2_name = request.form.get('pk2')
        return render_template('pk.html',pk1=pk1_name, pk2=pk2_name)
    return Response('invalid input')
	
	
