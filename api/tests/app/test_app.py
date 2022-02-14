from api.tests import BaseTestCase


class TestWebApp(BaseTestCase):

    def test_app(self):
        # print(self.app.config.get('ES_URL'))
        assert self.app is not None
        # assert 'localhost' not in self.app.config.get('ES_URL')


    def test_home_page_redirect(self):
        response = self.client.get('/')
        assert response.status_code == 200
