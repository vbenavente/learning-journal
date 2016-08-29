import pytest

from pyramid import testing


def test_home_view():
    from .views import home_view
    request = testing.DummyRequest()
    info = home_view(request)
    assert "entries" in info


def test_detail_view():
    from .views import detail_view
    request = testing.DummyRequest()
    request.matchdict = {'id': '1'}
    info = detail_view(request)
    assert "body" in info


def test_create_view():
    from .views import create_view
    request = testing.DummyRequest()
    info = create_view(request)
    assert "entries" in info


def test_update_view():
    from .views import update_view
    request = testing.DummyRequest()
    request.matchdict = {'id': '1'}
    info = update_view(request)
    assert "body" in info

# -------Functional Tests----------


@pytest.fixture()
def testapp():
    from learning_journal import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_root(testapp):
    response = testapp.get('/', status=200)
    assert b'Vic Week 2 Day 5' in response.body


def test_root_contents(testapp):
    """Test contents of root page contain as many <article> as journal entries."""
    from .views import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll("article"))


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
