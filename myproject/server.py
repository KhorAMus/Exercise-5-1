from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config



@view_config(route_name = "index", renderer = "index.jinja2")
@view_config(route_name = "index_synonim2", renderer = "index.jinja2")
def index(request):
    return {}

@view_config(route_name = "aboutme", renderer = "about/aboutme.jinja2")
def aboutme(request):
    return {}

if __name__ == '__main__':
    config = Configurator()
    config.add_route('index', '/')
    config.add_route('index_synonim2', '/index.html')
    config.add_route('aboutme', '/about/aboutme.html')
    config.include('pyramid_jinja2')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()






