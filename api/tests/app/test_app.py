from api.tests import BaseTestCase


class TestWebApp(BaseTestCase):

    def test_app(self):
        assert self.app is not None

    def test_home_page_redirect(self):
        response = self.client.get('/')
        assert response.status_code == 200
