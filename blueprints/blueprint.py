from sanic.response import json,text
from sanic import Blueprint

bp = Blueprint('apiv1',url_prefix='/v1')

@bp.route('/bp')
async def bp_root(request):
    return json({'aipic': 'blueprint'})

@bp.route('/urlfor')
async def test(request):
    url = request.app.url_for('apiv1.post_handler', post_id=5)  # --> '/v1/post/5'
    return text(url)

@bp.route('/post/<post_id>')
async def post_handler(request, post_id):
    return text('Post {} in Blueprint V1'.format(post_id))