import pytest
import transaction
import datetime

from pyramid import testing

from .models import (
    MyEntry,
    get_engine,
    get_session_factory,
    get_tm_session
)
from .models.meta import Base

DB_SETTINGS = {'sqlalchemy.url': 'sqlite:////tmp/testme.sqlite'}


@pytest.fixture(scope="session")
def sqlengine(request):
    """Set up sql engine."""
    config = testing.setUp(settings=DB_SETTINGS)
    config.include(".models")
    settings = config.get_settings()
    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    def teardown():
        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return engine


@pytest.fixture(scope="function")
def new_session(sqlengine, request):
    """Set up new new session."""
    session_factory = get_session_factory(sqlengine)
    session = get_tm_session(session_factory, transaction.manager)

    def teardown():
        transaction.abort()

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope="function")
def populated_db(request, sqlengine):
    session_factory = get_session_factory(sqlengine)
    session = get_tm_session(session_factory, transaction.manager)

    with transaction.manager:
        session.add(MyEntry(title="Vic Week 2 Day 5", body="This is a test entry, James is being awesome.", creation_date=datetime.datetime.utcnow()))

    def teardown():
        with transaction.manager:
            session.query(MyEntry).delete()

    request.addfinalizer(teardown)


@pytest.fixture()
def dummy_request(new_session):
    """Call a dummy request."""
    return testing.DummyRequest(dbsession=new_session)


def test_home_view(dummy_request, new_session):
    """Test entries are in home view."""
    from .views.default import home_view
    new_session.add(MyEntry(title="test", body="this is a test", creation_date=datetime.datetime.utcnow()))
    new_session.flush()
    info = home_view(dummy_request)
    assert "entries" in info


def test_detail_view(new_session):
    """Test detail view has a body."""
    from .views.default import detail_view
    request = testing.DummyRequest(dbsession=new_session)
    new_session.add(MyEntry(title="test", body="this is a test", creation_date=datetime.datetime.utcnow()))
    new_session.flush()
    request.matchdict = {'id': '1'}
    info = detail_view(request)
    assert "this is a test" in info['entry'].body


def test_create_view():
    """Test create view."""
    from .views.default import create_view
    request = testing.DummyRequest()
    create_view(request)
    assert request.response.status_code == 200


def test_edit_view(new_session):
    """Test update view has a body."""
    from .views.default import edit_view
    request = testing.DummyRequest(dbsession=new_session)
    new_session.add(MyEntry(title="test", body="this is a test", creation_date=datetime.datetime.utcnow()))
    new_session.flush()
    request.matchdict = {'id': '1'}
    info = edit_view(request)
    assert info["entry"].body == "this is a test"

# -------Functional Tests----------


@pytest.fixture()
def testapp(sqlengine):
    """Setup TestApp."""
    from learning_journal import main
    app = main({}, **DB_SETTINGS)
    from webtest import TestApp
    return TestApp(app)


def test_layout_root_home(testapp, populated_db):
    """Test layout root of home route."""
    response = testapp.get('/', status=200)
    assert b'Vic Week 2 Day 5' in response.body


def test_layout_root_create(testapp):
    """Test layout root of create route."""
    response = testapp.get('/create', status=200)
    assert response.html.find("textarea")


def test_layout_root_edit(testapp, populated_db):
    """Test layout root of edit route."""
    response = testapp.get('/edit/1', status=200)
    html = response.html
    assert html.find("h2")


def test_layout_root_detail(testapp, populated_db):
    """Test layout root of detail route."""
    response = testapp.get('/detail/1', status=200)
    html = response.html
    assert html.find("p")


def test_root_contents_home(testapp, populated_db):
    """Test contents of root page contain as many <article> as journal entries."""
    response = testapp.get('/', status=200)
    html = response.html
    assert len(html.findAll("article")) == 1


def test_root_contents_create_notitle(testapp):
    """Test no title returns dictionary with error."""


def test_root_contents_detail(testapp, populated_db):
    """Test contents of detail page contains <p> in detail content."""
    response = testapp.get('/detail/1', status=200)
    assert b"James is being awesome." in response.body
