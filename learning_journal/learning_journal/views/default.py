from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPFound
from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.security import remember, forget
from learning_journal.security import check_credentials
import datetime
import os

from ..models import MyEntry


@view_config(
    route_name="home", renderer="../templates/home.jinja2")
def home_view(request):
    query = request.dbsession.query(MyEntry).order_by(MyEntry.creation_date.desc())
    entries = query.all()
    return {"entries": entries}


@view_config(
    route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(MyEntry).get(entry_id)
    if entry is None:
        raise HTTPNotFound
    return {"entry": entry}


@view_config(
    route_name='update', renderer='../templates/edit.jinja2', permission='private')
def edit_view(request):
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(MyEntry).get(entry_id)
    if entry is None:
        raise HTTPNotFound
    if request.method == "POST":
        entry.title = request.POST["title"]
        entry.body = request.POST["body"]
        entry = MyEntry(title=entry.title, body=entry.body, creation_date=entry.creation_date)
        return HTTPFound(location=request.route_url('home'))
    return {"entry": entry}


@view_config(
    route_name='create', renderer='../templates/create.jinja2', permission='private')
def create_view(request):
    title = body = error = ''
    if request.method == 'POST':
        title = request.params.get('title', '')
        body = request.params.get('body', '')
        if not body or not title:
            error = "title and body are both required"
    if request.method == "POST":
        new_title = request.POST["title"]
        new_body = request.POST["body"]
        new_creation_date = datetime.datetime.utcnow()
        new_entry = MyEntry(title=new_title, body=new_body, creation_date=new_creation_date)
        request.dbsession.add(new_entry)
        return HTTPFound(location=request.route_url('home'))  # credit Cris Ewing
    return {"title": title, "body": body, "error": error}


@view_config(route_name='login', renderer='../templates/login.jinja2', permission=NO_PERMISSION_REQUIRED)
def login_view(request):
    username = password = error = ""
    if request.method == "POST":
        username = request.params.get("username", "")
        password = request.params.get("password", "")
        if not username or not password:
            error = "You must enter a username and password"
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if check_credentials(username, password):
            headers = remember(request, username)
            return HTTPFound(location=request.route_url('home'), headers=headers)
        error = "You lack editing permissions, but can still view the page."
    return {"error": error}


@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(request.route_url('login'), headers=headers)
