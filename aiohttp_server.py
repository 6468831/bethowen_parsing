import re
from aiohttp import web
import aiohttp_cors

from logger import logger

async def hey_handle(request):
    text = "Hey"
    logger.debug(text)
    return web.json_response({'success': text})
    
async def name_handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    logger.debug(text)
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/hey', hey_handle),
                web.get('/{name}', name_handle)])

cors = aiohttp_cors.setup(app, defaults={
   "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*"
    )
  })


for route in list(app.router.routes()):
    cors.add(route)

# class Handler(web.View):
#     @aiohttp_jinja2.template('tmpl.jinja2')
#     async def get(self):
#         return {'name': 'Andrew', 'surname': 'Svetlov'}

def is_ajax(request):
    print('!!', request._protocol.__dir__())
    requested_html = re.search(r'^text/html', request.META.get('HTTP_ACCEPT'))
    return bool(requested_html)

if __name__ == '__main__':
    web.run_app(app)