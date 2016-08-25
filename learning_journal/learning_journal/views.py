from pyramid.response import Response
from pyramid.view import view_config
import os

HERE = os.path.dirname(__file__)


@view_config(route_name="home", renderer="templates/home.html")
def home_view(request):
    imported_text = open(os.path.join(HERE, 'templates/home.html')).read()
    return Response(imported_text)


@view_config(route_name="detail", renderer="templates/detail.html")
def detail_view(request):
    imported_text = open(os.path.join(HERE, 'templates/detail.html')).read()
    return Response(imported_text)


@view_config(route_name="create", renderer="templates/create.html")
def create_view(request):
    imported_text = open(os.path.join(HERE, 'templates/create.html')).read()
    return Response(imported_text)


@view_config(route_name="update", renderer="templates/edit.html")
def update_view(request):
    imported_text = open(os.path.join(HERE, 'templates/edit.html')).read()
    return Response(imported_text)


def includeme(config):
    config.add_view(home_view, route_name='home')
    config.add_view(detail_view, route_name="detail")
    config.add_view(create_view, route_name="create")
    config.add_view(update_view, route_name="update")
