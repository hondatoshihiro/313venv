from django.http import HttpRequest
from django.test import TestCase, Client, RequestFactory    #RequestFactoryをインポート
from django.urls import resolve
from snippets.views import top, snippet_new, snippet_edit, snippet_detail
from django.contrib.auth import get_user_model  #get_user_modelをインポート
from snippets.models import Snippet
from snippets.views import top

#class TopPageViewTest(TestCase):
#    def test_top_return_200(self):
#        request = HttpRequest()
#        response = top(request)
#        self.assertEqual(response.status_code, 200)
#
#    def test_top_return_expected_content(self):
#        request = HttpRequest()
#        response = top(request)
#        self.assertEqual(response.content, b"Hello World")

#class TopPageTest(TestCase):
#    def test_top_return_200(self):
#        response = self.client.get("/")
#        self.assertEqual(response.status_code, 200)
#
#    def test_top_return_expected_content(self):
#        response = self.client.get("/")
#        self.assertEqual(response.content, b"Hello World")
class TopPageTest(TestCase):
    def test_top_page_return_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "Djangoスニペット", status_code=200)

    def test_top_page_uses_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response,"snippets/top.html")

class CreateSnippetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        found = resolve("/snippets/new/")
        self.assertEqual(snippet_new, found.func)

class SnippetDetailTest(TestCase):
    def test_should_resolve_snippet_detail(self):
        found = resolve("/snippets/1/")
        self.assertEqual(snippet_detail, found.func)

class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve("/snippets/1/edit/")
        self.assertEqual(snippet_edit, found.func)

UserModel = get_user_model()
#実践Django Pythonによる本格Webアプリケーション開発(p.90)
class TopPageRenderSnippetsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = "test_user",
            email = "test@test.com",
            password = "passpass"
        )
        self.snippet = Snippet.objects.create(
            title = "title1",
            code = "print('hello')",
            description = "description1",
            created_by = self.user,
        )
    
    def test_should_return_snippet_title(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.snippet.title)

    def test_should_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)

#実践Django Pythonによる本格Webアプリケーション開発(p.100)
class SnippetDetailTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = "test_user",
            email = "test@test.com",
            password = "passpass"
        )
        self.snippet = Snippet.objects.create(
            title = "title2",
            code = "print('hello2')",
            description = "description2",
            created_by = self.user,
        )

    def test_should_use_expected_template(self):
        response = self.client.get("snippets/%s/" % self.snippet.id)
        self.assertTemplateUsed(response, "snippets/snippet_detail.html")

    def test_top_page_returns_200_and_expected_heading(self):
        response = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertContains(response, self.snippet.title, status_code=200)
