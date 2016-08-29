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

# import unittest
# import transaction
#
# from pyramid import testing
#
#
# def dummy_request(dbsession):
#     return testing.DummyRequest(dbsession=dbsession)
#
#
# class BaseTest(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp(settings={
#             'sqlalchemy.url': 'sqlite:///:memory:'
#         })
#         self.config.include('.models')
#         settings = self.config.get_settings()
#
#         from .models import (
#             get_engine,
#             get_session_factory,
#             get_tm_session,
#             )
#
#         self.engine = get_engine(settings)
#         session_factory = get_session_factory(self.engine)
#
#         self.session = get_tm_session(session_factory, transaction.manager)
#
#     def init_database(self):
#         from .models.meta import Base
#         Base.metadata.create_all(self.engine)
#
#     def tearDown(self):
#         from .models.meta import Base
#
#         testing.tearDown()
#         transaction.abort()
#         Base.metadata.drop_all(self.engine)
#
#
# class TestMyViewSuccessCondition(BaseTest):
#
#     def setUp(self):
#         super(TestMyViewSuccessCondition, self).setUp()
#         self.init_database()
#
#         from .models import MyModel
#
#         model = MyModel(name='one', value=55)
#         self.session.add(model)
#
#     def test_passing_view(self):
#         from .views.default import my_view
#         info = my_view(dummy_request(self.session))
#         self.assertEqual(info['one'].name, 'one')
#         self.assertEqual(info['project'], 'vic_learning_journal')
#
#
# class TestMyViewFailureCondition(BaseTest):
#
#     def test_failing_view(self):
#         from .views.default import my_view
#         info = my_view(dummy_request(self.session))
#         self.assertEqual(info.status_int, 500)
#
