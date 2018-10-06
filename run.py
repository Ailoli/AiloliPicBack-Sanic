import json
import jwtrun
from sanic import Sanic
from encode import MyEncode
from sanic.response import text
from blueprints.blueprint import bp


app = Sanic(__name__)
app.blueprint(bp,url_prefix = '/v1')

@app.route("/")
async def test(request):
    return text('Hello world!')

@app.middleware('request')
async def print_on_request(request):
    print(request)
    print("I print when a request is received by the server")

@app.route("/apiv1/getUser",methods=["POST"])
async def getToken(request):

    status,jsonstr = jwtrun.create_token(request)
    mEncode = MyEncode.MyEncoder()
    if  status:
        return text(
            json.dumps({
            "status_code":"200",
            "msg":"操作成功！",
            "JWT":jsonstr
        })
        )
    return text(jwtrun.create_token(request))
    # return jwtrun.create_token(request)

app.run(host="0.0.0.0", port=5000, debug=True)


