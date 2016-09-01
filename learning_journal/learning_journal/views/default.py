from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPFound
import datetime

from sqlalchemy.exc import DBAPIError

from ..models import MyEntry


@view_config(route_name="home", renderer="../templates/home.jinja2")
def home_view(request):
    query = request.dbsession.query(MyEntry).order_by(MyEntry.creation_date.desc())
    entries = query.all()
    return {"entries": entries}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(MyEntry).get(entry_id)
    if entry is None:
        raise HTTPNotFound
    return {"entry": entry}


@view_config(route_name='update', renderer='../templates/edit.jinja2')
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


@view_config(route_name='create', renderer='../templates/create.jinja2')
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
    return{"title": title, "body": body, "error": error}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_learning_journal_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
