from sanic.response import json
from sanic import Blueprint

bp = Blueprint('blueprint')

@bp.route('/bp')
async def bp_root(request):
    return json({'aipic': 'blueprint'})