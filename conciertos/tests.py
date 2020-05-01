from django.test import TestCase

# Create your tests here.
class TestViews(TestCase):
    def test_barra(self):
        check = '<img src="/static/conciertos/black_album.jpg" width="200" height="200" align="right">'
        response = self.client.get('/conciertos/')
        content = response.content.decode(encoding='UTF-8')
        self.assertInHTML(check, content)

    def test_nav(self):
        check = '<a class="nav-link" href="/conciertos/grupos/">Grupos</a>'
        response = self.client.get('/conciertos/')
        content = response.content.decode(encoding='UTF-8')
        self.assertInHTML(check, content)
