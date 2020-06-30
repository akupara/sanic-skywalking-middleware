from sanic import Sanic
from sanic.response import json

from sanic_skywalking_middleware import SanicSkywalingMiddleware

app = Sanic("Sanic")

agent = SanicSkywalingMiddleware(app, service='Sanic Skywalking Demo Service', collector='127.0.0.1:11800')


@app.route("/hello")
async def hello(request):
    return json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
