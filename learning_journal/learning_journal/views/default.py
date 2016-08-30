from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from sqlalchemy.exc import DBAPIError

from ..models import MyEntry


@view_config(route_name="home", renderer="../templates/home.jinja2")
def home_view(request):
    try:
        query = request.dbsession.query(MyEntry)
        entries = query.all()
    except DBAPIError:
        return Response(db_err_msg, content_type="text/plain", status=500)
    return {"entries": entries}


@view_config(route_name='detail', renderer='../templates/detail.jinja2')
def detail_view(request):
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(MyEntry).get(entry_id)
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
    return {"entry": entry}


@view_config(route_name='create', renderer='../templates/create.jinja2')
def create_view(request):
    if request.method == "POST":
        new_title = request.POST["title"]
        new_body = request.POST["body"]
        new_creation_date = request.POST["creation_date"]
        new_entry = MyEntry(title=new_title, body=new_body, creation_date=new_creation_date)
        request.dbsession.add(new_entry)
        return {"entry": {"title": new_entry.title}}
    return{"entry": {"title": "this worked"}}



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
