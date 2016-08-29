import pytest

from pyramid import testing


def test_home_view():
    """Test entries are in home view."""
    from .views import home_view
    request = testing.DummyRequest()
    info = home_view(request)
    assert "entries" in info


def test_detail_view():
    """Test detail view has a body."""
    from .views import detail_view
    request = testing.DummyRequest()
    request.matchdict = {'id': '1'}
    info = detail_view(request)
    assert "body" in info


def test_create_view():
    """Test create view."""
    from .views import create_view
    request = testing.DummyRequest()
    info = create_view(request)
    assert "entries" in info


def test_update_view():
    """Test update view has a body."""
    from .views import update_view
    request = testing.DummyRequest()
    request.matchdict = {'id': '1'}
    info = update_view(request)
    assert "body" in info

# -------Functional Tests----------


@pytest.fixture()
def testapp():
    """Setup TestApp."""
    from learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_root_home(testapp):
    """Test layout root of home route."""
    response = testapp.get('/', status=200)
    assert b'Vic Week 2 Day 5' in response.body


def test_layout_root_create(testapp):
    """Test layout root of create route."""
    response = testapp.get('/create', status=200)
    assert response.html.find("textarea")


def test_layout_root_edit(testapp):
    """Test layout root of edit route."""
    response = testapp.get('/edit/1', status=200)
    html = response.html
    assert html.find("h2")


def test_layout_root_detail(testapp):
    """Test layout root of detail route."""
    response = testapp.get('/1', status=200)
    html = response.html
    assert html.find("h2")


def test_root_contents_home(testapp):
    """Test contents of root page contain as many <article> as journal entries."""
    from .views import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll("article"))


def test_root_contents_create(testapp):
    """Test contents of root page contains <textarea> in create content."""
    response = testapp.get('/create', status=200)
    html = response.html
    assert html.find("textarea")


def test_root_contents_edit(testapp):
    """Test contents of edit page contains <input> in edit content."""
    response = testapp.get('/edit/1', status=200)
    html = response.html
    assert html.find("input")


def test_root_contents_detail(testapp):
    """Test contents of detail page contains <p> in detail content."""
    response = testapp.get('/1', status=200)
    html = response.html
    assert html.find("p")


# class ViewTests(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp()
#
#     def tearDown(self):
#         testing.tearDown()
#
#     def test_my_view(self):
#         from .views import my_view
#         request = testing.DummyRequest()
#         info = my_view(request)
#         self.assertEqual(info['project'], 'learning_journal')

#
# class FunctionalTests(unittest.TestCase):
#     def setUp(self):
#         from learning_journal import main
#         app = main({})
#         from webtest import TestApp
#         self.testapp = TestApp(app)
#
#     def test_root(self):
#         res = self.testapp.get('/', status=200)
#         self.assertTrue(b'Pyramid' in res.body)
