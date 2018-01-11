from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from lists.views import home_page
import re


class HomePageTest(TestCase):

    # NOTE: HACK!
    # The book uses Django 1.8, we're on another version.
    # The CSRF token will be present in the decoded response. If we add
    # the request to #render_to_string the tokens will be different.
    # String the token from the response.
    def __remove_token(self, content):
        csrf_regex = r'<input.+csrfmiddlewaretoken.+'
        return re.sub(csrf_regex, '', content)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_has_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        response_content = self.__remove_token(response.content.decode())
        expected_html = render_to_string('home.html')

        self.assertEqual(response_content, expected_html)

    def test_hame_page_handles_post_request(self):
        name = 'my new item'
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = name

        response = home_page(request)
        response_content = self.__remove_token(response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': name}
        )

        self.assertIn(name, response_content)
        self.assertEqual(response_content, expected_html)
