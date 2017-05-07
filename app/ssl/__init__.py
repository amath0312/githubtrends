from flask import Blueprint

ssl = Blueprint('ssl',__name__,url_prefix='/.well-known/pki-validation/')

from . import fileauth